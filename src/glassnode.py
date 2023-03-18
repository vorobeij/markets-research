#!pip install yfinance
# !pip install mplfinance
import os
import json
import pandas as pd
import requests
from pathlib import Path

# insert your API key here
GLASSNODE_API_KEY = os.environ['GLASSNODE_API_KEY']
API_KEY = GLASSNODE_API_KEY


def save(filename, text):
    try:
        os.makedirs(Path(filename).parent.absolute())
    except FileExistsError:
        pass
    with open(filename, 'w') as outfile:
        outfile.write(text)


def saveJson(filename, jsonObj):
    with open(filename, 'w') as outfile:
        json.dump(jsonObj, outfile)


def playWithApiPoints():
    # Read api points
    f = open('output/glassnode_points.json')
    data = f.read()
    f.close()
    jsonData = json.loads(data)

    filtered = []
    for route in jsonData:
        if route['tier'] == 1:
            filtered.append(route)
    saveJson('output/glassnode_tier1.json', filtered)
    print(filtered)


def jsonStringToDf(data):
    try:
        df = pd.DataFrame(json.loads(data))
        df = df.set_index('t')
        df.index = pd.to_datetime(df.index, unit='s')
        df = df.sort_index()
        print(df.tail())
        return df
    except Exception as e:
        print(e)


def loadAndGet(url):
    res = requests.get('https://api.glassnode.com/' + url, params={'a': 'BTC', 'f': 'JSON', 'i': '24h', 'api_key': API_KEY})
    print(res.text)
    # save to file for later
    save(url + '.json', res.text)
    return res.text


def loadFileOrGetFromApi(url):
    try:
        f = open(url + '.json')
        data = f.read()
        return data
    except:
        return loadAndGet(url)


def loadGlassNodeData(url):
    # Try to get the data from file
    # If no files saved, load json from api
    # Save to file
    # Read data from file
    data = loadFileOrGetFromApi(url)
    df = jsonStringToDf(data)
    # convert to df
    print(df.tail())
    return df


glassnode_active_more_1y_percent = loadGlassNodeData('v1/metrics/supply/active_more_1y_percent')

if __name__ == '__main__':
    print(API_KEY)
    loadGlassNodeData('v1/metrics/supply/active_more_1y_percent')

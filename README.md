# Business cycles analysis

> Correlation between Google Trends and BTC price

1. Create `venv`
2. Install dependencies
    ```shell
    pip install pipreqs
    pip install -r src/requirements.txt
    ```
3. Launch `main.py`
4. See results at [dashboard.html](output/btc-example.pdf)
5. To see fresh results, download data from Google trends

# Ideas

[Coherence between signals](https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py)

# TODO

- [x] Download data from fred
  Example: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=1900-01-01&coed=2022-11-01&fq=Monthly
- [x] Download data from Yahoo
- [ ] Download OECD data?
- [ ] Draw multiple indexes on one plot
- [ ] Add MA to plots https://www.geeksforgeeks.org/how-to-calculate-moving-average-in-a-pandas-dataframe/
- [ ] Maps with animation of data from https://tradingeconomics.com/united-states/productivity

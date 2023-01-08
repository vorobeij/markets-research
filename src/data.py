def tradingeconomics_data():
    return [
        title_block("Lagging indicators"),
        oecd_embed("Household debt", "6W6X"),
        fred_embed("Personal Saving Rate (PSAVERT)", "YcRg"),
        oecd_embed("Household savings, Total, % of household disposable income", "6W6Z"),
        oecd_embed("Household disposable income, Gross, Per capita, percentage change, previous period last 8 quarters, Quarterly", "6W71"),
        oecd_embed("Household financial assets Shares and other equity, % of total financial assets 2021, Annual", "6W73"),
        oecd_embed("Business confidence index (BCI) Amplitude adjusted, Long-term average = 100 Jan 2008 – latest, Monthly", "6W75"),
        image_embed("SHSP SCFI Index China shipping activity", "https://www.sse.net.cn/index/indexImg?name=scfi&type=english"),
        fred_embed("10-Year Breakeven Inflation Rate (T10YIE)", "YcSw"),
        fred_embed("All Sectors; Total Capital Expenditures, Transactions (BOGZ1FA895050005Q)", "YcUT"),
        fred_embed("Rail Freight Carloads (RAILFRTCARLOADSD11)", "YcUU"),
        fred_embed("Industrial Production: Consumer Goods (IPCONGD)", "YcV4"),
        fred_embed("All Employees, Total Nonfarm (PAYEMS)", "YcV6"),
        fred_embed("Real personal income excluding current transfer receipts (W875RX1)", "YcVc"),
        fred_embed("Real Personal Consumption Expenditures (PCEC96)", "YcVf"),
        fred_embed("Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks (CCLACBW027SBOG)", "YcWi"),
        fred_embed("Real Personal Income (RPI)", "YcWf"),
        fred_embed("Average Weekly Hours of All Employees, Total Private (AWHAETP)", "Xpzv"),
        fred_embed("M2 (WM2NS)", "YcQ9"),
        fred_embed("Labor Force Participation Rate (CIVPART)", "Xd7G"),
        fred_embed("Real gross domestic product per capita (A939RX0Q048SBEA)", "YcQb"),
        fred_embed("Liabilities and Capital: Liabilities: Earnings Remittances Due to the U.S. Treasury: Wednesday Level (RESPPLLOPNWW)", "YcQq"),
        fred_embed("Assets: Total Assets: Total Assets (Less Eliminations from Consolidation): Wednesday Level (WALCL)", "Y0LS"),
        fred_embed("Federal Debt: Total Public Debt as Percent of Gross Domestic Product (GFDEGDQ188S)", "YcQu"),
        fred_embed("Inflation, consumer prices for the United States (FPCPITOTLZGUSA)", "QmPH"),
        fred_embed("Producer Price Index by Commodity: All Commodities (PPIACO)", "XoAU"),
        fred_embed("Chicago Fed National Financial Conditions Index (NFCI)", "XNGU"),
        fred_embed("Bank Prime Loan Rate (DPRIME)", "YcQD"),
        fred_embed("U.S. Net International Investment Position (IIPUSNETIQ)", "YcQE"),
        fred_embed("University of Michigan: Consumer Sentiment (UMCSENT)", "YcQI"),
        fred_embed("Job Openings: Total Nonfarm (JTSJOL)", "YcQL"),
        fred_embed("Overnight Reverse Repurchase Agreements: Treasury Securities Sold by the Federal Reserve in the Temporary Open Market Operations (RRPONTSYD)", "YcQO"),
        fred_embed("Total Vehicle Sales (TOTALSA)", "YcRk"),
        fred_embed("Auto Inventory/Sales Ratio (AISRSA)", "YcQS"),
        fred_embed("Commercial Real Estate Prices for United States (COMREPUSQ159N)", "YcRc"),
        fred_embed("Nonfinancial Corporate Business; Debt Securities and Loans; Liability, Level (BCNSDODNS)", "YcRe"),
        fred_embed("Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (CPIAUCSL)", "XCad"),
        fred_embed("Velocity of M2 Money Stock (M2V)", "Y0jn"),
        fred_embed("Household Debt Service Payments as a Percent of Disposable Personal Income (TDSP)", "YbfT"),
        tradingeconomicsc("Germany Industrial Production", "gripiyoy&v=202212070832V20220312"),
        tradingeconomicsc("Japan Industrial Production", 'jnipyoy&v=202212140448V20220312'),
        tradingeconomicsc("United States Philly Fed CAPEX Index", 'usapfci&v=202212151348V20220312'),
        tradingeconomicsc("United States Durable Goods Orders", 'unitedstadurgooord&v=202212231345V20220312&d1=20121229&h=300&w=600'),
        tradingeconomicsc("United States Nonfarm Labour Productivity", "unitedstapro&v=202212071341V20220312"),
        tradingeconomicsc("Germany Productivity", "germanypro&v=202212171002V20220312"),
        tradingeconomicsc("Euro Area Changes In Inventories", 'euroareachaininv&v=202212071124V20220312'),
        tradingview_embed("Baltic Exchange Dry Index", "INDEX%3ABDI"),
        tradingview_embed("btcusd", "BTCUSD"),
        tradingview_embed("US ISM Purchasing Managers Index", "USBCOI")
    ]


def gt_files():
    return [
        'data/gt/gt-stock-market-bubble.csv',  # look closer
        'data/gt/gt-market-bottom.csv',  # pay close attention
        'data/gt/gt-bear-market.csv',
        'data/gt/gt-bull-run.csv',
        'data/gt/gt-gas-prices.csv',
        'data/gt/gt-inflation.csv',
        'data/gt/gt-interest-rates.csv',
        'data/gt/gt-mortgage.csv',
        'data/gt/gt-refinance.csv',
        'data/gt/gt-shortage.csv',
        'data/gt/gt-treasury.csv',
        'data/gt/gt-market-crash.csv'
    ]


def tradingeconomicsc(name, symbol):
    return title_chart(name) + "<iframe src='https://d3fy651gv2fhd3.cloudfront.net/embed/?s=euroareachaininv&v=202212071124V20220312&d1=19980102&h=300&w=600' height='300' width='600'  frameborder='0' scrolling='no'></iframe>".replace("euroareachaininv&v=202212071124V20220312", symbol)


def tradingview_embed(name, symbol):
    return title_chart(name) + "<iframe src='xxx' height='300' width='600'  frameborder='0' scrolling='no'></iframe>".replace("xxx", "https://s.tradingview.com/widgetembed/?frameElementId=tradingview_c0869&symbol=BTCUSD&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=0&toolbarbg=rgba(255,%20255,%20255,%201)&studies=%5B%5D&hideideas=1&theme=White&style=2&timezone=Etc%2FUTC&withdateranges=1&hidevolume=1&studies_overrides=%7B%7D&overrides=%7B%22symbolWatermarkProperties.color%22%3A%22%23fff%22%2C%22volumePaneSize%22%3A%22tiny%22%7D&enabled_features=%5B%5D&disabled_features=%5B%22use_localstorage_for_settings%22%5D&locale=en&utm_source=tradingeconomics.com&utm_medium=widget&utm_campaign=chart&utm_term=INDEX%3ABDI#%7B%22page-uri%22%3A%22tradingeconomics.com%2Fcommodity%2Fbaltic%22%7D".replace("BTCUSD", symbol))


def fred_embed(name, symbolId):
    return title_chart(name) + '<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=symbolId&width=900&height=500" scrolling="no" frameborder="0" style="overflow:hidden; width:900px; height:600px;" allowTransparency="true" loading="lazy"></iframe>'.replace("symbolId", symbolId)


def oecd_embed(name, symbolId):
    return '<iframe src="https://data.oecd.org/chart/symbolId" width="900" height="675" style="border: 0" mozallowfullscreen="true" webkitallowfullscreen="true" allowfullscreen="true"><a href="https://data.oecd.org/chart/symbolId" target="_blank">title</a></iframe>'.replace("title", name).replace("symbolId", symbolId)


def image_embed(name, url):
    return title_chart(name) + '<img src="urllll"/>'.replace("urllll", url)


def random_embed(name, url):
    return title_chart(name) + '<iframe src="urllll" scrolling="no" frameborder="0" style="overflow:hidden; width:900px; height:600px;" allowTransparency="true" loading="lazy"></iframe>'.replace("urllll", url)


def title_block(text):
    return "<div><h1>" + text + "</h1></div>"


def title_chart(text):
    return "<div><h3>" + text + "</h3></div>"

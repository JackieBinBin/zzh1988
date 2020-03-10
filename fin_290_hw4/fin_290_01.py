import pandas
import requests
from bs4 import BeautifulSoup

def get_coinmarketcap_his_info(url,start_date,end_date):

    # 通过requests 请求页面获取对应文档
    response = requests.get(url.format(start_date,end_date))

    # 通过BeautifulSoup解析html返回的结果
    history_data = BeautifulSoup(response.text,"html.parser")

    value_list = []

    # 通过css选择器获取页面元素内容
    for items in history_data.select("table tr.cmc-table-row"):
        # 通过指定页面元素获取指定标签的内容
        for item in items.select_one("td.cmc-table__cell").find_next_siblings():
            value_list.append(item.get_text())
        new_dict = dict(zip(['open', 'high', 'low','close','volume','marketcap'],value_list))
        # 生成
        yield new_dict['close'],new_dict['volume'],new_dict['marketcap']
        value_list = []



if __name__ == '__main__':

    # scrape the historical data for the current top 3 cryptocurrencies: bitcoin (BTC),
    # ethereum (ETH), and ripple (XRP) between the time periods indicated below.

    btc_link = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={}&end={}'
    eth_link = 'https://coinmarketcap.com/currencies/ethereum/historical-data/?start={}&end={}'
    xrp_link = 'https://coinmarketcap.com/currencies/xrp/historical-data/?start={}&end={}'

    url_list = {"btc_link":btc_link,"eth_link":eth_link,"xrp_link":xrp_link}

    # Do that for the following sets of dates:
    # (a) March 30th 2019 to May 30th 2019
    # (b) June 5th 2019 to June 15th 2019
    # (c) Feb 23 2020 to March 2nd 2020

    time_range = [('20190330','20190530'),('20190605','20190615'),('20200223','20200302')]

    for url in url_list.keys():
        for times in time_range:
            print(f'obtain {url} data')
            print(f'Time range {times[0]} - {times[1]}')
            df = (elem for elem in get_coinmarketcap_his_info(url_list[url],times[0],times[1]))
            df = pandas.DataFrame(df,columns=['Close','Volume','Market Cap'])
            # print(df)

import requests
from lxml import html
import matplotlib.pyplot as plt
import pandas as pd

# 发送HTTP请求
url = 'https://www.hko.gov.hk/tide/WAGtextPH2024.htm'
response = requests.get(url)

# 检查请求是否成功
if response.ok:
    # 解析HTML内容
    tree = html.fromstring(response.content)
    
    # 提取数据
    data = []
    rows = tree.xpath('//table/tr')[1:]  # 跳过表头
    for row in rows:
        cells = row.xpath('td')
        if cells:
            date = cells[0].text_content().strip()
            hours = [float(cell.text_content().strip()) for cell in cells[1:]]
            data.append((date, hours))
    
    # 转换数据
    df = pd.DataFrame(data, columns=['Date', 'Heights'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # 可视化数据
    plt.figure(figsize=(12, 6))
    for hour in range(24):
        plt.plot(df.index, df['Heights'].apply(lambda x: x[hour]), label=f'Hour {hour:02d}')
    
    plt.title('Tidal Heights at Waglan Island in 2024')
    plt.xlabel('Date')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print('Failed to retrieve data:', response.status_code)
    
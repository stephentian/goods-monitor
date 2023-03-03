import requests
import smtplib
import time

# china
url = "https://api-cn.louisvuitton.cn/api/zhs-cn/catalog/skuavailability/M45647?origin=qubit"
url1 = "https://api-cn.louisvuitton.cn/api/zhs-cn/catalog/availability/nvprod2440099v"

# hongkong(china)
url3 = "https://api.louisvuitton.com/api/zht-hk/catalog/availability/nvprod2440099v"
url4 = "https://www.louisvuitton.cn/zhs-cn/products/boite-chapeau-souple-mm-monogram-nvprod2440099v/M45647"

headers = {
    # ':authority': 'api-cn.louisvuitton.cn',
    # ':scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'g	zip, deflate, br',
    'accept-language': 'zh-CN, zh;q = 0.9, en;q = 0.8',
    'cache-control': 'no-cache',
    'content-type': 'text/plain',
    'origin': 'https://www.louisvuitton.cn',
    'pragma': 'no-cache',
    'referer': 'https://www.louisvuitton.cn/zhs-cn/products/boite-chapeau-souple-mm-monogram-nvprod2440099v/M45647',
    'sec-ch-ua': "'Not_A Brand';'v = 99', 'Google Chrome';'v = 109', 'Chromium';'v = 109'",
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "macOS",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': "Mozilla/5.0 (Macintosh;Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

# try:
# 	s = requests.get(url, headers=headers, timeout=(3, 7))
# 	print("success")
# except requests.exceptions.RequestException as e:
# 	print(e)

# print(s.status_code)

# print(s.reason)

# print(s.apparent_encoding)

# print("s.json(): ", s.json())
# print("inStock: ", s.json().get('inStock', False))

# print("Hello world!")

# 定义邮件内容
subject = 'Louis Vuitton包包库存状态更新'
body = '包包的库存已经更新，请尽快购买。'

# 定义发送邮件的函数


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    msg = "Subject: {}\n\n{}".format(subject, body)
    server.sendmail(from_addr, to_addr, msg)
    server.quit()


# 设置轮询比较频率
interval = 1 * 60  # 5分钟监控一次

# 开启监控
while True:
    # 发起API请求并得到返回的数据
    response = requests.get(url1)
    if response.status_code == 200:
        data = response.json()

        # 提取需要的数据：inStock字段
        in_stock = data.get('inStock', False)

        print("Hello world!")

        # 如果包包有货，发送邮件通知
        if in_stock:
            # send_email()
            print("Hello world!")
    else:
        print("error")

        # 等待一段时间再次请求 API
        time.sleep(interval)

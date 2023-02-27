import requests

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

try:
	s = requests.get(url, headers=headers, timeout=(3, 7))
	print("success")
except requests.exceptions.RequestException as e:
	print(e)

# print(s.status_code)

# print(s.reason)

# print(s.apparent_encoding)

print(s.text)

print("Hello world!")

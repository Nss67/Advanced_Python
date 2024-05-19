import requests as rq
# import pandas as pd

# r = rq.get("https://www.python.org")
#
# print(dir(r))
# print(r.url)
# logo = rq.get("https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png")
#
# with open("site.txt", mode="w") as site:
#     site.write(r.text)
#
# with open("requests_site_logo.png", mode="wb") as _logo:
#     _logo.write(logo.content)

# test with httpbin.org
# _get = rq.get("https://httpbin.org/get")
# print(_get)
# print(_get.status_code)
# print(_get.ok)
# print(_get.headers)

# test with wikipedia
# r = rq.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
#
# data_frame = pd.read_html(r.content)
# print(len(data_frame))
#
# data_frame = data_frame[0]
#
# print(data_frame.columns)
#
# data_frame = data_frame.loc[:, ['Location', 'Population', '% of world', 'Date',
#                                 'Source (official or from the United Nations)']]
#
# print(data_frame)
#
# data_frame.to_csv("World Population.csv")

# r = rq.get("https://httpbin.org/get")
# r2 = rq.get("https://httpbin.org/get?key=value")
# r3 = rq.get("https://httpbin.org/get?Nss67=88")
# print(r.text)
# request1 = r.json()
# request2 = r2.json()
# request3 = r3.json()
# print(request1)
# print(request2)
# print(request3)
#
# data_for_send = {
#     "Milad": 15,
#     "Amin": 17,
#     "Sahel": 20
# }
# r4 = rq.get("https://httpbin.org/get", params=data_for_send)
# request4 = r4.json()
# print(request4)


data_for_send = {
    "Milad": 15,
    "Amin": 17,
    "Sahel": 20
}
p = rq.post("https://httpbin.org/post", data=data_for_send)
print("your status code is:", p.status_code)
response = p.json()
print(type(response))
for k, v in response.items():
    print(k, v)

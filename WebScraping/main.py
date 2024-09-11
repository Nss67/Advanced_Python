from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = "https://www.myfxbook.com/forex-economic-calendar"
# respond = requests.get(url)
# status_respond_code = respond.status_code
# print(status_respond_code)
#
# bs = BeautifulSoup(respond.content, "html.parser")


# find_title = bs.find("h1").get_text()
# print(find_title)
#
# # way 1
# print("\nway 1")
# find_by_id_1 = bs.find(id="calRow245784").get_text().split("\n ''")
# print(find_by_id_1)
#
#
# # way 2 the best way
# print("\nway 2")
# find_by_id_2 = bs.find("tr", attrs={"data-row-id": "245784"}).get_text().split("\n ''")
# print(find_by_id_2)
#
# # way 1
# print("\nway class 1")
# find_by_class = (bs.find(class_="table table-hover dont-color-tds-hover text-center no-margin-bottom font11").
#                  find("tr", attrs={"data-row-id": "245784"}).get_text()).split("\n ''")
# print(find_by_class)
#
# # way 2 the best way
# print("\nway class 2")
# find_by_class_2 = (bs.find("table", attrs={"class": "table table-hover dont-color-tds-hover text-center no-margin-bottom font11"}).
#                    find("tr", attrs={"data-row-id": "245784"}).get_text().split("\n ''"))
# print(find_by_class_2)
#
# # find all elements
# print("\nFind All  01")
# find_all_impact = bs.find_all("div", attrs={"class": "impact_high"})
# print(find_all_impact)
# print(len(find_all_impact))
# print(type(find_all_impact))
#
# # find all elements
# print("\nFind All  02")
# find_all_impact_02 = bs.findAll("div", attrs={"class": "impact_high"})
# print(find_all_impact_02)
# print(len(find_all_impact_02))
# print(type(find_all_impact_02))
# print()
# print(find_all_impact == find_all_impact_02)
# print()
#
# # CSS selectors > select_one
# select_one_by_id_1 = bs.select_one("#calRow245784").get_text().split("\n ''")
# print(select_one_by_id_1)
# print("\n", select_one_by_id_1 == find_by_id_1, "\n")
#
# select_one_by_class_1 = (bs.select_one(".page-content-inner").find(attrs={"data-row-id": "245784"}).
#                          get_text()).split("\n ''")
# print(select_one_by_class_1)
# print("\n", select_one_by_class_1 == find_by_class, "\n")
#
# select_all_news = bs.select(".economicCalendarRow")
# print(select_all_news)
# print(len(select_all_news))

# ===============================================================
# print("Good way")
# find_1 = bs.find("tbody").find(attrs={"class": "impact_high"}).get_text().strip()
# find_2 = bs.find("tbody").find(attrs={"class": "impact_high"}).get("class")
# find_3 = bs.find("tbody").find(attrs={"class": "impact_high"})["class"]
# print(find_1)
# print(find_2)
# print(find_3)
# ================================================================

url = "https://www.myfxbook.com/forex-economic-calendar"
respond = requests.get(url)
status_respond_code = respond.status_code
print(status_respond_code)

bs = BeautifulSoup(respond.content, "html.parser")

counter = 0
_array = []
date_time = None
country = None
event = None
subject = None
# impact_low = None
# impact_medium = None
# impact_high = None
impact = None
tbody = bs.find("tbody")
economic_rows = tbody.findAll("tr", attrs={"class": "economicCalendarRow"})
print(len(economic_rows))
for row in economic_rows:
    cells = row.findAll("td", attrs={"class": "calendarToggleCell"})
    event_cell = row.find("td", attrs={"class": "calendarToggleCell text-left"})
    events = event_cell.find("a", attrs={"class": "calendar-event-link"})
    events_subject = event_cell.find("span")
    if events_subject:
        subject = events_subject.get_text().strip()
    if events:
        event = events.get_text().strip()
    for cell in cells:
        symbol = cell.get_text().strip()
        date = cell.find("div", attrs={"class": "align-center calendarDateTd"})
        countries = cell.find("i", attrs={"title": "United States"})
        impacts_low = cell.find("div", attrs={"class": "impact_low"})
        impacts_medium = cell.find("div", attrs={"class": "impact_medium"})
        impacts_high = cell.find("div", attrs={"class": "impact_high"})
        if impacts_low:
            impact = impacts_low.get_text().strip()
        if impacts_medium:
            impact = impacts_medium.get_text().strip()
        if impacts_high:
            impact = impacts_high.get_text().strip()
        if countries:
            country = countries.get("title")
        if date:
            date_time = date.get("data-calendardatetd")
        if symbol == "USD":
            counter += 1
            _list = [date_time, symbol, country, event, subject, impact]
            _array.append(_list)
            # print(counter, date_time, symbol, country, event, subject, impact)
            break


df = pd.DataFrame(_array, columns=["date-time", "symbol", "country", "event", "subject", "impact"])
df.index = range(1, len(df) + 1)
df.to_csv("./Economic_Calendar_News.csv")
print(df)
print(len(df))
impact_list = list(df["impact"])
time_list = list(df["date-time"])
print(impact_list)
print(time_list[0])
print(time_list[0].split(" "))
print(time_list[0].split(" ")[0])

# url2 = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
# respond2 = requests.get(url2)
# print(respond2.status_code)
# bs2 = BeautifulSoup(respond2.content, "html.parser")
#
# find_p = bs2.find_all(attrs={"class": "mw-default-size mw-halign-none"})
# for p in find_p:
#     links = p.find('a')
#     img = links.find('img')
#     if links:
#         link = links.get("href")
#         src = img.get("src")
#         print(link)
#         print(src)




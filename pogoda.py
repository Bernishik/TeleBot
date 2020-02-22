import requests
import bs4


def getPogoda():
    url = "https://sinoptik.ua/погода-лодзь-103093133"
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    # time
    time1 = b.select("tr.gray")
    time2 = time1[0].getText().split()
    # температура
    t1 = b.select("tr.temperature")
    t2 = t1[0].getText().split()
    # давление
    g1 = b.select("tr.gray")
    g2 = g1[1].getText().split()
    p = 0
    time2 = time2[::2]
    for k in time2:
        time2[p] = k + ":00"
        p += 1

    print(time2)
    return [time2, t2, g2]

# time;

# print( + '\n' + t2 + '\n' + g2)
# for i in time2:
#     time += i.replace(' ', '') + ' '
# print(time)
# print(time2 + '\n' + t2 + '\t' + g2)
# print(d2)
# dollar = "Доллар = " + d2[0] + " \ " + list.pop(d2)
# euro = "Євро = " + e2[0] + " \ " + list.pop(e2)
# plz = "Злотий = " + p2[0] + " \ " + list.pop(p2)

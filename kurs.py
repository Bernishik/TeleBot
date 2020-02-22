import requests
import bs4


def getCurse():
    url = "https://minfin.com.ua/currency/banks/"
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    d1 = b.select(".mfm-table.mfcur-table-lg-banks>tbody>tr>td:nth-child(2)")
    d2 = d1[0].getText().split()
    e2 = d1[1].getText().split()
    p2 = d1[3].getText().split()
    dollar = "Доллар = " + d2[0] + " \ " + list.pop(d2)
    euro = "Євро = " + e2[0] + " \ " + list.pop(e2)
    plz = "Злотий = " + p2[0] + " \ " + list.pop(p2)
    return [dollar, euro, plz]


def getCursePln():
    url = "http://kantorlodz.pl/wszystkie-waluty-hurt"
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    d1 = b.select("#USD_hk , #USD_hs ")
    d2 = d1[0].getText().split() + d1[1].getText().split()

    e1 = b.select("#EUR_hk , #EUR_hs ")
    e2 = e1[0].getText().split() + e1[1].getText().split()

    u1 = b.select("#UAH_hk , #UAH_hs ")
    u2 = u1[0].getText().split() + u1[1].getText().split()
    dollar = "Доллар = " + d2[0] + " \ " + list.pop(d2)
    euro = "Євро = " + e2[0] + " \ " + list.pop(e2)
    uan = "Гривня = " + u2[0] + " \ " + list.pop(u2)
    return [dollar, euro, uan]


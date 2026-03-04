import requests

cookies = {
    "FCCDCF": "%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%226aff86c2-2169-48ee-96e2-12ad68fd7158%5C%22%2C%5B1772644564%2C340000000%5D%5D%22%5D%5D%5D",
    "_gid": "GA1.2.1455210565.1772644565",
    "_ga_DJLCSW50SC": "GS2.1.s1772654665$o2$g1$t1772655255$j60$l0$h0",
    "_ga_D6NF5QC4QT": "GS2.1.s1772654665$o2$g1$t1772655255$j60$l0$h0",
    "_ga": "GA1.2.2039575976.1772644564",
    "_gat_gtag_UA_29446588_1": "1",
    "FCNEC": "%5B%5B%22AKsRol8uVBboaEEOnXx61t2NIqB6aI2HiDp-wwkwY44_sGNkLdClAHx-kWjG8IKOEO4FXKc_MK5aAJcLzvb-5D7mMwEdsWI5Bj_vjI4v8KXVIkcevdg2zTHH-UKvRyc7PU5IqnWt-yYwrsYoKDHEMhF5t378t9fxtw%3D%3D%22%5D%5D",
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://www.residentevildatabase.com/personagens/",
    "sec-ch-ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    # 'cookie': 'FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%226aff86c2-2169-48ee-96e2-12ad68fd7158%5C%22%2C%5B1772644564%2C340000000%5D%5D%22%5D%5D%5D; _gid=GA1.2.1455210565.1772644565; _ga_DJLCSW50SC=GS2.1.s1772654665$o2$g1$t1772655255$j60$l0$h0; _ga_D6NF5QC4QT=GS2.1.s1772654665$o2$g1$t1772655255$j60$l0$h0; _ga=GA1.2.2039575976.1772644564; _gat_gtag_UA_29446588_1=1; FCNEC=%5B%5B%22AKsRol8uVBboaEEOnXx61t2NIqB6aI2HiDp-wwkwY44_sGNkLdClAHx-kWjG8IKOEO4FXKc_MK5aAJcLzvb-5D7mMwEdsWI5Bj_vjI4v8KXVIkcevdg2zTHH-UKvRyc7PU5IqnWt-yYwrsYoKDHEMhF5t378t9fxtw%3D%3D%22%5D%5D',
}

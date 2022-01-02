import requests
import re
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}


res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()#가격
    rate = item.find("em", attrs={"class":"rating"})#평점
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})

    if ad_badge:
        #print("     <광고 상품 제외합니다.>")
        continue

    if "Apple" in name:
        #print("     <Apple 상품 제외합니다.>")
        continue

    if rate:
        rate = rate.get_text()
    else:
        #print("     <평점 없는 상품 제외합니다.>")
        continue
    #평점 수
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        #print("     <리뷰 수 없는 상품 제외합니다.>")
        continue
    if float(rate) >=4.5 and float(rate_cnt) >=50:
        print("상품명 : " + name)
        print("가격 : " + price + "원")
        print("평점 : " + rate)
        print("리뷰 수 : " + rate_cnt)



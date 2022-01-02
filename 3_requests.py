import requests
res = requests.get("http://google.com")
res.raise_for_status() #2,3줄 쌍으로 습관적으로 쓴다. 3번줄 = 오류있으면 바로 종료하는 뜻
print("응답코드 :",res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")

print(len(res.text))
#print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
    #mygoogle.html을 만들어서 그 안에 내용을 "w" write 한다.
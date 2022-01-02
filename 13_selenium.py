from selenium import webdriver
import time

browser = webdriver.Chrome()  # 현재 폴더에 있으니까  "./chromedriver.exe"

#1. 네이버로 이동
browser.get("http://naver.com")

#2. 로그인 버튼 입력
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. 아이디와 비밀번호 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(1) # 시간 기다리기

#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("123r_id")

#6. html 정보 출력
#print(browser.page_source)

#7. 브라우저 종료
#browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 

browser = webdriver.Chrome()
# browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)#1. 네이버항공권으로 이동

#2. 가는날 선택 버튼 입력
elem = browser.find_element_by_link_text("가는날 선택").click()

#9월 27일, 28일 선택
# elem = browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# elem = browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

#10월 27일, 28일 선택
# elem = browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# elem = browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

#9월 27일, 10월 28일 선택
elem = browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
elem = browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

#제주도 선택
#elem = browser.find_element_by_class_name("bg_gradient").click() #둘 다 기능함

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click() #둘 다 기능함

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

#로딩 기다리기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) 
    #      WebDriverWait통해 브라우져를 최대 10초기다림 10초 지나가면 에러
    #                                       EC= expected condition 어떤 조건으로 기다리는데 그것은 위XPATH값에 해당하는 element가 위치할때 까지
    #                                                                       튜플형태로!!!!          
    #성공했을 때 동작 수행
    print(elem.text) #첫번째 결과 출력
finally:
    browser.quit()

# elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")) 
# #      WebDriverWait통해 브라우져를 최대 10초기다림 10초 지나가면 에러              
# #                                       EC= expected condition 어떤 조건으로 기다리는데 그것은 위XPATH값에 해당하는 element가 위치할때 까지
# #성공했을 때 동작 수행
# print(elem.text)#첫번째 결과 출력
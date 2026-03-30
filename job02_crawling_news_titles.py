import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

category = ['Politics', 'Economy', 'Social', 'Culture', 'World', 'IT']

options = ChromeOptions()
options.add_argument('lang=ko_KR')
# options.add_argument('headless')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# 본인 카테고리
my_section = 0

url = 'https://news.naver.com/section/10{}'.format(my_section)
driver.get(url)

# for i in range(10):
#     time.sleep(0.5)
#     button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]'
#     driver.find_element(By.XPATH, button_xpath).click()

while True:
    try:
        button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]'
        driver.find_element(By.XPATH, button_xpath).click()
    except:
        break

time.sleep(1)
title_tags = driver.find_elements(By.CLASS_NAME, 'sa_text_strong')

titles = []
for title in title_tags:
    titles.append(title.text)
df_titles = pd.DataFrame(titles, columns=['title'])
df_titles['category'] = category[my_section]
print(df_titles.head())
df_titles.info()
df_titles.to_csv('./crawling_data/news_titles_{}.csv'.format(category[my_section]))
import requests
# from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import pytesseract as tess
from PIL import Image

img = Image.open('text.png')
text = tess.image_to_string(img)

print(text)



#
# site ='https://10fastfingers.com/typing-test/turkish'
#
#
#
#
#
# driver_path = "/Users/Suleymanefecelik/Desktop/Yazilim/chromedriver"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://10fastfingers.com/typing-test/turkish')
#
# time.sleep(50)
# inp = driver.find_element_by_id('inputfield')
# test = driver.find_element_by_class_name('highlight')
# while test.text:
#     time.sleep(0.3)
#     inp.send_keys(test.text + ' ')
#     test = driver.find_element_by_class_name('highlight')
#
#
#
#
# print(test.text)
#
#

#
# r = requests.get(site)
# soup = bs(r.content, "html.parser")
# entryler = soup.find('div', 'reload-box')
# print(entryler)


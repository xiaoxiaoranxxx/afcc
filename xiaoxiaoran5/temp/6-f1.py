from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
import pyexcel

driver = webdriver.Chrome(r'D:\Temp\chromedriver.exe')
driver.get('http://flight.qunar.com')
driver.implicitly_wait(10)
# driver.click()
# driver.send_keys('澳门')
# driver.send_keys(Keys.RETURN)
driver.find_element_by_css_selector('button.btn_search').click()

flights = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[@class="m-airfly-lst"]/div[@class="b-airfly"]')))
for f in flights:
    fdata = {}
    airlines = f.find_elements_by_xpath('//div[@class="m-airfly-lst"]/div[@class="b-airfly"]//div[@class="d-air"]')
    fdata['airlines'] = [airline.text.replace('\n','-') for airline in airlines]
    fdata['depart'] = f.find_elements_by_xpath('//div[@class="m-airfly-lst"]/div[@class="b-airfly"]//div[@class="sep-lt"]').text
    fdata['time'] = f.find_elements_by_xpath('//div[@class="m-airfly-lst"]/div[@class="b-airfly"]//div[@class="sep-ct"]').text
    fdata['dest'] = f.find_elements_by_xpath('//div[@class="m-airfly-lst"]/div[@class="b-airfly"]//div[@class="sep-rt"]').text

    fake_price = list(f.find_elements_by_xpath('//span[@class="prc_wp"]/em/b[1]').text)
    covers = f.find_elements_by_xpath('//span[@class="prc_wp"]/em/b[position()>1]')
    for c in covers:
        index = int(c.value_of_css_property('left')[:-2])  // c.size['width']
        fake_price[index] = c.text
    fdata['price'] = ''.join(fake_price)
    print(fdata)



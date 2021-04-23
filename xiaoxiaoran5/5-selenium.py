from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import time
import pyexcel

if __name__ == "__main__":
    keyword = 'iphone'
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    option = Options()
    # option.add_argument('--headless')
    driver = webdriver.Chrome(
        r'D:\Temp\chromedriver.exe', chrome_options=option)
    driver.get('http://www.jd.com')
    kw = driver.find_element_by_id('key')
    kw.send_keys(keyword)
    kw.send_keys(Keys.RETURN)
    time.sleep(3)
    sort_btn = driver.find_element_by_xpath('.//div[@class="f-sort"]/a[2]')
    sort_btn.click()
    i = 0
    has_next = True
    rows = []
    page_count = 0
    while has_next:
        page_count += 1
        if page_count > 3:
            break
        time.sleep(5)
        cur_page = driver.find_element_by_xpath(
            '//div[@id="J_bottomPage"]//a[@class="curr"]').text
        print('current page is ---------------------> %s ' % cur_page)

        goods_list = driver.find_element_by_id('J_goodsList')  # 尺寸
        y = goods_list.rect['y'] + goods_list.rect['height']  # 滑
        driver.execute_script('window.scrollTo(0,%s)' % y)

        products = driver.find_elements_by_class_name('gl-item')

        for p in products:
            row = {}
            sku = p.get_attribute('data-sku')
            row['price'] = p.find_element_by_css_selector(
                'strong.J_%s' % sku).text
            row['name'] = p.find_element_by_css_selector(
                'div.p-name>a>em').text
            row['comment'] = p.find_element_by_id('J_comment_%s' % sku).text

            try:
                row['shop'] = p.find_element_by_css_selector(
                    'div.p-shop>span>a').text
            except:
                row['shop'] = '无'

            print(row)

            i += 1
            print('-------->', i)
            rows.append(row)
        try:
            next_page = driver.find_element_by_css_selector('a.pn-next')
            if 'disabled' in next_page.get_attribute('class'):
                has_next = False
            else:
                next_page.click()
        except:
            has_next = False

    pyexcel.save_as(records=rows, dest_file_name='%s.xls' % keyword)
    driver.quit()

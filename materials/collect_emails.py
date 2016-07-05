# dependencies
# 1. selenium

from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hits = []
# years = xrange(2005, 201)5

# Open a session
driver = webdriver.Firefox()

# Open a web of knowledge session
driver.get("https://webofknowledge.com")

# select web of science database
elem = driver.find_element_by_xpath('//*[@id="collectionDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="collectionDropdown"]/ul/li[2]/a')
elem.click()

# setup search
elem = driver.find_element_by_xpath('//*[@id="value(input1)"]')
elem.send_keys('2005-2015')
elem = driver.find_element_by_xpath('//*[@id="s2id_select1"]/a/span[2]/b')
elem.click()
elem.send_keys(Keys.ARROW_DOWN *8)
elem.send_keys(Keys.ENTER)
elem = driver.find_element_by_xpath('//*[@id="addSearchRow1"]/span[1]/a')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="value(input2)"]')
elem.send_keys('psychology')
elem.send_keys(Keys.ENTER)

# refining search
elem = driver.find_element_by_xpath('//*[@id="DocumentType_1"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="DocumentType_tr"]/div[3]/a')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="ResearchArea_img"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="ResearchArea_1"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="ResearchArea_tr"]/div[3]/a')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="Language_img"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="Language_1"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="Language_tr"]/div[3]/a')
elem.click()

# 50 p/page
elem = driver.find_element_by_xpath('//*[@id="s2id_selectPageSize_.bottom"]/a/span[2]/b')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="selectPageSize_.bottom"]/option[3]')

# loop over pages
# take into account a max of 5000 hits to be put on marked list
# this is 100 pages and 99 next page clicks
for i in xrange(0,5):
    # create loop over ascending/descending
    # create loop over 500 marked list
    elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[23]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
    elem.click()
    # navigate to next page
    # automatically adds selected to marked list
    elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a/i')
    elem.click()

    i = 1 
    while(not (i % 100 == 0)):
        # select all
        elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[23]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
        elem.click()
        # navigate to next page
        # automatically adds selected to marked list
        elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a/i')
        elem.click()
        i += 1
    raw_input('Download the lists, clear marked list, go back to searches and click next page. THEN press enter')

# Close a session
driver.close()

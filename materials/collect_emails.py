from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hits = []
years = xrange(2004, 2015)

# Open a session
driver = webdriver.Firefox()

# Open a web of knowledge session
driver.get("https://webofknowledge.com")

# select web of science database
elem = driver.find_element_by_xpath('//*[@id="collectionDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="collectionDropdown"]/ul/li[2]/a')
elem.click()

# set to search for year publsihed
elem = driver.find_element_by_xpath('//*[@id="s2id_select1"]/a')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="select2-results-1"]')
elem.click()

# Search the year
elem = driver.find_element_by_xpath('//*[@id="value(input1)"]')
elem.send_keys('2014') # REPLACE by year variable at end
elem.send_keys(Keys.RETURN)

# select only english
elem = driver.find_element_by_xpath('//*[@id="Language_img"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="Language_1"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="Language_tr"]/div[3]/a')
elem.click()

# select only journal articles
elem = driver.find_element_by_xpath('//*[@id="DocumentType_1"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="DocumentType_tr"]/div[3]')
elem.click()

# save number of hits
elem = driver.find_element_by_xpath('//*[@id="hitCount.top"]')
hits.append(elem.get_attribute('content'))

# select Publication date -- newest to oldest [is default]

# make the search page return 50 hits
elem = driver.find_element_by_xpath('//*[@id="s2id_selectPageSize_.bottom"]/a')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="select2-results-5"]')
elem.click()

# select all
elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[19]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
elem.click()

# navigate to next page and automatically add to marked list
elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a')
elem.click()

# go to marked list

# identify number of records on marked list
elem = driver.find_element_by_xpath('//*[@id="skip-to-navigation"]/ul[2]/li[3]/a/span')
marked = elem.get_attribute('content')

# ensure only corresponding and source are checked
# select all
elem = driver.find_element_by_xpath('//*[@id="value(select_All)"]')
elem.click()
# unselect all
elem = driver.find_element_by_xpath('//*[@id="value(select_All)"]')
elem.click()
# select only corresponding and source
elem = driver.find_element_by_xpath('//*[@id="ADDRS_fields"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="SOURCE_fields"]')
elem.click()

# download marked list per 500
# iterate over records for download
elem = driver.find_element_by_xpath('//*[@id="markFrom"]')

elem = driver.find_element_by_xpath('//*[@id="markTo"]')

# select Publication date -- oldest to newest

# navigate through pages and add each page to marked list

# download marked list per 500

# Close a session
driver.close()
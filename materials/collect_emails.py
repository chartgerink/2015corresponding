# dependencies
# 1. selenium

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

# go to advanced search
elem = driver.find_element_by_xpath('/html/body/div[1]/div[19]/h2/i')
elem.click()
elem = driver.find_element_by_xpath('/html/body/div[1]/div[19]/h2/i/ul/li[4]/a')
elem.click()

# select only english
elem = driver.find_element_by_xpath('//*[@id="value(input2)"]/option[2]')
elem.click()

# select only articles
elem = driver.find_element_by_xpath('//*[@id="value(input3)"]/option[2]')
elem.click()

for year in years:
    # enter the year
    elem = driver.find_element_by_xpath('//*[@id="value(input1)"]')
    elem.send_keys('PY=%s' % str(year)) # REPLACE 2014 by year variable at end
    elem = driver.find_element_by_xpath('//*[@id="searchButton"]/input')
    elem.click()

# for search in xrange(1, len(years) + 1):
# open the next search
xpath = '//*[@id="set_%s_div"]/a' % str(search)
elem = driver.find_element_by_xpath(xpath)
hits.append(elem.get_attribute('content'))
elem.click()

# loop over pages
# take into account a max of 5000 hits to be put on marked list
# this is 100 pages and 99 next page clicks

# create loop over ascending/descending
# create loop over 500 marked list

i = 0 
while(not (i % 50 == 0)):
	# select all
    elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[19]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
    elem.click()
    # navigate to next page
    # automatically adds selected to marked list
    elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a')
    elem.click()
    i += 1

# navigate to marked list
elem = driver.find_element_by_xpath('//*[@id="skip-to-navigation"]/ul[2]/li[3]/a')
elem.click()

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

# need to implement the downloading itself...
elem = driver.find_element_by_xpath('//*[@id="s2id_saveToMenu"]/a/span[2]/b')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="select2-drop"]')
elem.click()
###

# empty marked list
elem = driver.find_element_by_xpath('//*[@id="output_form"]/div[3]/span/input[2]')
elem.click()
try:
    selsend_keys(Keys.RETURN)
except selenium.common.exceptions.UnexpectedAlertPresentException

elem = driver.find_element_by_xpath('//*[@id="skip-to-navigation"]/ul[1]/li[2]/a')
elem.click()




# go to marked list



# download marked list per 500
# iterate over records for download
elem = driver.find_element_by_xpath('//*[@id="markFrom"]')

elem = driver.find_element_by_xpath('//*[@id="markTo"]')

# select Publication date -- oldest to newest

# navigate through pages and add each page to marked list

# download marked list per 500

# Close a session
driver.close()
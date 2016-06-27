# dependencies
# 1. selenium

from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hits = []
years = xrange(2011,2015)

for year in years:
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

    # enter the year
    elem = driver.find_element_by_xpath('//*[@id="value(input1)"]')
    elem.send_keys('PY=%s' % str(year))
    elem = driver.find_element_by_xpath('//*[@id="searchButton"]/input')
    elem.click()

    # Select the search just commenced
    elem = driver.find_element_by_xpath('//*[@id="set_1_div"]/a')
    elem.click()

    # save the number of hits
    elem = driver.find_element_by_xpath('//*[@id="hitCount.top"]')
    hits = elem.text
    # remove commas
    hits = hits.replace(',', '')
    with open('data/hits.csv', 'a') as f: f.write('%s,%s\n' % (year, hits))

    # Prompt to set the page settings
    raw_input("Please set the page settings (50 p/page, descending or ascending)")

    # Set the counter
    j = 0

    while j <= 20:
        # select all [first page]
        elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[19]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
        elem.click()
        # navigate to next page
        # automatically adds selected to marked list
        elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a')
        elem.click()

        # Set the counter
        i = 1

        while(not (i % 20 == 0)): # change 10 --> 100
            # select all
            elem = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[19]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[1]/input')
            elem.click()
            # navigate to next page
            # automatically adds selected to marked list
            elem = driver.find_element_by_xpath('//*[@id="summary_navigation"]/table/tbody/tr/td[3]/a')
            elem.click()
            i += 1

        # move to marked list
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

        lb = 1
        ub = 500
        z = 1

        while z <= 2: # change 1 --> 10
            elem = driver.find_element_by_xpath('//*[@id="markFrom"]')
            elem.send_keys(Keys.CONTROL + 'a')
            elem.send_keys(lb)
            elem = driver.find_element_by_xpath('//*[@id="markTo"]')
            elem.send_keys(Keys.CONTROL + 'a')
            elem.send_keys(ub)

            raw_input("Please save the marked list to disk")

            lb += 500
            ub += 500
            z += 1

        # clear marked list
        elem = driver.find_element_by_xpath('//*[@id="output_form"]/div[3]/span/input[2]').click()
        alert = driver.switch_to_alert()
        alert.accept()

        # go back to search results
        elem = driver.find_element_by_xpath('//*[@id="skip-to-navigation"]/ul[1]/li[2]')
        elem.click()

        j += 1

    # close the window before moving on to the next year
    driver.close()

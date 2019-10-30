# https://github.com/csaftoiu/yahoo-groups-backup/issues/41 


import os

from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference("devtools.jsonview.enabled",False)

browser = webdriver.Firefox(firefox_profile=fp)



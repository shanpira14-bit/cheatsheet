#Library
from selenium import webdriver
import time

#Using webdriver with the help of Chrome driver
PATH = "/Users/shanpira/chromedriver"
web = webdriver.Chrome(PATH)
web.get ("https://insight.myprimehr.net") 

time.sleep(1)

#Variables
userName = "${Username}"
passWord = "${Password}"

#Type userName on Textbox using XPATH
user = web.find_element_by_xpath('//*[@id="LoginMain_UserName"]')
user.send_keys(userName)

#Type passWord on Textbox using XPATH
passwd = web.find_element_by_xpath('//*[@id="LoginMain_Password"]')
passwd.send_keys(passWord)

#Click button using XPATH
SignIn = web.find_element_by_xpath('//*[@id="LoginMain_LoginButton_OneClickBtn"]')
SignIn.click()

time.sleep (2)

TimeAttendanceRecord = web.find_element_by_xpath('//*[@id="WebPartMgrMaster_gwpstart1_start1_DESC_rpt_LINK_hl_1"]')
TimeAttendanceRecord.click()

time.sleep (2)

TimeRecorder = web.find_element_by_xpath('//*[@id="MainZone"]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div[6]/a[2]')
TimeRecorder.click()

time.sleep (2)

AttendanceTimeOut = web.find_element_by_xpath('//*[@id="WebPartMgrMaster_gwpTimelogRecorder1_TimelogRecorder1_logout_Btn"]')
AttendanceTimeOut.click()
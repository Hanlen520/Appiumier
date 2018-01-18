# coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait

def click_by_id(driver,ele_id):
	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(ele_id))
	el = driver.find_element_by_id(ele_id)
	el.click()
	return driver

def input_by_id(driver,ele_id,content):
	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(ele_id))
	el = driver.find_element_by_id(ele_id)
	el.click()
	el.send_keys(content)
	return driver

def click_by_xpath(driver,ele_xpath):
	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ele_xpath))
	el = driver.find_element_by_xpath(ele_xpath)
	el.click()
	return driver

def get_text_by_id(driver,ele_id):
	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(ele_id))
	text = driver.find_element_by_id(ele_id).get_attribute("text")
	return driver,text

def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swipe_up(driver,time):
	l = getSize(driver)
	x1 = int(l[0] * 0.5)
	y1 = int(l[1] * 0.75)
	y2 = int(l[1] * 0.25)
	driver.swipe(x1, y1, x1, y2,time)
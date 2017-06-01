from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unicodecsv as csv
from selenium.common.exceptions import StaleElementReferenceException
import datetime 
import time
import xlsxwriter
import sys

url = sys.argv[1]
print (url)
browser = webdriver.Chrome()

browser.get(url)
checkindate = datetime.datetime.now()
checkoutdate = datetime.datetime.now()+datetime.timedelta(days=1)
checkindate = checkindate + datetime.timedelta(days=14)
checkoutdate = checkoutdate + datetime.timedelta(days=14)
for i in range(30):
	hotel_data = []
	checkindate = checkindate + datetime.timedelta(days=1)
	checkoutdate = checkoutdate + datetime.timedelta(days=1)
	checkin = str(checkindate.year)+"-"+str(int(checkindate.month)-1)+"-"+str(checkindate.day)
	checkout = str(checkoutdate.year)+"-"+str(int(checkoutdate.month)-1)+"-"+str(checkoutdate.day)
	indate = str(checkindate.year)+"-"+str(checkindate.month)+"-"+str(checkindate.day)
	outdate = str(checkoutdate.year)+"-"+str(checkoutdate.month)+"-"+str(checkoutdate.day)

	WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//span[@data-datetype='CHECKIN']/span[@class='picker-inner']/span[@class='picker-label']"))).click()
	WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='dsdc-month']/span[@data-date='"+checkin+"']"))).click()
	WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='dsdc-month']/span[@data-date='"+checkout+"']"))).click()   
	time.sleep(2)
	if len(browser.window_handles)>1:
		browser.switch_to_window(browser.window_handles[1])	
		browser.close()
		browser.switch_to_window(browser.window_handles[0])

	
	mainPrice = browser.find_elements_by_xpath("//*[@id='taplc_hr_north_star_v1_meta_0']/div[2]/div/div/div")
	for main in mainPrice:
		attempts=0
		while attempts<2:
			try:
				price = main.get_attribute("data-pernight")
				vendor = main.get_attribute("data-vendorname")
				break
			except StaleElementReferenceException:
				print ("waiting for DOM---")
			attempts = attempts + 1
		if str(vendor)!="None" and str(price)!="None":
			#print vendor+" : "+price 
			data = [
					vendor,
					price,
					
			]
			hotel_data.append(data)

	mainPrice1 = browser.find_elements_by_xpath("//*[@id='taplc_hr_north_star_v1_meta_0']/div[2]/div/div/div[4]/div/div")
	for main1 in mainPrice1:
		attempts=0
		while attempts<2:
			try:
				price = main1.get_attribute("data-pernight")
				vendor = main1.get_attribute("data-vendorname")
				break
			except StaleElementReferenceException:
				print ("waiting for DOM---")
			attempts = attempts + 1
		if str(vendor)!="None" and str(price)!="None":
			#print vendor," : ",price 
			data = [
					vendor,
					price,
					
			]
			hotel_data.append(data)


	subPrice = browser.find_elements_by_xpath("//*[@id='taplc_hr_meta_block_offerclick_0']/div/div/div/div/div/div/div")
	for sub in  subPrice:
		attempts=0
		while attempts<2:
			try:
				price = sub.get_attribute("data-pernight")
				vendor = sub.get_attribute("data-vendorname")
				break
			except StaleElementReferenceException:
				print ("waiting for DOM---")
			attempts = attempts + 1
		if str(vendor)!="None" and str(price)!="None":
			#print vendor," : ",price
			data = [
					vendor,
					price,
					
			]
			hotel_data.append(data)

	print (hotel_data)
	excelPath = sys.argv[2]
	workbook = xlsxwriter.Workbook('%s/%s.xlsx'%(excelPath,i))
	worksheet = workbook.add_worksheet()
	
	row = 1
	col = 0
	
	worksheet.write('A1', indate+"(CheckIn)")
	worksheet.write('B1', outdate+"(Checkout)")

	for vendor, price in hotel_data:    
		worksheet.write_string (row, col,     vendor)
		worksheet.write_string(row, col + 1, price )
		row += 1

	workbook.close()
	


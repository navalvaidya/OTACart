#!/usr/bin/env python
from datetime import datetime
from time import time
from lxml import html,etree
import requests,re
import os,sys
import unicodecsv as csv
import argparse

#sys.path.append('E:\Anaconda3\lib\site-packages')

#import pandas as pd

def parse():
    #Referrer is necessary to get the correct response from TA if not provided they will redirect to home page
    headers = {
                            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                            'Accept-Encoding': 'gzip,deflate',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'www.tripadvisor.in',
                            'Pragma': 'no-cache',
                            'Referer': sys.argv[1],
                            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
    
    #print( "Downloading search results page")
    page_response  = requests.post(url = sys.argv[1],headers=headers).text
    #print( "Parsing results ")
    #print page_response.encode('utf-8')
    parser = html.fromstring(page_response)

    hotel_lists = parser.xpath('.//div[contains(@class,"prw_rup prw_reviews_basic_review")]')
    hotel_data = []
    for hotel in hotel_lists:
        XPATH_REVIEWS = './/span[@class="noQuotes"]//text()'
        raw_reviews = hotel.xpath(XPATH_REVIEWS)
        reviews = ''.join(raw_reviews).strip() if raw_reviews else None

        data = {
                    'reviews':reviews,
        }
        hotel_data.append(data)
    #url = parser.xpath('.//div[contains(@class,"unified pagination ")]')

    #for i in url:
    #    raw_nexturl = i.xpath('.//a[@class="nav next rndBtn ui_button primary taLnk"]/@href')
    #    nexturl = 'http://www.tripadvisor.in'+raw_nexturl[0] if raw_nexturl else None    

    url = sys.argv[1]
    url = url+("#REVIEWS")
    temp = url.split("Reviews-")
    count = 5
    nexturl = temp[0]+"Reviews-or"+str(count)+"-"+temp[1]

    for i in range(10):
        headers = {
                            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                            'Accept-Encoding': 'gzip,deflate',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'www.tripadvisor.in',
                            'Pragma': 'no-cache',
                            'Referer': nexturl,
                            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
    
        #print( "Downloading search results page")
        page_response  = requests.post(url = nexturl,headers=headers).text

        parser = html.fromstring(page_response)

        hotel_lists = parser.xpath('.//div[contains(@class,"prw_rup prw_reviews_basic_review")]')
    
        for hotel in hotel_lists:
            XPATH_REVIEWS = './/span[@class="noQuotes"]//text()'
            raw_reviews = hotel.xpath(XPATH_REVIEWS)
            reviews = ''.join(raw_reviews).strip() if raw_reviews else None

            data = {
                        'reviews':reviews,
            }
            hotel_data.append(data)
        count = count+5
        nexturl = temp[0]+"Reviews-or"+str(count)+"-"+temp[1]

        #url = parser.xpath('.//div[contains(@class,"unified pagination ")]')
        #for i in url:
        #    raw_nexturl = i.xpath('.//a[@class="nav next rndBtn ui_button primary taLnk"]/@href')
        #    nexturl = 'http://www.tripadvisor.in'+raw_nexturl[0] if raw_nexturl else None       
    return hotel_data


    

if __name__ == '__main__':
    data=parse()        
  
    with open(sys.argv[2],'wb')as csvfile:
        fieldnames = ['reviews']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in  data:
            writer.writerow(row)

        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:37:00 2017

@author: Yang
"""

from selenium import webdriver
from bs4 import BeautifulSoup

def get_html(url, pjs_url, driver):
    driver.get(url) 
    driver.switch_to.frame('g_iframe') #加载 iframe 框架中的内容
    html = driver.page_source#获取加载的网页内容
    html = BeautifulSoup(html, 'lxml')
    return html

def get_top50_song(html, pjs_url, driver):
    info = html.select('div .ttc a')
    href_list = ['http://music.163.com/#/'+ item.get('href') for item in info]
    for href in href_list:
        lyric_html = get_html(href, pjs_url, driver)
        title = lyric_html.select('div .cnt .tit')[0].text.strip('\n').replace('\n',' ')
        singer = lyric_html.select('div .cnt span')[0].get('title')
        album = lyric_html.select('div .cnt p')[1].a.text 
        lyric = lyric_html.select('.bd.bd-open.f-brk.f-ib')[0].text
        data = {'title': title, 'singer': singer, 'album': album, 'lyric': lyric}
        print(data)
        

if __name__ == '__main__':
    url = 'http://music.163.com/#/artist?id=5781'    
    pjs_url = "E:/Software/phantomjs/bin/phantomjs.exe"
    driver = webdriver.PhantomJS(pjs_url) #打开PhantomJS
    html = get_html(url, pjs_url, driver)
    get_top50_song(html, pjs_url, driver)
    

    
    
    
    


# Import libraries
import os
import pandas as pd
import pymongo
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint

print(os.path.abspath("chromedriver.exe"))

def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_p = mars_news(browser)
    
    results = {
        "title": news_title,
        "paragraph": news_p,
        "image_URL": jpl(browser),
        "weather": mars_tweet(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemispheres(browser),
    }

    browser.quit()
    return results

def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    mars_soup = BeautifulSoup(html, 'html.parser')

    news_title = mars_soup.find('div', class_='content_title').text
    news_p = mars_soup.find('div', class_='article_teaser_body').text
    return news_title, news_p

def jpl(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')
    sleep(5)
    browser.click_link_by_partial_text('more info')

    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    img_url = image_soup.find('figure', class_='lede').a['href']
    img_full_url = f'https://www.jpl.nasa.gov{img_url}'
    return img_full_url

def mars_tweet(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    twit_soup = BeautifulSoup(html, 'html.parser')
    
    tweet = twit_soup.find('p', class_='TweetTextSize').text
    return tweet
    
def mars_facts():
    url = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(url)
    df.columns = ['Field', 'Value']
    df.set_index('Field', inplace=True)
    
    return df.to_html()
    
def mars_hemispheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(ast_url)
    
    ast_html = browser.html
    ast_soup = BeautifulSoup(ast_html, 'html.parser')

    hemisphere_images = []
    ast_links = ast_soup.find_all('h3')

    for x in ast_links:
        hemisphere_images.append(x.text)
    
    hemisphere_images[]

    hemisphere_image_urls = []

    hemisphere_urls = []

    for y in hemisphere_images:
        hdictionary = {}    
        browser.click_link_by_partial_text(y)
        hdictionary["img_url"] = browser.find_by_text('Sample')['href']
        hdictionary["title"] = y
        hemisphere_urls.append(hdictionary)
        pprint(hemisphere_urls)
        browser.click_link_by_partial_text('Back')
    
        return hemisphere_image_urls[]
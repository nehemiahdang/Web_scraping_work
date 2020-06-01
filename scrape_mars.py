# Import Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import os
import cssutils
import pandas as pd
import time

news_data = {}

def init_browser():
    # Function for executable path for browser; conditions set for types of os
    if os.name=="nt":
        executable_path = {'executable_path': './chromedriver.exe'}
    else:
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

def scrape_news():
    # Save the init_browser() function as a variable
    # browser = init_browser()

    news_data = {}
    
    # Request from the url and store
    news_url = 'https://mars.nasa.gov/news/'
    response = requests.get(news_url)

    # Scrape page into Soup
    news_soup = bs(response.text, 'html.parser')

    # Get latest news title
    #news_title = news_soup.title.text

    # Get latest news paragraph
    #news_p = news_soup.p.text

    # Store data to return
    news_data["title"] = news_soup.title.text
    news_data["paragraph"] = news_soup.p.text

    return news_data




# def scrape_images():
#     browser = init_browser()


# def scrape_weather():
#     browser = init_browser()


# def scrape_facts():
#     browser = init_browser()


# def scrape_hemi():
#     browser = init_browser()

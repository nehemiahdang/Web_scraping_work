# Import Dependencies
from bs4 import BeautifulSoup as bs
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
    browser = init_browser()

    news_data = {}
    
    # Request from the url and store
    news_url = 'https://mars.nasa.gov/news/'

    browser.visit(news_url)
    time.sleep(5)

    # Scrape page into Soup
    news_html = browser.html
    news_soup = bs(news_html, 'html.parser')

    # Store data to return
    news_data["title"] = news_soup.title.text
    news_data["paragraph"] = news_soup.p.text

    browser.quit()

    return news_data




def scrape_images():
    browser = init_browser()

    images_data = {}

    mars_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(mars_url)
    time.sleep(5)

    images_html = browser.html
    images_soup = bs(images_html, 'html.parser')

    art_style = images_soup.find('article')['style']
    style = cssutils.parseStyle(art_style)
    img_url = style['background-image']
    img_url = img_url.replace('url(', '').replace(')', '')
    featured_image_url = 'https://www.jpl.nasa.gov' + img_url
    featured_image_url

    images_data['image_url'] = featured_image_url

    browser.quit()

    return images_data


def scrape_weather():
    browser = init_browser()

    weather_data = {}

    twitter_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(twitter_url)
    time.sleep(5)

    twitter_html = browser.html
    twitter_soup = bs(twitter_html, 'html.parser')

    mars_tweets = twitter_soup.find_all('span')
    mars_weather = []
    for tweet in mars_tweets:
        if 'InSight sol' in tweet.text:
            mars_weather.append(tweet.text)
            #print(mars_weather)
    
    weather_data['latest_tweet'] = mars_weather[0]

    browser.quit()

    return weather_data

def scrape_facts():
    browser = init_browser()

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns = ["Description", "Value"]
    facts_df.set_index('Description', inplace=True)

    facts_data = facts_df.to_dict()['Value']

    browser.quit()

    return facts_data

def scrape_hemi():
    browser = init_browser()

    hemi_data = {}

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemi_url)
    time.sleep(5)

    hemi_html = browser.html
    hemi_soup = bs(hemi_html, 'html.parser')

    hemi_soup.find_all('img', class_='thumb')

    hemi_data['hemi_1_title'] = hemi_soup.find_all('img', class_='thumb')[0]['alt'].strip(' thumbnail')
    hemi_data['hemi_1_img_url'] = 'https://astrogeology.usgs.gov' + hemi_soup.find_all('img', class_='thumb')[0]['src']

    hemi_data['hemi_2_title'] = hemi_soup.find_all('img', class_='thumb')[1]['alt'].strip(' thumbnail')
    hemi_data['hemi_2_img_url'] = 'https://astrogeology.usgs.gov' + hemi_soup.find_all('img', class_='thumb')[1]['src']

    hemi_data['hemi_3_title'] = hemi_soup.find_all('img', class_='thumb')[2]['alt'].strip(' thumbnail')
    hemi_data['hemi_3_img_url'] = 'https://astrogeology.usgs.gov' + hemi_soup.find_all('img', class_='thumb')[2]['src']

    hemi_data['hemi_4_title'] = hemi_soup.find_all('img', class_='thumb')[3]['alt'].strip(' thumbnail')
    hemi_data['hemi_4_img_url'] = 'https://astrogeology.usgs.gov' + hemi_soup.find_all('img', class_='thumb')[3]['src']

    browser.quit()

    return hemi_data






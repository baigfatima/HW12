from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape() :
	browser = init_browser()
    mars_data = {}

#NASA Mars News
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

response = response = requests.get(url)
soup = bs(response.text, 'html.parser')


article = soup.find('div', class_='list_text')
news_title = soup.find('div', class_='content_title')
news_p = soup.find('div', class_='rollover_description_inner')

newsTitle = news_title.next
newsText = news_p.text

print(newsTitle)
print(newsText)

#JPL Mars Space Images - Featured Image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
url_base = 'https://www.jpl.nasa.gov'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

result = soup.find('article', class_='carousel_item').attrs

style_prop = str(result['style'])
trim1 = style_prop.replace("full-image","")
trim2 = trim1.replace(" urs('","")
image = trim2.replace("');","")
image_url = url_base + image
print(image_url)

#Mars Weather
url = 'https://twitter.com/marswxreport?lang=en'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

result = soup.find('div', class_="js-tweet-text-container")
print(result)

tweet_text = result.p.text
tweet_text

#Mars Facts
url = 'https://space-facts.com/mars/'
table = pd.read_html(url)
print(table)

df = table[0]
df.colums = ["Parameters", "Values"]
df.head()

html_table = df.to_html()
html_table

#Mars Hemispheres
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

url_list=[]

for y in result: 
    url_list.append(url)
    
print("URL List")
print(url_list)
print("")
print("----------")
print("'hemisphere_images_urls' List")
print("")

hemisphere_image_urls = []

for x in url_list:
    url = url_base + x
    response = requests.get(url)
    soup = bd(browser.html, 'html.parser')
    
    result1 = soup.find('img', class_="wide-image")
    image = url_base + result1["src"]
    
    result2 = soup.find('h2', class_='title')
    title = result2.text
    title = title.rsplit(' ', 1)[0]
    
    mars_hemi = {"title": title, "img_url": image}
    hemisphere_image_urls.append(mars_hemi)
    
    
print(hemisphere_image_urls)
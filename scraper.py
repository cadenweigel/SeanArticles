import requests
from datetime import datetime
import time
import os
from bs4 import BeautifulSoup

main_page = "https://dailyemerald.com/staff_name/sean-avery/"

#clear log file at the start
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Scraping Log\n")

def log(message):
    with open("log.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def get_links():

    response = requests.get(main_page)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', class_='homeheadline')

    return [link.get('href') for link in links if link.get('href')]

def scrape_article(link):

    #log(f"Starting scrape: {link}")
    start_time = time.time()

    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract headline
        headline_div = soup.find('div', class_='sno-story-headline')
        headline = headline_div.text.strip() if headline_div else ''

        # extract deck
        deck_div = soup.find('div', class_='sno-story-deck')
        deck = deck_div.text.strip() if deck_div else ''

        # extract date
        date_span = soup.find('span', id='time-wrapper')
        date = date_span.text.strip() if date_span else ''

        # extract content
        content_div = soup.find('div', class_='sno-story-body-content')
        content = []
        if content_div:
            paragraphs = content_div.find_all('p')
            content = [p.text.strip() for p in paragraphs if p.text.strip()]

        duration = time.time() - start_time
        log(f"Finished scrape: {link} | Time: {duration:.2f}s")
        return {
            'headline': headline,
            'deck': deck,
            'date': date,
            'content': content
        }

    except Exception as e:
        duration = time.time() - start_time
        log(f"Error scraping {link} after {duration:.2f}s: {e}")
        return {
            'headline': '',
            'deck': '',
            'date': '',
            'content': []
        }


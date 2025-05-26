from scraper import get_links, scrape_article
from hash import HashTable   

def main():

    links = get_links()
    data = []

    for link in links:
        page_data = scrape_article(link)
        data.append(page_data)

    

if __name__ == "__main__":
    main()
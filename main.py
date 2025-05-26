from scraper import get_links, scrape_article     

def main():

    links = get_links()
    data = []

    for link in links:
        page_data = scrape_article(link)
        data.append(page_data)

    print(data[0]["content"][0])

if __name__ == "__main__":
    main()
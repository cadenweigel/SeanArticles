import time
from scraper import get_links, scrape_article
from parser import count_word_frequencies
from hash import HashTable   

def main():

    start_time = time.time()
    links = get_links()
    data = []

    for link in links:
        page_data = scrape_article(link)
        data.append(page_data)

    total_duration = time.time() - start_time
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"\nTotal scraping time: {total_duration:.2f} seconds\n")

    word_counts = count_word_frequencies(data)
    print(word_counts)

if __name__ == "__main__":
    main()
import time
import os
from scraper import get_links, scrape_article
from parser import (
    count_word_frequencies, save_word_counts, load_word_counts,
    convert_hash_to_alphabetical_list, convert_hash_to_sorted_list)
from hash import HashTable   

def main():

    if os.path.exists("word_counts.pkl"):
        print("Loading cached word counts...")
        word_counts = load_word_counts()
    else:
        print("Scraping articles and computing word frequencies...")
        start_time = time.time()
        links = get_links()
        data = [scrape_article(link) for link in links]

        total_duration = time.time() - start_time
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"\nTotal scraping time: {total_duration:.2f} seconds\n")

        word_counts = count_word_frequencies(data)
        save_word_counts(word_counts)

    sorted_count = convert_hash_to_sorted_list(word_counts)
    print(sorted_count)
    print(len(sorted_count))


if __name__ == "__main__":
    main()
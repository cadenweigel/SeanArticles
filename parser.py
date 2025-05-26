import re
import pickle
from hash import HashTable   

def count_word_frequencies(data):
    word_counts = HashTable()

    for article in data:
        content = article.get('content', [])
        for paragraph in content:
            words = re.findall(r'\b\w+\b', paragraph.lower())  # Normalize and tokenize
            for word in words:
                if word in word_counts:
                    count = word_counts.get(word)
                    word_counts.set(word, count + 1)
                else:
                    word_counts.set(word, 1)

    return word_counts

def convert_hash_to_sorted_list(hash):
    items = []
    for bucket in hash.table:
        for key, value in bucket:
            items.append((key, value))
    return sorted(items, key=lambda x: x[1], reverse=True)

def convert_hash_to_alphabetical_list(hash):
    items = []
    for bucket in hash.table:
        for key, value in bucket:
            items.append((key, value))
    return sorted(items, key=lambda x: x[0])

def save_word_counts(word_counts, filename='word_counts.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(word_counts.table, f)

def load_word_counts(filename='word_counts.pkl'):
    with open(filename, 'rb') as f:
        table = pickle.load(f)
    
    wc = HashTable()
    wc.table = table
    return wc
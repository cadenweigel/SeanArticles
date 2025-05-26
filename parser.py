import re
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
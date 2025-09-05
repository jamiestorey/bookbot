from collections import Counter

def num_words_in_book(book_text):
    words = book_text.split()
    return len(words)

def num_chars_in_book(book_text):
    text = book_text.lower()
    char_count = Counter(text)
    print(char_count)
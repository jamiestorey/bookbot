from stats import num_words_in_book, num_chars_in_book

def get_book_text(path_to_book):
    book_contents = ""
   
    with open(path_to_book) as f:
        book_contents = f.read()

    return book_contents


def main():
   book = get_book_text("books/frankenstein.txt")
   num_words = num_words_in_book(book)
   print(f"{num_words} words found in the document")
   num_chars_in_book(book_text=book)


main()
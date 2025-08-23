from stats import get_num_words, get_char_count

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return file_contents

def main():
    # print(get_book_text("books/frankenstein.txt"))
    get_num_words(get_book_text("books/frankenstein.txt"))
    print(get_char_count(get_book_text("books/frankenstein.txt")))


main()
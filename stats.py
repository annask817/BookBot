def get_num_words(content):
    words = content.split()
    print(f"{len(words)} words found in the document")

def get_char_count(content):
    chars = {}
    content = content.lower()
    
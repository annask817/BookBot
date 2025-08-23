def get_num_words(content):
    words = content.split()
    print(f"{len(words)} words found in the document")

def get_char_count(content):
    chars = {}
    content = content.lower()
    for c in content:
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars
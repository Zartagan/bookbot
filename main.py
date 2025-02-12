def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_count = count_chars(text)
    # print(char_count)
    listed_chars = make_a_list(char_count)
    sorted_chars = sort_on(listed_chars)
    
    print(sorted_chars)
    # num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


def count_chars(text):
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def sort_on(listed_chars):
    sorted_list = sorted(listed_chars, key=lambda x: list(x.values())[0], reverse=True)
    return(sorted_list)

def make_a_list(char_count):
    characters = []
    for k, v in char_count.items():
        if k.isalpha() == True:
            dict = {k : v}
            characters.append(dict)
    return(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
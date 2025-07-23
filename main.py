import sys
from stats import count_words, count_chars, sort_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    words_count = count_words(book_text)
    chars_count = sort_chars_dict(count_chars(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char_data in chars_count:
        print(f"{char_data["char"]}: {char_data["count"]}")

main()
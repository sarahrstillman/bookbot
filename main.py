import sys
from stats import get_num_words, get_char_counts, chars_dict_to_sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()
  
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)

    num_words = get_num_words(text) 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
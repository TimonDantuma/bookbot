from stats import count_words
from stats import count_characters
from stats import report_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    result = report_count(count_characters(get_book_text(path_to_book)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(path_to_book))} total words")
    print("--------- Character Count -------")
    for element in result:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
 
    
   


main()
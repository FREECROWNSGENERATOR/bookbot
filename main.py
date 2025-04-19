import sys
from stats import count_words, count_characters, sort_chars_by_count
 
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path) as f:
        text = f.read()
 
    word_count = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_chars_by_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
            
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    

main()



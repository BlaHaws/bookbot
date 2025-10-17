import stats
import sys

book_path = ""
book_contents = ""

def main():
        if(len(sys.argv) != 2):
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_path = sys.argv[1]
            book_contents = get_book_text(book_path)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {book_path}...")
            print("----------- Word Count ----------")
            stats.num_of_words(book_contents)
            #print(stats.num_of_chars(get_book_text(book)))
            print("--------- Character Count -------")
            stats.order_list(book_contents)
            print("============= END ===============")

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except:
        pass


main()
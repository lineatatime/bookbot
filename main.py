from stats import number_of_words, character_count, dictionary_sort
import sys

def get_book_text(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        text = get_book_text(file_path)
        char_count = character_count(text)
        # print(char_count)
        sorted_chars = dictionary_sort(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count -----------")
        print(number_of_words(text))
        print("--------- Character Count -------")
        for i in sorted_chars:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
            else: continue
        print("============= END ===============")

main()
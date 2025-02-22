from stats import get_num_words
import sys

def count_letters(contents):
    character_count = {}
    lowered_contents = contents.lower()    
    for letter in lowered_contents:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1

    return(character_count)

def sort_on(dict):
    return dict["num"]

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    total_count = get_num_words(book)

    with open(book) as f:
        file_contents = f.read()

    chracter_count = count_letters(file_contents)
    sorted_count = dict(sorted(chracter_count.items(), reverse=True, key=lambda item: item[1]))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_count} total words")
    print("--------- Character Count -------")

    for letters in sorted_count:
        if letters.isalpha():
            print(f"{letters}: {chracter_count[letters]}")

    print("============= END ===============")

main()
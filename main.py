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
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_count = len(file_contents.split())

    chracter_count = count_letters(file_contents)
    sorted_count = dict(sorted(chracter_count.items(), reverse=True, key=lambda item: item[1]))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_count} words found in the document")

    for letters in sorted_count:
        if letters.isalpha():
            print(f"The '{letters}' character was found {chracter_count[letters]} times")

    print("--- End report ---")

main()
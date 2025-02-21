def count_letters(contents):
    character_count = {}
    lowered_contents = contents.lower()    
    for letter in lowered_contents:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1

    print(character_count)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(len(file_contents.split()))

    count_letters(file_contents)

    


main()
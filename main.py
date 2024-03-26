def main():
    file_location = "books/frankenstein.txt"
    print(f"--- Begin report of {file_location} ---")
    with open(file_location) as f:
        file_content = f.read()

    words = file_content.split()
    print(f"{len(words)} words found in the document")
    char_count = {}
    for word in words:
        lowered_word = word.lower()
        for letter in lowered_word:
            if letter.isalpha():
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
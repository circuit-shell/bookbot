def main():
    path_to_file = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"{word_count} words found in the document.")
        char_count = count_characters(file_contents)
        for char, count in char_count.items():

            if char.isalpha():
                print(f"The '{char}' character was foung {count} times.")
    print("--- End report ---")


def count_characters(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_count = dict(sorted(char_count.items(), key=lambda item: item[0]))
    return char_count


main()

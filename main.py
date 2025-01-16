def main():
    path_to_file = "books/frankenstein.txt"
    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Number of words: {word_count}")
        char_count = count_characters(file_contents)
        for char, count in char_count.items():
            print(f"The character '{char}' was foung {count} times.")
    print("--- End report ---")


def count_characters(text):
    # Initialize empty dictionary to store character counts
    char_count = {}

    # Convert text to lowercase
    text = text.lower()

    # Count each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


main()

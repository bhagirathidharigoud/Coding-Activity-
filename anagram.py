def is_anagram(first: str, second: str) -> bool:
    """Return whether two strings contain the same letters, ignoring case and spaces."""
    first_letters = sorted(character.casefold() for character in first if not character.isspace())
    second_letters = sorted(character.casefold() for character in second if not character.isspace())
    return first_letters == second_letters


if __name__ == "__main__":
    first_word = input("Enter the first word or phrase: ")
    second_word = input("Enter the second word or phrase: ")

    if is_anagram(first_word, second_word):
        print("The words or phrases are anagrams.")
    else:
        print("The words or phrases are not anagrams.")

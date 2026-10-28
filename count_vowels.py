def count_vowels(text: str) -> int:
    """Return the number of vowels in text, ignoring case."""
    vowels = "aeiou"
    return sum(1 for character in text if character.casefold() in vowels)


if __name__ == "__main__":
    user_text = input("Enter a string: ")
    print("Number of vowels:", count_vowels(user_text))

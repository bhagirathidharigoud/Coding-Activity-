def reverse_string(text):
    """Return text with its characters in reverse order."""
    reversed_text = ""
    # Read the string from its last character back to its first.
    for index in range(len(text) - 1, -1, -1):
        reversed_text += text[index]
    return reversed_text


if __name__ == "__main__":
    user_text = input("Enter a string: ")
    print("Reversed string:", reverse_string(user_text))

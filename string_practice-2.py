def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)
    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    text1 = example_string
    print(min(text1))
    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    text2 = example_string
    print(max(text2))
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    word = example_string
    print(word.index("t"))
    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    string = example_string
    list_of_chars = list(string)
    print(list_of_chars)
    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    sentence = example_string
    print(sentence.count("t"))

main()

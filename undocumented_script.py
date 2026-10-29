
"""Process numbers and words and display the results."""


def process_numbers(numbers):
    """Multiply even numbers by 2 and odd numbers by 3."""
    processed_numbers = []

    for number in numbers:
        if number % 2 == 0:
            processed_numbers.append(number * 2)
        else:
            processed_numbers.append(number * 3)

    return processed_numbers


def process_strings(words):
    """Capitalize words based on their length and return one string."""
    processed_words = []

    for word in words:
        if len(word) > 5:
            processed_words.append(word.upper())
        else:
            processed_words.append(word.lower())

    return " ".join(processed_words)


def main():
    """Run the program and print the results."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(words)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()

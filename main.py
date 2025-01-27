def main():
    print(
        "Welcome to BookBot. Developed by Lucas Azevedo on 01/26/2025 as part of the Boot.dev backend course.\n"
    )

    print("Pick a book from the list to generate a report from:")
    print("a. Frankenstein\nb. Charlotte's Web")
    book_choice = input("Pick ('a' or 'b'): ")

    if book_choice not in ["a", "b"]:
        print("You should pick an option from the book list! Restarting...\n")
        main()

    print(
        "\n\n",
        f"--- BOOKBOT REPORT: {"Frankenstein" if book_choice == "a" else "Charlotte's Web"} ---",
    )

    try:
        with open(
            f"books/{"Frankenstein" if book_choice == "a" else "charlottes_web"}.txt"
        ) as f:
            content = f.read()

            words = count_words(content)
            print(f"Total words found: {words}")

            chars_dict = count_characters(content)
            print_letters_report(chars_dict)
    except Exception as e:
        print(e)

    finally:
        print("--- END OF BOOK REPORT ---")


def count_words(content):
    if not len(content):
        raise Exception("Failed to read book content or book is empty.")

    words = content.split()
    return len(words)


def count_characters(content):
    if not len(content):
        raise Exception("Failed to read book content or book is empty.")

    chars_dict = {}

    for letter in content:
        lower_letter = letter.lower()

        if lower_letter not in chars_dict:
            chars_dict[lower_letter] = 1
        else:
            chars_dict[lower_letter] += 1

    return chars_dict


def print_letters_report(chars_dict):
    if not len(chars_dict):
        raise Exception("Failed to read characters data.")

    for char in chars_dict:
        if not char.isalpha():
            continue

        print(f"The letter '{char}' was found {chars_dict[char]} times.")


main()

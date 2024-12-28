def count_words(book):
    return len(book.split())


def count_characters(book):
    char_count = {}
    for c in book:
        if c.isalpha():
            char_count[c.lower()] = char_count.get(c.lower(), 0) + 1
    return char_count

file_name = "frankenstein.txt"

with open("books/" + file_name) as f:
    book = f.read()
    word_count = count_words(book)
    char_count = count_characters(book)

    with open("reports/" + file_name, "w") as report:
        report.write(f"--- Begin report of books/{file_name} ---\n")
        report.write(f"{word_count} words found in the document\n")

        for c in sorted(char_count, key=char_count.get, reverse=True):
            report.write(f"The '{c}' character was found {char_count[c]} times\n")

        report.write("---End report---")

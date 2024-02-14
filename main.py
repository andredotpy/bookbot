def main():
    content = get_content("books/frankenstein.txt")
    num_words = count_words(content)
    letters_dict = {}
    for word in content.split():
        letters_dict.update(
            count_letters(word=word, letter_counter=letters_dict)
        )
    report(path="books/frankenstein.txt", total_words=num_words, letter_count=letters_dict)

def get_content(path: str):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text: str):
    word_list = text.split()
    return len(word_list)

def count_letters(word: str, letter_counter: dict):
    for letter in word.lower():
        if not letter.isalpha():
            continue
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter


def convert_dict_to_sorted_list(letter_count: dict):
    list_of_words = []
    for k, v in letter_count.items():
        list_of_words.append({"letter": k, "count": v})

    def sort_on(dict):
        return dict["count"]
    list_of_words.sort(reverse=True, key=sort_on)
    return list_of_words


def report(path, total_words, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document")
    for counter in convert_dict_to_sorted_list(letter_count):
        print(f"The '{counter["letter"]}' character was found {counter['count']} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()
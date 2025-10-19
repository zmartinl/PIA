import string

def count_words(word_list, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        words = text.split()

        frequencies = {}

        for word in word_list:
            frequencies[word] = words.count(word)

        sorted_frequencies = dict(sorted(frequencies.items()))

        return sorted_frequencies

if __name__ == "__main__":
    words_to_search = ["python", "data", "ai", "big", "machine"]
    path = "dictionary.txt"
    result = count_words(words_to_search, path)
    for word, frequency in result.items():
        print(f"{word}: {frequency}")

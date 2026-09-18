'''Text Analyzer
You'll practice
Returning structured data from helper functions
Write analyze(text) that returns a dictionary of statistics, where each statistic is computed by its own small helper function:
• word_count
• char_count (excluding spaces)
• sentence_count (split on . ! ?)
• avg_word_length (rounded to 1 decimal)
• most_common_word
• longest_word
'''

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    count = 0

    for char in text:
        if char != " ":
            count += 1

    return count

def sentence_count(text):
    count = 0

    for char in text:
        if char == "." or char == "!" or char == "?":
            count += 1

    return count

def get_words(text):
    words = text.split()
    clean_words = []

    for word in words:
        word = word.strip(".,!?")
        clean_words.append(word.lower())

    return clean_words

def avg_word_length(text):
    words = get_words(text)

    total = 0

    for word in words:
        total += len(word)

    average = total / len(words)

    return round(average, 1)

def most_common_word(text):
    words = get_words(text)

    most_common = words[0]
    highest_count = 0

    for word in words:
        count = words.count(word)

        if count > highest_count:
            highest_count = count
            most_common = word

    return most_common

def longest_word(text):
    words = get_words(text)

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def analyze(text):
    result = {
        "word_count": word_count(text),
        "char_count": char_count(text),
        "sentence_count": sentence_count(text),
        "avg_word_length": avg_word_length(text),
        "most_common_word": most_common_word(text),
        "longest_word": longest_word(text)
    }

    return result

text = input("Enter your text: ")
result = analyze(text)
print(result)


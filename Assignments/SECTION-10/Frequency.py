'''Word Frequency Counter
You'll practice
Counting with dictionaries, case-insensitive
Given a paragraph of text, count how often each word appears (case-insensitive, and ignore punctuation). Then report:
• Each word with its count, sorted by frequency (highest first)
• The total number of unique words
• The most common and least common word'''

text = input("Enter a paragraph: ")

text = text.lower()

punctuation = ".,!?;:'\"-()"

for symbol in punctuation:
    text = text.replace(symbol, "")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

word_counts = list(frequency.items())

for i in range(len(word_counts)):
    for j in range(i + 1, len(word_counts)):

        if word_counts[j][1] > word_counts[i][1]:
            word_counts[i], word_counts[j] = word_counts[j], word_counts[i]

print("\n--- Word Frequency ---")

for word, count in word_counts:
    print(f"{word}: {count}")

print(f"\nTotal unique words: {len(frequency)}")

most_common = word_counts[0]

least_common = word_counts[-1]

print(f"Most common word: {most_common[0]} ({most_common[1]})")
print(f"Least common word: {least_common[0]} ({least_common[1]})")
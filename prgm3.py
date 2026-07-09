def count_words(text):
    words = text.split()
    return len(words)
user_input = input("Enter a Sentence or Paragraph:")
total_words = count_words(user_input)
print(f"Total words : {total_words}")
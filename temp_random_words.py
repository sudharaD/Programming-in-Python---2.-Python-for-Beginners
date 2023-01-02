import random

# Set the number of words to generate
num_words = 1000

# Open a new text file for writing
with open('random_words.txt', 'w') as f:
    # Generate `num_words` random words
    for _ in range(num_words):
        # Choose a random length for the word (between 1 and 10 characters)
        word_length = random.randint(1, 11)
        # Generate a random word with the chosen length
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        # Write the word to the file, followed by a space
        f.write(word + ' ')

print(f'Generated {num_words} random words and wrote them to random_words.txt')

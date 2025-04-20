import re

# Regex filters
words_5_plus = re.findall(r'\b\w{6,}\b', text)
numbers = re.findall(r'\d+', text)
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)

# Splitting by alphabets only
split_alpha = re.findall(r'\b[a-zA-Z]+\b', text)
starts_with_vowel = [w for w in split_alpha if w[0].lower() in 'aeiou']

print("Words >5 chars:", words_5_plus)
print("Numbers:", numbers)
print("Capitalized:", capitalized_words)
print("Starts with vowel:", starts_with_vowel)

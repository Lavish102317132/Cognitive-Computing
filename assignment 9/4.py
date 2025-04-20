def custom_tokenizer(text):
    # Preserve contractions
    text = re.sub(r"([^\w\s'\-\.])", '', text)

    # Keep hyphenated words as one
    tokens = re.findall(r'\b\w+(?:-\w+)*\b', text)

    return tokens

text2 = "Here's an email: example@mail.com and a phone number: +91 9876543210 and a URL: https://example.com"

# Regex substitutions
text2 = re.sub(r'\S+@\S+', '<EMAIL>', text2)
text2 = re.sub(r'http[s]?://\S+', '<URL>', text2)
text2 = re.sub(r'\+?\d[\d\- ]{7,}\d', '<PHONE>', text2)

print("Cleaned text:", text2)
print("Custom tokens:", custom_tokenizer(text2))

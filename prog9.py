
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
text = input("Enter string: ")
no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct += char
print("String without punctuation:", no_punct)

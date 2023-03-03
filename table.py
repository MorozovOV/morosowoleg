punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
def get_unique_words(text):
    text = text.lower()
    for symbol in text:
        if symbol in punctuation_list:
            text = text.replace(symbol, '')
    text_splitted = text.split()
    final_list = list(set(text_splitted))
    final_list.sort()
    return final_list
print(get_unique_words)
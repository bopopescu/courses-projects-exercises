def cap_text(text):
    b = []
    for temp in text.split(' '): b.append(temp.capitalize())
    return ' '.join(b)

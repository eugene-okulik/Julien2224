text = """Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"""
words = text.split()
for word in words:
    if word.endswith(','):
        print(word[:-1] + 'ing' + ',', end=' ')
    elif word.endswith('.'):
        print(word[:-1] + 'ing' + '.', end=' ')
    else:
        word = word + 'ing'
        print(word, end=' ')
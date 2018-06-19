def swap(text, ch1, ch2):
    text = text.replace(ch2, '!',)
    text = text.replace(ch1, ch2)
    text = text.replace('!', ch1)
    return text


swap("dhanush", "s", "a")


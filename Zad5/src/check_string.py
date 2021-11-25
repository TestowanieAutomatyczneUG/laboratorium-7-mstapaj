def check_string(word):
    if isinstance(word, str):
        return True
    else:
        raise TypeError("Podane słowo nie jest stringiem")

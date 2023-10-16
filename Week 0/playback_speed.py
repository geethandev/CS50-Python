def add_period(string):
    playback_words = string.replace(" ","...")

    return playback_words

string = input()
print(add_period(string))

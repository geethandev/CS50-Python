def main(string):
    words = string.lower().replace(" ","")

    if words.startswith('hello'):
        print('$0')
    elif words.startswith('h') and not words.startswith('hello'):
        print('$20')
    else:
        print('$100')
string = input("Greeting:")
main(string)
def main(string):
    normalized_input = string.lower().replace(" ", "")

    valid_answers = ["42", "forty-two", "fortytwo"]

    if normalized_input in valid_answers:
        print("Yes")
    else:
        print("No")


string = input("What is the answer to the Great Question of Life, the Universe and Everything ")
main(string)
def face(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

user_input = input()
result = face(user_input)
print(result)

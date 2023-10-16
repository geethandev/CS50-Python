def cal(x: int, y: str, z: int):
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    return result

input_str = input("Expression:")

input_str = input_str.split()
x, y, z = int(input_str[0]), input_str[1], int(input_str[2])

result = cal(x, y, z)
formatted_result = "{:.1f}".format(result)
print(formatted_result)
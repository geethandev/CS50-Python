def main():
    while True:
        result = Fractionper()
        if result is not None:
            print(result)
            break

def Fractionper():
    try:
        x, y = input("Fraction:").split("/")
        x, y = int(x), int(y)
        if 0 <= x / y <= 0.1:
            return "E"
        elif 0.9 <= x / y <= 1:
            return "F"
        elif 0.1 < int(x)/int(y) < 0.9:
            return str(round(x / y * 100)) + "%"
    except ZeroDivisionError as e:
        print("Error:", e)
        return None
    except ValueError as e:
        print("Another error:", e)
        return None

main()







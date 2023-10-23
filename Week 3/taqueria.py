def main():
    data = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            user = input("item: ").title()
            cost = data.get(user)
            total += cost
            print(f"Total: ${total:.2f}")
        except EOFError:
            print("")
            break
        except TypeError:
            continue

if __name__ == "__main__":
    main()
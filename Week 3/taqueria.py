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
    try:
        while True:
            user = input("item: ").title()
            if user == '':
                break
            cost = data.get(user)
            if cost is not None:
                total += cost
    except KeyboardInterrupt:
        print("Loop interrupted by Ctrl + D")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
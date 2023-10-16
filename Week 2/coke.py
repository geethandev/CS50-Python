
due = 50
denominations = [5, 10, 25]

print(f"Amount Due: {due}")

while due > 0:
    try:
        amount = int(input("Insert Coin: "))

        if amount not in denominations:
            print(f"Amount Due: {due}")
        else:
            due -= amount
            if due > 0:
                print(f"Amount Due: {due}")
            elif due < 0:
                change = abs(due)
                print(f"Change Owed: {change}")
                break
            else:
                print(f"Change Owed: {due}")
                break
    except ValueError:
        print("Invalid input. Please insert a valid coin.")
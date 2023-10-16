item = input("Item:").lower().replace(" ","")

items = {

    "130":"apple",
    "110":"banana",
    "100":["pear","sweetcherries"],
    "90":["grapes","kiwifruit"],
    "80":["orange","watermelon"],
    "70":"plums",
    "60":["grapefruit","nectarine","peach"],
    "50": ["avocado","cantaloupe","honeydewmelon","pineapple","strawberries","tangerine"],
    "15":"lemon",
    "20":"lime",


}

for key, value in items.items():
        if item in value:
            print("Calories:", key)
        elif item == value:
            print("Calories:", key)
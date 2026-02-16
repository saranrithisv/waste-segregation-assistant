waste_categories = {
    "burnable": ["food", "tissue", "paper", "wood"],
    "non-burnable": ["ceramic", "glass"],
    "pet": ["plastic bottle", "pet bottle"],
    "metal": ["can", "aluminum", "tin"]
}

item = input("Type the item name: ").lower()
found = False
for category, keywords in waste_categories.items():
    for keyword in keywords:
        if keyword in item:
            print("Category of the item is: ", category)
            found = True
            break
    if found:
        break
if not found:
    print("Category not found :(")
print("Welcome to The Ice Creamery")
flavorsList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]
flavorsList[0] = "French Vanilla"
flavorsList.append("Mint Chocolate Chip")
flavorsList.sort()
numOfFlavors = len(flavorsList)
print("Number of flavors:", numOfFlavors)
for i in range(numOfFlavors):
    flavorNumber = i + 1
    flavorName = flavorsList[i]
    print("Flavor", flavorNumber, ":", flavorName)

conePrices = {"S": "$1.50", "M": "$2.50", "L": "$3.50"}
coneSizes = {"S": "smallish", "M": "more for me", "L": "lotta lickin"}

customerSize = input("Enter a cone size (S, M, L): ")
if customerSize not in conePrices:
    print("Invalid cone size entered.")

customerFlavor = input("Enter a flavor number: ")
if not customerFlavor.isdigit() or int(customerFlavor) < 1 or int(customerFlavor) > numOfFlavors:
    print("Invalid flavor number entered.")

else:
    flavorIndex = int(customerFlavor) - 1
    price = conePrices[customerSize]
    sizeDescription = coneSizes[customerSize]
    chosenFlavor = flavorsList[flavorIndex]
    print("Price:", price)
    print("Size Description:", sizeDescription)
    print("Flavor:", chosenFlavor)
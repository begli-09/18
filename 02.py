prices = {"alma" : 8,
          "uzum" : 12,
          "hurma" : 18,
          "banan" : 25,
          "nar" : 15
}

total_cost = 0

while True:
    fruit = input("Name almak isleyansiniz? ").lower()
    if fruit == 'quit':
        break
    if fruit in prices:
        kg = float(input("Naxe kg almak isleyaniz? "))
        total_cost += prices[fruit] * kg
    else:
        print("Gornusi tapylmady. basga magazina git")

print(f"Siz {total_cost} manat bermeli.")
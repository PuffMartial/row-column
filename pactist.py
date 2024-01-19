rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("enter the symbol that you use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
        print()
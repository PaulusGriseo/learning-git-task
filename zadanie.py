my_shopping = {
    'warzywniak': ['kapusta', 'marchew', 'buraki', 'czosnek' ],
    'piekarnia': ['chleb', 'bułka', 'bułka', 'bagietka'],
    'obowniczy': ['sandały'],
    'instalacyjny': ['rurka', 'kran', 'zawór']
    }
counting_products = []

print("""
Wybrałem się na zakupy
i nabyłem natępujące rzeczy
w nastepujacych sklepach:
""")

for shop in my_shopping:
    print(f"{shop.capitalize()}:")
    for things in my_shopping[shop]:
        print(f"  -{things.capitalize()}")
        counting_products.append(things)
    print()

count = len(counting_products)
print(f"W sumie kupiłem {count} produktów... \n")

print("""
Uwaga!!! tu wyświetlają się liczby
podzielne przez 5
z zakresu od 0 do 100:
""")
divide_numbers = []

for n in range (0,101):
    if n > 0 and n % 5 == 0:
        divide_numbers.append(n)
print(divide_numbers)
print()
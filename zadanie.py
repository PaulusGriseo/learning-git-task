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
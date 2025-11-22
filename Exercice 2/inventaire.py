from article import Article

a1 = Article("A01", "Laptop Lenovo", 4500, 10)
a2 = Article("A02", "Macbook Pro", 25000, 5)
a3 = Article("A03", "PC Gamer", 8000, 12)

articles = (a1, a2, a3)

for a in articles:
    print(a)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} MAD")

from carnet import Carnet
from contact import Contact

c = Carnet()
c.ajouter(Contact("Chnitfa", "0611111111", "chnitfa@example.com"))
c.ajouter(Contact("Marwane", "0622222222", "marwane@example.com"))
c.ajouter(Contact("Flan", "0633333333", "flan@example.com"))

resultat = c.recherche("fl")
for contact in resultat:
    print(contact.nom, contact.telephone)

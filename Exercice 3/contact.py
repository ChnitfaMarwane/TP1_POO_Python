class Contact:
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initial(self):
        return self.nom[0].upper()

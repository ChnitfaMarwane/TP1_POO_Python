from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.f = open("Exercice 5/journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        self.f.write(f"{datetime.now().isoformat()} — {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self.f.close()

    @classmethod
    def lire(cls):
        with open("Exercice 5/journal.txt", "r", encoding="utf-8") as f:
            for ligne in reversed(f.readlines()):
                print(ligne, end="")

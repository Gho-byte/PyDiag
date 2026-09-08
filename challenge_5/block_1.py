class Livre:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        print(f'"{self.title}" de {self.author} -- {'disponible' if available else 'indisponible'}')

    def emprunter(self):
        if not self.available: return False
        self.available = False
        return True

    def rendre(self):
        if self.available: return False
        self.available = True
        return True

class Adherent:
    def __init__(self, name):
        self.name = name
        self.books = []

    def emprunter(self, book):
        if not book.emprunter(): return f"you can't get {book.title} book because it's anavaible"
        self.books.append(book)
        return f"the book {book.title} is for {self.name} now"

    def rendre(self, book):
        if not book.rendre(): return f"you can't remove {book.title} book because it's available"
        try:
            self.books.remove(book)
        except ValueError:
            return f"you can't remove {book.title} book because you don't have it"
    
    def how_much_books(self):
        return len(self.books)

livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
sara = Adherent("Sara")
print(ali.emprunter(livre))
print(sara.emprunter(livre))
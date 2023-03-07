from csv import DictReader

class Book():
    def __init__(self, title, author, genre="Fiction"):
        self.title = title
        self.author = author
        self.genre = genre
    def __repr__(self):
        text = f"Book({self.title} - {self.author})"
        return text

class LibraryCatalog():
    def __init__(self):
        self.books = []
    def load_from_file(self, fpath):
        with open(fpath, 'r') as f:
            reader = DictReader(f)
            for row in reader:
                book = Book(row['title'], row['author'], row['genre'])
                self.books.append(book)

    def save_to_file(self, fpath):
        pass



def main():
    # Create LibraryCatalog object
    # Call load_from_file with the object, pass in string of your file
    # Iterate through all the books and print them out
    library_catalog = LibraryCatalog()
    library_catalog.load_from_file("database.csv")
    for book in library_catalog.books:
        print(book)


main()
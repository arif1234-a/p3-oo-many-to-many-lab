class Book:
    def __init__(self, title: str):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))
    
class Author:
    def __init__(self, name: str):
        self.name = name
        self._contracts = []

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
class Contract:
    all = []  # Store all contracts

    def __init__(self, author, book, date, royalties):
        # Validate author is an instance of Author
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")

        # Validate book is an instance of Book
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")

        # Validate date is a string
        if not isinstance(date, str):
            raise TypeError("date must be a string")

        # Validate royalties is an integer
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        # Store valid data
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
@classmethod
def contracts_by_date(cls, target_date):
    return [contract for contract in cls.all if contract.date == target_date]
"""
Solution:
Create abstract class InvoicePersistence and and add an abstract save method, 
then each persistence class will implement this "save" method.
If we got new requirements to add 2 different types of databases like MySQL and MongoDB, we can easily do that.
"""
from abc import ABC, abstractmethod
from SRP_before import Book, Invoice

class InvoicePersistence(ABC):
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    @abstractmethod
    def save(self):
        pass
 
class DatabasePersistence(InvoicePersistence):
 
    # overriding abstract method
    def save(self):
        return ("I save to database")
 
class FilePersistence(InvoicePersistence):
 
    # overriding abstract method
    def save(self):
        return ("I save to a file")



if __name__ == "__main__":
    book = Book("Book 1", "Unknown author", 1997, 30, "A99765")

    invoice = Invoice(book, 3, 0.2, 0.15)

    db_saver = DatabasePersistence(invoice)
    print(db_saver.save())

    file_saver = FilePersistence(invoice)
    print(file_saver.save())
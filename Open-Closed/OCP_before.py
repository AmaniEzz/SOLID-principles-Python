"""
The Open-Closed Principle requires that classes should be open for extension and closed to modification.
Modification means changing the code of an existing class, and extension means adding new functionality.
It is usually done with the help of interfaces and abstract classes.
"""

"""
Question: What if we want to save the invoice into a database as well?
Possible answer: simply modifying class InvoicePersistence and add a new method.
"""

from SRP_before import Book, Invoice

class InvoicePersistence():

    """
    Persistence logic could be saving to a file, database, making an API call ... etc.
    """
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def save_to_file(self):
        # complex logic
        print("I save to a file")

    def save_to_database(self):
        # complex logic
        print("I save to database")

"""
Answer: NOOOOO!! 
we are violating OCP because we ended up modifying the InvoicePersistence class
"""
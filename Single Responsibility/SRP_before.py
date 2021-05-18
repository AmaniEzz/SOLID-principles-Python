
# The Single Responsibility Principle


# This is a simple book class with some fields
class Book:
    def __init__(self, name: str, author_name: str, year: int, price: int, isbn: str):
        self.name = name
        self.author_name = author_name
        self.year = year
        self.price = price
        self.isbn = isbn

# A invoice class which violates the Single Responsibility Principle
class Invoice:
    def __init__(self, book: Book, quantity: int, discount_rate: float, tax_rate: float):
        self.book = book
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.total = self.calculate_total()

    def calculate_total(self) -> float:
        """
        The SRP states that our class should only have a single reason to change,
        and that reason should be a change in the invoice calculation for our class.
        """
        price = ((self.book.price - self.book.price * self.discount_rate) * self.quantity)
        price_with_taxes = price * (1 + self.tax_rate)
        return price_with_taxes
    
    def print_invoice(self):
        """
        The first vioaltion: 
        we should not have printing logic mixed with business logic in the same class.
        """
        return f"{self.quantity}x of {self.book.name} is {self.book.price}$\nDiscount Rate:  {self.discount_rate}\nTax Rate: {self.tax_rate}\nTotal: {self.total}"

    # this could be saving to a database, making an API call ... etc.
    def save_to_file(self):
        """
        The second vioaltion: 
        It is an extremely common mistake to mix persistence logic with business logic.
        """
        return ("saving to file...")

if __name__ == "__main__":

    book = Book("Book 1", "Unknown author", 1997, 30, "A99765")
    invoice = Invoice(book, 3, 0.2, 0.15)
    print(invoice.calculate_total())
    print(invoice.print_invoice())
    print(invoice.save_to_file())


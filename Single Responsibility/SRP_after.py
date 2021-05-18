from SRP_before import Book

################################### Solution #####################################

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

# We create 2 classes, InvoicePrinter and InvoicePersistence, and move the methods.
class InvoicePrinter():
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def print_invoice(self):
        return f"{self.invoice.quantity}x of {self.invoice.book.name} is {self.invoice.book.price}$\nDiscount Rate:  {self.invoice.discount_rate}\nTax Rate: {self.invoice.tax_rate}\nTotal: {self.invoice.total}"


class InvoicePersistence():
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    # this could be saving to a database, making an API call ... etc.
    def save_to_file(self):
        return ("saving to file...")


if __name__ == "__main__":

    book = Book("Book 1", "Unknown author", 1997, 30, "A99765")

    invoice = Invoice(book, 3, 0.2, 0.15)
    print(invoice.calculate_total())

    invoice_printer = InvoicePrinter(invoice)
    print(invoice_printer.print_invoice())

    invoice_saver = InvoicePersistence(invoice)
    print(invoice_saver.save_to_file())


from abc import ABCMeta, abstractmethod


class Book(metaclass=ABCMeta):
  """An item that can be purchased and read"""

  def __init__(self, name: str, price: float):
    """Create an instance of book given a name and price"""
    self._name = name
    self._price = price

  @abstractmethod
  def read(self):
    """Give access to read a book instance"""
    


class BookInventory(Book):
  """An object that contains all available books for purchase and reading"""
  Books = {}

  def _add_book(self, book: Book):
    """Add a book's name and price to the list of books"""

    # ordinarily, we should check if book's name is already in the dictionary
    self.Books[book._name] = book._price

  def _update_price_of_book(self, book: Book):
    """Update the price of a book in the inventory"""

    # we should actually check if the book is in the inventory before performing this operation
    self.Books.update(book._name, book._price)



class EbookReader(BookInventory):
  """A Reader can use an EbookReader to purchase books and read"""
  pass


class Reader(EbookReader):
  """A reader can buy books in an EbookReader and read purchased books"""
  pass

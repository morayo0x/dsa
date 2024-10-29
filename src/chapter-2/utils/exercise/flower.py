# class Flower

# instance fields: = name, num_petals, price

# instance methods: 
# 	set_name, set_num_petals, set_price
# 	get_name, get_num_petals, get_price

class Flower:
  """A Flower object

  With a name, number of petals, and price
  """

  def __init__(self, name: str, num_of_petals: int, price: float) -> None:
    """Create a flower instance given the name, number of petals and price"""
    self._name = name
    self._petals = num_of_petals
    self._price = price

  # getter methods
  def get_name(self) -> str:
    """Return the name of the flower instance"""
    
    return self._name

  def get_petals(self) -> int:
    """Return the number of petals of the flower instance"""
    
    return self._petals

  def get_price(self) -> float:
    """Return the price of the flower instance"""

    return self._price

  # setter methods
  def set_name(self, name: str) -> None:
    """set the name of a flower instance to a new [name]"""

    self._name = name

  def set_petals(self, petal: int) -> None:
    """set the number of petals of a flower instance to a new [petal]"""
    
    self._petals = petal

  def set_price(self, price: float) -> None:
    """set the price of a flower instance to a new [price]"""

    self._price = price 

if __name__ == "__main__":

  # create a flower instance 
  f = Flower('Rose', 1, 3)

  # test all the methods

  # name of f
  print(f.get_name())

  # number of petals of f
  print(f.get_petals())

  # price of f
  print(f.get_price(), end="\n\n")

  # set new values

  # new name for f
  f.set_name('Blue Lily')

  # new number of petals for f
  f.set_petals(2)
  
  # new price for f
  f.set_price(5.2)

  # get new values
  
  # name of f
  print(f.get_name())

  # number of petals of f
  print(f.get_petals())

  # price of f
  print(f.get_price())

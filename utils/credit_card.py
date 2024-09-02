# A Credit Card Class

class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer: str, bank: str, acnt: str, limit: float) -> None:
    """Creates a new credit card instance.
    
    The initial balance is zero.
    
    customer the name of the customer (e.g., 'John Bowman')
    
    bank the name of the bank (e.g., 'Access Bank')
    
    acnt the account identifier (e.g., '1234, 5678, 9123, 5678')
    
    limit credit limit (measured in naira)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0
    
  def get_customer(self) -> str:
    """Return name of customer"""
    return self._customer
    
  def get_bank(self) -> str:
    """Return the bank's name"""
    return self._bank
    
  def get_account(self) -> str:
    """Return the card identifying number (typically stored as string)"""
    return self._account
    
  def get_limit(self) -> float:
    """Return the credit limit"""
    return self._limit
    
  def get_balance(self) -> float:
    """Return the current balance"""
    return self._balance
    
  def charge(self, price: float) -> bool:
    """Charge given price to the card, assuming sufficient credit limit.
    Return True if charge was processed; False if charge was denied.
    """
    if price + self._balance > self._limit:		# charge would exceed limit
      return False														# cannot accept charge
    else:
      self._balance += price
      return True   
    
  def make_payment(self, amount: float) -> None:
    """Process customer payment that reduces balance"""
    self._balance -= amount 
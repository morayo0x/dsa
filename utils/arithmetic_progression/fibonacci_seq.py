from progression import Progression

class Fibonacci(Progression):
  """Iterator producing an Fibonacci sequence."""
  
  def __init__(self, start=0):
    """Create a new Fibonacci sequence."""
    super().__init__(start)
    self.previous = 0
    self._current = 1

  def _advance(self):
    """Advance to the next value by adding the previous to the current value"""
    
    prev = self._current
    self._current += self.previous
    self.previous = prev

  def __next__(self):
    """Return the current value and advance it by the previous value"""

    if self._current is None:
      raise StopIteration()
    
    else: 
      answer = self._current
      self._advance()
      return answer

if __name__ == "__main__":
  fp = Fibonacci()

  print(next(fp))
  print(next(fp))
  print(next(fp))
  print(next(fp))
  print(next(fp))

  fp._advance()
  fp.print_progression(10)
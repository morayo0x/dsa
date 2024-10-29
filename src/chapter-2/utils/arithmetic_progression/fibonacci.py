from fibonacci_seq import Fibonacci

class FibonacciProgression(Fibonacci):
  """An iterator that produces a fibonacci progression"""

  def __init__(self, start=1, second=1):
    """Create a fibonacci progression using the two starting values [first, second]"""
    super().__init__(start)
    self._current = start
    self.previous = second - start

  def _advance(self):
    
    return super()._advance()

if __name__ == "__main__":
  fp = FibonacciProgression(start=3, second=7)

  print(next(fp))
  print(next(fp))
  print(next(fp))
  print(next(fp))
  print(next(fp))

  fp._advance()
  fp.print_progression(10)
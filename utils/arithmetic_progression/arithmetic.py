from progression import Progression

class ArithmeticProgression(Progression):
  """Iterator producing an arithmetic progression."""
  
  def __init__(self, start=0, increment=1):
    """Create a new arithmetic progression."""
    super().__init__(start)
    self.d = increment
  
  def _advance(self):
    """Advance to the next value by adding the increment to the current value"""
    if self.d == 1:
      return super()._advance()
    
    else:
      self._current += self.d
      
  def __next__(self):
    """Return the current value and advance it by the increment value"""
    
    if self._current is None:
      raise StopIteration()
    
    elif self.d == 1:
      return super().__next__()
    
    else:
      answer = self._current
      self._advance()
      return answer

if __name__ == "__main__":
  ap = ArithmeticProgression(3, 3)

  print(next(ap))
  print(next(ap))
  print(next(ap))
  print(next(ap))
  print(next(ap))

  ap._advance()
  ap.print_progression(10)
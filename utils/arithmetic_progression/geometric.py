from progression import Progression

class GeometricProgression(Progression):
  """Iterator producing an geometric progression."""
  
  def __init__(self, start=1, base=2):
    """Create a new geometric progression.
    The multiplicative term (base) defaults to 2

    """
    super().__init__(start)
    self.r = base
  
  def _advance(self):
    """Advance to the next value by multiplying the base to the current value"""
    if self.r == 1:
      return super()._advance()
    
    else:
      self._current *= self.r			# a.r
      
  def __next__(self):
    """Return the current value and advance it by the base value"""
    
    if self._current is None:
      raise StopIteration()
    
    elif self.r == 1:
      return super().__next__()
    
    else:
      answer = self._current
      self._advance()
      return answer

if __name__ == "__main__":
  gp = GeometricProgression(3)

  print(next(gp))
  print(next(gp))
  print(next(gp))
  print(next(gp))
  print(next(gp))

  gp._advance()
  gp.print_progression(10)
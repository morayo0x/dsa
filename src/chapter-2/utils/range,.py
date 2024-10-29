# The range class

from typing import Any


class Range:
  """A class that mimics the built-in range class"""
  
  def __init__(self, start, stop=None, step=1) -> None:
    """Initialize a Range instance.
    
    Semantics is similar to built-in range class. 
    """ 
    if step == 0:
      raise ValueError('step cannot be zero')
    
    if stop is None:
      start, stop = 0, start 					# special case of range(n)
    
    # calculate effective length
    self._length = max(0, (stop - start + step - 1) // step)
    
    self._start = start
    self._step = step
    
  def __len__(self):
    """Return the number of entries in the range."""
    return self._length
    
  def __getitem__(self, k):
    """Return entry at index k (using standard interpretation if negatives)."""
    if k < 0:
      k += len(self)
    if not 0 <= k < self._length:
      raise IndexError('index out of range')
      
    return self._start + k * self._step
  
if __name__ == '__main__':
  r = Range(1000, step=5)
  print(list(r).__len__())
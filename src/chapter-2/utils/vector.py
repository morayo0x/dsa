from typing import Any, Sequence


class Vector:
  """Represent a vector in multidimensional space."""
  
  def __init__(self, d: Any) -> None:
    """Create d-dimensional vectors of zeros"""
    self._coords = [0] * d
    self.type = type(d)
    
  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)
  
  def __getitem__(self, j: int):
    """Return the jth coordinate of vector"""
    return self._coords[j]
  
  def __setitem__(self, j: int, val):
    """Set jth coordinate of vector to given value."""
    
    self._coords[j] = val
    
  def __add__(self, other):
    """Return the sum of two vectors."""
    
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] + other[j]
      
    return result
  
  def __eq__(self, other: Sequence) -> bool:
    """Return True if vector has the same coordinate as other"""
    return self._coords == other._coords
  
  def __ne__(self, other: Sequence) -> bool:
    return not self == other
  
  def __str__(self) -> str:
    return '<' + str(self._coords)[1:-1] + '>'
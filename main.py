from credit_class import CreditCard
from vector_class import Vector

cc = CreditCard('Mo Kolawole', 'Access Bank', '0085083650', 1000)

# cc._balance = 10000
print(cc.make_payment(1000))
print(cc.charge(100))

vc = Vector(4)

vc[1] = 23
vc[-1] = 45

print(vc[3])

u = vc + vc
print(u)
total = 0

for entry in vc:
  total += entry
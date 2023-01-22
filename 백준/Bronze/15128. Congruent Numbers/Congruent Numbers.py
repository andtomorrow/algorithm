from fractions import Fraction
import cmath


p1, q1, p2, q2 = map(int, input().split())

leg1, leg2 = Fraction(p1,q1), Fraction(p2,q2)

area = Fraction(leg1 * leg2, 2)

if Fraction(area, 1) == int(area):
	result = 1
else:
	result = 0
	
print(result)
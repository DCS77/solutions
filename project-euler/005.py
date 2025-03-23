# Smallest Multiple
# https://projecteuler.net/problem=5
# Finds the smallest number evenly divisible by all numbers from 1 to max_divisor
# Notes:
# - Brute force approach has time complexity O(N * D) for lowest common multiple N and
#   max denominator D
# - Replace with Lowest Common Multiple approach (using Greatest Common Denominator),
#   which has time complexity O(D log M) as the complexity of computing the LCM of two
#   numbers is O(log M)
# - lcm(a,b) = (a * b)/gcd(a, b) 

import math
from functools import reduce

def lcm(a: int, b: int) -> int:
  return a * b // math.gcd(a, b)

def smallest_number_evenly_divisible(max_divisor: int) -> int:
  return reduce(lcm, range(1, max_divisor + 1))

def is_divisible_by_all(value: int, max_divisor: int) -> bool:
  return all(value % d == 0 for d in range(1, max_divisor + 1))

def smallest_number_evenly_divisible_brute_force(max_divisor: int) -> int:
  value = 20

  while True:
    if is_divisible_by_all(value, max_divisor):
      return value
    value += 1

if __name__ == "__main__":
  result = smallest_number_evenly_divisible(20)
  print(result)
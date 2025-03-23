# Multiples of 3 or 5
# https://projecteuler.net/problem=1
# Finds the sum of all the multiples of 3 or 5 below 1000

from typing import List

def sum_of_multiples(limit: int, divisors: List[int]) -> int:
  return sum(i for i in range(limit) if any(i % n == 0 for n in divisors))

if __name__ == "__main__":
  result = sum_of_multiples(1000, [3, 5])
  print(result)
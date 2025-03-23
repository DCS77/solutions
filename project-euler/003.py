# Largest Prime Factor
# https://projecteuler.net/problem=3
# Finds the largest prime factor of the specified number

def largest_prime_factor(value: int) -> int:
  d = 2

  while d * d <= value:
    while value % d == 0:
      value //= d
    d += 1

  return value

if __name__ == "__main__":
  result = largest_prime_factor(600851475143)
  print(result)
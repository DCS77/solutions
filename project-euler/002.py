# Even Fibonacci Numbers
# https://projecteuler.net/problem=2
# Finds the sum of all the even valued Fibonacci values below 4 million

def sum_of_even_fibonacci(limit: int) -> int:
  a, b = 1, 2
  total = 0

  while b < limit:
    if b % 2 == 0:
      total += b
    a, b = b, a+b

  return total

if __name__ == "__main__":
  result = sum_of_even_fibonacci(4_000_000)
  print(result)
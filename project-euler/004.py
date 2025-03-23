# Largest Palindrome Product
# https://projecteuler.net/problem=4
# Finds the largest product of two 3-digit numbers which is a palindrome

def is_palindrome(value: int) -> bool:
  return str(value) == str(value)[::-1]

def largest_palindrome_product() -> int:
  largest_product = 0

  for a in range(999, 99, -1):
    for b in range(a, 99, -1):
      product = a * b

      if product <= largest_product:
        break
      
      if is_palindrome(product):
        largest_product = product
  
  return largest_product

if __name__ == "__main__":
  result = largest_palindrome_product()
  print(result)
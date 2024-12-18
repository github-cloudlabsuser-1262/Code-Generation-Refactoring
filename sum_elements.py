"""
This program prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases.
"""

MAX = 100

def calculate_sum(arr):
   return sum(arr)

def main():
   while True:
      try:
         n = int(input("Enter the number of elements (1-100): "))
         if 1 <= n <= MAX:
            break
         else:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

   arr = []
   print(f"Enter {n} integers:")

   for _ in range(n):
      while True:
         try:
            arr.append(int(input()))
            break
         except ValueError:
            print("Invalid input. Please enter a valid integer.")

   total = calculate_sum(arr)
   print("Sum of the numbers:", total)

if __name__ == "__main__":
   main()

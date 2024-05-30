
number = 3446877846445566

num_str = str(number)

sum_odds = 0

for char in num_str:

    digit = int(char)
    
    if digit % 2 != 0:
        
        sum_odds += digit

print("Sum of odd digits:", sum_odds)

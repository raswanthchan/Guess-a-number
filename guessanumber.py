def get_binary_digits(num_input):
  quotient = 0
  remainder = 0
  mynumlist = []
  while num_input != 0:
    quotient = num_input // 2
    remainder = num_input % 2 
    num_input = quotient 
    mynumlist.append(remainder)
  print(mynumlist)

get_binary_digits(50) 
#multiply the binary with the notations of 2 

# Fill the 'cards' list by applying the game logic in python.
cards = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63],
         [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63],
         [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63],
         [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63],
         [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
         [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]]

# Run the game here.
# Give a message 'Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.' to the player
print("Think of a number between 1 and 63.")
player_input = input("Type 'start' when you are ready and hit the 'Enter' key. ")
# Keep printing the message until the player enters only 'start'.
while player_input.lower() != "start":
  print("Think of a number between 1 and 63.")
  player_input = input("Type 'start' when you are ready and hit the 'Enter' key. ")
#  the 'num' variable and set its initial value equal to 0.
num = 0
# list named valid_entries.
valid_entries = ['yes', 'no']
# loop to display the numbers of each card and to take the input whether the number exists in the card displayed. 
for i in range(0,6):
  print(cards[i])
  input_yes_or_no = input("If the number exists in the given card, type 'yes', else type 'no': ")
# If the number exists in the card displayed, then the first number is added to the 'num' variable. list indexing is used to get the first number.
  if input_yes_or_no.lower() in valid_entries[0]:
    num = num + cards[i][0]
# Print the value of the 'num' variable.
print("The number you guessed is:", num)


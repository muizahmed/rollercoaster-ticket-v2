print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
  print("Hooray ,you can ride the rollercoaster!")
  age = int(input("How old are you?\n"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age > 45 and age < 55:
    print("Midlife crisis tickets are free!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  photo = input("Do you want a photo taken too? Photos are additional $3.\n")
  if photo.startswith("Y"):
    bill += 3

  print(f"Your total bill is ${bill}.")  


else:
  print("Oops ,you're too short to ride the rollercoaster!")






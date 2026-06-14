import random
import time
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

savecode = None
count = 0
hamburger = None
bullets = 0

def generate_randoms(counter):
  rand = f"{random.randint(0,counter)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters).upper()}{random.choice(letters).upper()}{random.choice(letters).upper()}"
  return rand

def load(seconds):
	for i in range(seconds):
		os.system('clear')
		print("Loading.")
		time.sleep(0.1)
		os.system('clear')
		print("Loading..")
		time.sleep(0.1)
		os.system('clear')
		print("Loading...")
		time.sleep(0.1)

os.system('clear')
mode = input("Enter mode (read/write): ").lower()

if mode == "write":
	upto = input("Enter a number to count up to (max 4 digits): ")
	maxcount = upto[0:4]
	print(" ")
	while (count < int(maxcount)):
		print ("\033[A\033[A")
		count += 1
		print(f"Count: {count}")
		time.sleep(0.001)


	food = input("Enter yes/no: ").lower()
	if food == "yes":
		hamburger = "yes"
	elif food == "no":
		hamburger == "-no"
	else: 
		print("Error: invalid answer, defaulting to yes")
		hamburger = "yes"

	load = input("Enter magazine bullet count for pistol (max 4 digits): ")
	maxbullets = load[0:4]
	print(" ")
	while (bullets < int(maxbullets)):
		print ("\033[A\033[A")
		bullets += 1
		print(f"Bullets: {bullets}")
		time.sleep(0.001)

	print("Generating save code...")
	time.sleep(0.5)
	print("Calculating stuff...")
	clen = len(str(count))
	if clen < 4 :
		if clen == 1:
			count = f"000{count}"
		elif clen == 2:
			count = f"00{count}"
		elif clen == 3:
			count = f"0{count}"
	blen = len(str(bullets))
	if blen < 4 :
		if blen == 1:
			bullets = f"000{bullets}"
		elif blen == 2:
			bullets = f"00{bullets}"
		elif blen == 3:
			bullets = f"0{bullets}"
	
	time.sleep(3)
	print("Writing variables...")
	time.sleep(2)
	print("Done!")
	time.sleep(1.5)
	savecode = f"{count}{hamburger}{bullets}{generate_randoms(random.randint(0,5000))}"
	print(f"Save code: {savecode}")

elif mode == "read":
	savecode = input("Enter save code: ")
	count = savecode[0:4].strip("0")
	hamburger = savecode[4:7]
	bullets = savecode[7:11].strip("0")
	if hamburger == "yes":
		print(f'''
Count: {count}
Hamburger: Yes
Bullets: {bullets}
	''')
	elif hamburger == "-no":
		print(f'''
Count: {count}
Hamburger: No
Bullets: {bullets}
''')
else:
	print("Invalid mode. Please restart the program.")

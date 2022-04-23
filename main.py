import requests
import colorama
import threading
import time
import random
colorama.init()
def sniper_threaded():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		random1 = random.choice(choices)
		random2 = random.choice(choices)
		random3 = random.choice(choices)
		random4 = random.choice(choices)
		random5 = random.choice(choices)
		r = requests.get(f"https://api.roblox.com/users/get-by-username?username={random1}{random2}{random3}{random4}{random5}").text
		r = str(r)
		if "User not found" in r:
			print(colorama.Fore.GREEN + f"Generated Valid Name, {random1}{random2}{random3}{random4}{random5}")
			if save == "y":
				file = open("valid_roblox_names.txt", "a")
				file.write(f"{random1}{random2}{random3}{random4}{random5}\n")
				file.close()
		else:
			print(colorama.Fore.RED + f"Generated Invalid Name, {random1}{random2}{random3}{random4}{random5}")
		time.sleep(float(delay))
print("Roblox 5 Letter Username Sniper, Made By blob#0005")
while True:
	try:
		threads = input("Enter How Many Threads, 5-10 Recomended: ")
		threads = int(threads)
		break
	except Exception:
		print("Enter A Valid Choice")
while True:
	try:
		delay = input("Enter Delay For Each Thread, 0 = None: ")
		delay = float(delay)
		delay = str(delay)
		break
	except Exception:
		print("Enter A Valid Choice")
while True:
	save = input("Wanna Save All 5 Letter Account Names In A Txt (y/n): ")
	if save == "y" or save == "n":
		break
	else:
		print("Enter A Valid Choice")
input("Press Enter To Start: ")
for _ in range(int(threads)):
	t1 = threading.Thread(target=sniper_threaded)
	t1.start()

reqerror = False
colorerror = False
anyerror = False
try:
	import os
	from os import system
	system("title " + "Roblox Username Sniper,   Made By blob#0005,   Github: github.com/blob0005")
except:
	pass
try:
	import requests
except Exception:
	reqerror = True
	anyerror = True
try:
	import colorama
except Exception:
	colorerror = True
	anyerror = True

if anyerror == True:
	while True:
		fix = input("Missing Modules, Wanna Try To Auto Fix (y/n): ")
		if fix == "y" or fix == "n":
			break
		else:
			print("Enter A Valid Choice")
	if fix == "n":
		print("Press Enter To Close The Program")
		input("")
		exit()
	if fix == "y":
		try:
			import os
			os.system("pip install requests")
			os.system("pip install colorama")
		except Exception:
			print("Error While Fixing, Add blob#0005 For Help :)")
			input("")
			exit()
		print("Hopefully The Errors Shod Be Fixed, Restart The Program")
		input("")
		exit()
import threading
import time
import random
colorama.init(autoreset=True)
def sniper_threaded5():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=5)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated Valid Name/Banned User, {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated Invalid Name, {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))
def sniper_threaded4():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=4)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated Valid Name/Banned User, {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated Invalid Name, {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))
def sniper_threaded3():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=3)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated Valid Name/Banned User, {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated Invalid Name, {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))
print("Roblox 5 Letter Username Sniper, Made By blob#0005")
while True:
	letter = input("""Pick One
1. 5 Letter
2. 4 Letter
3. 3 Letter
4. Check Usernames In usernames_to_check.txt
5. Check One Username
> """)
	if letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5":
		break
	else:
		print("Enter A Valid Choice")
if letter == "1":
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
		t1 = threading.Thread(target=sniper_threaded5)
		t1.start()

if letter == "2":
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
		save = input("Wanna Save All 4 Letter Account Names In A Txt (y/n): ")
		if save == "y" or save == "n":
			break
		else:
			print("Enter A Valid Choice")
	input("Press Enter To Start: ")
	for _ in range(int(threads)):
		t1 = threading.Thread(target=sniper_threaded4)
		t1.start()


if letter == "3":
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
		save = input("Wanna Save All 3 Letter Account Names In A Txt (y/n): ")
		if save == "y" or save == "n":
			break
		else:
			print("Enter A Valid Choice")
	input("Press Enter To Start: ")
	for _ in range(int(threads)):
		t1 = threading.Thread(target=sniper_threaded3)
		t1.start()




if letter == "4":
	print("This Will Check All Usernames In usernames_to_check.txt")
	print("INFO: If The Usernames Does Not Follow Roblox Username Rules It Will Count As Valid")
	while True:
		try:
			delay = input("Enter Delay (0 For None): ")
			delay = float(delay)
			break
		except:
			print("Enter A Valid Choice")
	while True:
		save = input("Auto Save Names (y/n): ")
		if save == "y" or save == "n":
			break
		else:
			print("Enter A Valid Choice")
	input("Press Enter To Start: ")
	try:
		file = open("usernames_to_check.txt", "r")
		lines = file.readlines()
		file.close()
	except:
		print("Could Not Find usernames_to_check.txt Please Create One And Enter Usernames In It")
	list = []
	donelist = 0
	for name in lines:
		if "\n" in name:
			list.append(name[:-1])
			donelist = int(donelist) + 1
		else:
			list.append(name)
			donelist = int(donelist) + 1
		print(f"[{str(donelist)}] Loaded Namne")
	print("Done With Loading Names, Press Enter To Start Checker")
	input("")
	donee = 0
	for user in list:
		donee = int(donee) + 1
		e = len(user)
		e = str(e)
		if int(e) >= 3 or int(e) <= 20:
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(user)}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"[{str(donee)}] Checked Username, Valid! " + str(user))
				if save == "y":
					file = open("valid_usernames_(usernames_to_check).txt", "a")
					file.write(user+"\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"[{str(donee)}] Checked Username, Invalid! " + str(user))
				if save == "y":
					file2 = open("invalid_usernames_(usernames_to_check).txt", "a")
					file2.write(user+"\n")
					file2.close()
		else:
			print(colorama.Fore.RED + f"[{str(donee)}] Checked Username, Invalid! " + str(user))
			if save == "y":
				file3 = open("invalid_usernames_(usernames_to_check).txt", "a")
				file3.write(user+"\n")
				file3.close()
		time.sleep(float(delay))
	print("Done")
	input("")
	exit()




if letter == "5":
	print("INFO: If The Usernames Does Not Follow Roblox Username Rules It Will Count As Valid")
	while True:
		username = input("Enter Username: ")
		r = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(username)}").text
		r = str(r)
		if "User not found" in r:
			print(colorama.Fore.GREEN + "Username Not Taken Or Banned!")
		else:
			print(colorama.Fore.RED + "Username Taken!")

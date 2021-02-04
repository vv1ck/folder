import os
import time
import sys as n
import time as mm

def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 40)

print("""@AhmedoPlus / @vv1ck
           __________________
          [ Files management ]
           ||||||||||||||||||
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
time.sleep(1)
slow("""
1- Search for a file or folder
2- Extract folder content
3- Create a new folder
4- Create a new file
5- Writing inside an existing file
6- Delete an existing file
7- Delete an existing folder
""")

joker = input("Enter Number >> ")

if joker == '1':
	hi = input("Enter the name of the file or folder :\n>> ")
	print(" ")
	if os.path.exists(hi):
		print('The file or folder already exists')
		input("\nPress Enter to exit")
	else:
		print('The file or folder does not exist')
		input("\nPress Enter to exit")
	
elif joker == '2':
	print("Enter the name of the folder")
	eld = input(">> ")
	filess = os.listdir(eld)
	for file in filess:
		print(file)
		input("\nPress Enter to exit")

elif joker == '3':
		hii = input('Enter a name for the folder: ')
		os.mkdir(hii)
		print('The folder was created ...')
		input("\nPress Enter to exit")

elif joker == '4':
	print("""
Don't forget to write the file format
	( txt / py / jpg /Anything ..)
			""")
	ok = input("Enter a name for the file: ")
	file = open(ok, 'w')
	print('The file was created ...')
	input("\nPress Enter to exit")
	
elif joker == '5':
	nem = input('Enter the file name : ')
	file = open(hi, 'a')
	cum = input('Enter cumment: ')
	file.write(cum)
	file.close()
	input("Press Enter to exit")
	
elif joker == '6':
	dle = input("Enter the file name : ")
	os.remove(dle)
	print('Deleted ..')
	input("\nPress Enter to exit")

elif joker == '7':
	fold = input("Enter the folder name : ")
	os.rmdir(fold)
	print('Deleted ..')
	input("\nPress Enter to exit")
	
else:
	print("\nThere is no such number")
	print("Only this>> [ 1/2/3/4/5 ]")
	input("\nPress Enter to exit")
			

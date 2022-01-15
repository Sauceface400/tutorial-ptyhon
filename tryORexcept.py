#======================================try/except===============================

try:
    number = int(input("number: "))
    print(number)
except ZeroDivisionError as error:
    print("Error")
except ValueError:
    print("Invalid string")

#=====================================Reading file's===================================

opening_files = open("Untitled-1.txt", "r")
for Files in opening_files.readlines():
    print(Files)
opening_files.close()

#====================================Write files's=====================================
opening_files = open("Untitled-14.txt", "w")
opening_files.write("\nFarhan - cantik daripada aishah")
opening_files.close()
#Alex Ferguson
#Python
#Mod 6 Lab 3
#05/09/2023

import os
from datetime import datetime

# file_path = "Lab3Files\OutputTest.txt"

# if os.path.exists(file_path):
#     os.remove(file_path)

# file = open(file_path, "a")
# file.write("Hello World\r\nAlex")
# file.write("\nAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
# file.close()

order_number  = 0
receipt_path = "Lab3Files\Receipts"

while True:
    if os.path.exists(f"{receipt_path}\Order-{order_number}.txt"):
        order_number += 1
    else:
        break

while True:
    print(f"Order {order_number}")
    item = input("Item: ")
    cost = float(input("Price: $"))
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    receipt = open(f"{receipt_path}\Order-{order_number}.txt", "w")
    receipt.write(f"Order: {order_number}\r\n")
    receipt.write(f"Item: {item}\n")
    receipt.write(f"Cost: {cost}\n")
    receipt.write(f"Purchased: {timestamp}")
    receipt.close()
    order_number += 1
    
    repeat = input("\nWould you like to enter another item y/n: ")
    if repeat != "y":
        break
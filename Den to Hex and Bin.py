def dec_to_hex(num):
    dig1 = num // 16
    if dig1 == 10:
        dig1 = 'A'
    elif dig1 == 11:
        dig1 = 'B'
    elif dig1 == 12:
        dig1 = 'C'
    elif dig1 == 13:
        dig1 = 'D'
    elif dig1 == 14:
        dig1 = 'E'
    elif dig1 == 15:
        dig1 = 'F'
    dig2 = num % 16
    if dig2 == 10:
        dig2 = 'A'
    elif dig2 == 11:
        dig2 = 'B'
    elif dig2 == 12:
        dig2 = 'C'
    elif dig2 == 13:
        dig2 = 'D'
    elif dig2 == 14:
        dig2 = 'E'
    elif dig2 == 15:
        dig2 = 'F'
    print("Hexadecimal value is", dig1,dig2)
def dec_to_bin(num):
    dig1 = 0
    dig2 = 0
    dig3 = 0
    dig4 = 0
    dig5 = 0
    dig6 = 0
    dig7 = 0
    dig8 = 0
    if num >= 128:
        dig1 = 1
        num = num - 128
    if num >= 64:
        dig2 = 1
        num = num - 64
    if num >=32:
        dig3 = 1
        num = num  - 32
    if num >= 16:
        dig4 = 1
        num = num - 16
    if num >= 8:
        dig5 = 1
        num = num - 8
    if num >= 4:
        dig6 = 1
        num = num - 4
    if num >= 2:
        dig7 = 1
        num = num - 2
    if num >= 1:
        dig8 = 1
        num = num - 1
    print("Binary value is", dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8)
#main
num = int(input("enter a number between 0 and 255: "))
choice = input("Choose to convert the number to Hex (h) or Binary (b): ")
if choice == 'h':
    dec_to_hex(num)
elif choice == 'b':
    dec_to_bin(num)
else:
    print("Invalid choice")

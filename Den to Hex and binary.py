num = int(input("enter a number "))
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
    bin1 = num // 2
    bin2 = num % 2
    print("Binary value is", bin1,bin2)
from exception import ValueTooLarge, ValueTooSmall

# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmall(f"Value {str(i_num)} was too small!")
        elif i_num > number:
            raise ValueTooLarge(f"Value {str(i_num)} was too large!")
    finally:
        print("end")

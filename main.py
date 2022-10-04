import string
#from turtle import position

letters = string.ascii_lowercase
alphabets=' '.join(letters).split()

from art import logo
print(logo)



def caesar(start_text, shift_amount, cipher_direction):
    end_text=""

    if cipher_direction == "decode":
            shift_amount*= -1

    for letter in start_text:
        if letter in alphabets:
            position= alphabets.index(letter)
        
            new_position=position + shift_amount

            while new_position > 25:
                new_position-=26

            while new_position < 0:
                new_position+=26
            
            end_text+= alphabets[new_position]
        else:
            end_text+=letter

    print(f"The {cipher_direction}d text is {end_text}")


should_continue=True

while should_continue:
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text= input("type your message:\n").lower()
    shift=int(input("type your shift number:\n"))


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result=input("Type 'Yes' if you want to go again, otherwise, type 'no'...\n").lower()

    if result == "no":
        should_continue=False
        print("Goodbye")


# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for char in plain_text:
#         position=alphabets.index(char)
#         new_position= position + shift_amount
#         if new_position > 25:
#             new_position-=26
#         new_letter=alphabets[new_position]
#         cipher_text+=new_letter
    
#     print(f"Your encoded message is {cipher_text}")



# def decrypt(cipher_text, shift_amount):
#     decrypt_text=""
#     for char in cipher_text:
#         position=alphabets.index(char)
#         new_position= position - shift_amount
#         if new_position < 0:
#             new_position+=26
#         new_letter=alphabets[new_position]
#         decrypt_text+=new_letter
    
#     print(f"Your encoded message is {decrypt_text}")




# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

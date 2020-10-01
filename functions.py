# def p_msg():
#     print("Especial msg:")
#     print("I am learning!")


# p_msg()
# p_msg()
# p_msg()

def coversation(msg):
    print("Hi!")
    print(msg)
    print("Bye")

option = int(input("Chose 1, 2 or 3 :"))

if option == 1:
    conversation("You chise option 1")
elif option == 2:
    conversation("You chose option 2")
elif option == 3:
    coversation ("You chose option 3")
else:
    print("Type a correct option")
def confirmation(username):
    print("are you sure " + username + "? \n"
          "Once you do this, there's no turning back.")


def continuedialogue():
    while True:
        continuation = input("(1) continue \n")
        if continuation == "1":
            print()
            break
        else:
            print("wrong input, try again")
            print("test")

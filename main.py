checking = 12000
savings = 609


def withdraw(c_data=checking, s_data=savings):
    try:
        cors = input("do you want to withdraw from the [S]avings or [C]hecking?")
        amount = float(input("enter the amount"))
        if cors == "c":
            if amount <= c_data:
                print(f"dispensing ${amount}")
                c_data = c_data - amount
                print(f"your new balance is ${c_data}")
            else:
                print("insufficient funds")
        if cors == "s":
            if amount <= s_data:
                print(f"dispensing ${amount}")
                s_data = s_data - amount
                print(f"your new balance is ${s_data}")
            else:
                print("insufficient funds")
    except:
        print("enter a valid number\n")


def deposit(c_data=checking, s_data=savings):
      try:
        cors = input("do you want to deposit to your [S]avings or your [C]hecking >>>: ")
        amount = float(input("enter the amount "))
        if cors == "c":
            c_data = c_data + amount
            print(f"{amount} has now entered your checking  account and your new balance is {c_data}")
        if cors == "s":
            s_data = s_data + amount
            print(f"{amount} has now entered your savings account and your new balance is {s_data}")
      except:
          print("enter a valid number\n")


def balance(c_data=checking, s_data=savings):
    cors = input("do you want to see your [S]avings or your [C]hecking balance? >>>: ")
    if cors == "c":
        print(f"Your balance is ${c_data}")
    if cors == "s":
        print(f"Your balance is ${s_data}")


def transfer(c_data=checking, s_data=savings):
    try:
        cors = input("do you want to transfer to [C]heckings or your [S]avings account? >>>:")
        amount = float(input("enter the amount >>>: "))
        if cors == "c":
            if s_data >= amount:
                c_data = c_data + amount
                s_data = s_data - amount
                print(f"your new balances are ${c_data} for Checkings and ${s_data} for Savings ")
        elif cors == "s":
            if c_data >= amount:
                s_data = s_data + amount
                c_data = c_data - amount
                print(f"your new balances are ${c_data} for Checkings and ${s_data} for Savings ")
    except Exception as E:
        print(f"enter a valid number\n{E}")


def main():
    while True:
        print("Welcome to Evil Bank")
        print("*********ATM*********")
        selection = input("[W]ithdraw   [D]eposit\n[B]alance   [T]ransfer\n>>>: ").lower()
        if selection == "w":
            withdraw()
        elif selection == "d":
            deposit()
        elif selection == "b":
            balance()
        elif selection == "t":
            transfer()
        elif selection == "q":
            break


if __name__ == '__main__':
    main()

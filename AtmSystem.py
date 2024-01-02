class Atm:
  def __init__(self):
    self.pin = ""
    self.balance = 0

    self.menu()

  def menu(self):
    user_input = input("""
                 Hello, how would you like to proceed?

                 1. Enter 1 to create pin.
                 2. Enter 2 to do deposit.
                 3. Enter 3 to withdraw.
                 4. Enter 4 to check balance.
                 5. Enter 5 to exit.
    
    """)
    if user_input =='1':
      self.create_pin()
    elif user_input =='3':
      self.withdraw()
    elif user_input == '2':
      self.deposit()
    elif user_input== '4':
      self.check_balance()
    else :
      print('bye!')


  def create_pin(self):
    self.pin = input('Enter your pin')
    print('PIN set successfully')

  def deposit(self):
    temp = input('Enter your pIN')
    if temp ==self.pin:
      amount = int(input('enter your amount'))
      self.balance= self.balance+amount
      print('Amount :-',self.balance)
      print('deposit successfull')
    else:
      print('Invalid PIN')

  def withdraw(self):
     temp = input('Enter your pIN')
     if temp ==self.pin:
       amount = int(input('enter your amount'))
       if amount < self.balance:
          self.balance = self.balance- amount
          print('Current balance' , self.balance)
          print('Operation successfull')
       else:
         print('Insufficient funds')
     else:
        print("Invalid PIN")
  def check_balance(self):
    temp = input('Enter PIN')
    if temp ==self.pin:
      print(self.balance)
    else:
      print('Invalid PIN') 

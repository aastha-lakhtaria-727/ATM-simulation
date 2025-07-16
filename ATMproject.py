# Initial balance
balance = 1000

def atm_simulation():
    global balance  # Using global to modify the balance variable declared outside of the function
    while True:
        print('\nATM Menu:')
        print('1. Check Balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Exit')

        try:
            choice = input('Enter your choice (1-4): ').strip()

            # Check balance
            if choice == '1':
                print(f'\nYour current balance is: ${balance:.2f}')

            # Deposit money
            elif choice == '2':
                try:
                    deposit_amount = float(input('Enter the amount to deposit: $'))
                    if deposit_amount > 0:
                        balance += deposit_amount
                        print(f'\n${deposit_amount:.2f} has been deposited. Your current balance is: ${balance:.2f}')
                    else:
                        print('Invalid amount. Please enter a positive number.')
                except ValueError:
                    print('Invalid input. Please enter a valid numeric amount.')

            # Withdraw money
            elif choice == '3':
                try:
                    withdraw_amount = float(input('Enter the amount to withdraw: $'))
                    if withdraw_amount <= 0:
                        print('Invalid amount. Please enter a positive number.')
                    elif withdraw_amount > balance:
                        print('Insufficient balance.')
                    else:
                        balance -= withdraw_amount
                        print(f'\n${withdraw_amount:.2f} has been withdrawn. Your current balance is: ${balance:.2f}')
                except ValueError:
                    print('Invalid input. Please enter a valid numeric amount.')

            # Exit ATM simulation
            elif choice == '4':
                print('\nThank you for using our ATM. Have a good day!')
                break      #break statement will break the loop and the code will stop running

            else:
                print('Invalid choice. Please select a valid option (1-4).')

        except Exception as e:
            print(f'An unexpected error occurred: {e}')

# Run the ATM simulation
atm_simulation()

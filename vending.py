import sys
import math
import tkinter as Tk
import tkinter

print('Welcome to the UB vending machine.')




#window=tkinter.Tk()
#window.title("Tic Tac Toe")
#window.geometry("45x300")
#window.mainloop()
#quarters_amount=int(input('Enter the number of quaters you wish to insert:'))
quarter_amount=0
dollar_amount=0
balance=0
beginning_balance=0
def enter_moeny():
    global quarters_amount
    quarters_amount=input('Enter the number of quaters you wish to insert:')
    money()


def money():
    try:
        global dollar_amount
        global balance
        global beginning_balance
        #quarters_amount=int(input('Enter the number of quaters you wish to insert:'))
        val=int(quarters_amount)
        dollar_amount+=int(quarters_amount)*0.25
        balance=dollar_amount
        beginning_balance=dollar_amount
        print('You entered',int(quarters_amount)*0.25,'dollars.')
    except ValueError:
        print('please enter a valid entry')
        enter_moeny()




#dollar_amount=int(quarters_amount)*0.25

#balance=dollar_amount



def drinks_menu():
    global balance
    print('  Water ($1)\n  Juice ($3) \n  Soda ($1.5) ')
    drinks_option=input('Enter your drink selection(x to exit) ')
    x='x'
    if  drinks_option==x:
        ## print('remaing balance',beginning_balance-balance)
        main_menu()
    elif drinks_option in ['soda','water','juice']:
        try:
            #val=int(drinks_option)


            if drinks_option=='water' and dollar_amount>=1.0 and balance>0:
                balance-=1.0
                #tempbalance=account_manager(1)
                print('you have ',balance,'left.')
                drinks_menu()
                print('Success water')
            elif drinks_option=='water' and dollar_amount<1:
                print('you dont have enough for water')
                drinks_menu()
            elif drinks_option=='juice' and dollar_amount>=3 and balance>0:
                balance-=3.0
                print('you have ',balance,'left.')
                drinks_menu()

            elif  drinks_option=='juice' and dollar_amount<3:
                print('not enough for Juice')
                drinks_menu()
            elif drinks_option=='soda' and dollar_amount>=1.5 and balance>0:
                balance-=1.5
                print('you have ',balance,'left.')

                drinks_menu()
            elif  drinks_option=='soda' and dollar_amount<1.5:
                print('not enough for soda')
                drinks_menu()

            else:
                print('Insufficient funds please enter more')
                enter_moeny()

        except ValueError:

            print('This is not an option')
            main_menu()
    else:
        print('not a valid entry')

def snack_menu():
    global balance
    global beginning_balance
    print('  Chips ($1.25)\n  Peanuts ($0.75) \n  Cookie ($1) ')

    snack_option=input('Enter your snack selection(x to exit')
    if  snack_option=='x':
        #print('remaing balance',beginning_balance-balance)
        main_menu()
    elif snack_option in ['chips','peanuts','cookie']:
        try:
            #val=int(drinks_option)


            if snack_option=='chips' and dollar_amount>=1.25 and balance>0 :
                balance-=1.0

                print('you have ',balance,'left.')
                snack_menu()

            elif snack_option=='chips' and dollar_amount<1.25 :
                print('you dont have enough for chips')
                drinks_menu()
            elif snack_option=='peanuts' and dollar_amount>=0.75 and balance>0:
                balance-=0.75
                print('you have ',balance,'left.')
                snack_menu()

            elif  snack_option=='peanuts' and dollar_amount<3:
                print('not enough for peanuts')
                snack_menu()
            elif snack_option=='cookie' and dollar_amount>=1 and balance>0:
                balance-=1
                print('you have ',balance,'left.')

                snack_menu()
            elif  snack_option=='cookie' and dollar_amount<1:
                print('not enough for cookie')
                snack_menu()

            else:
                print('Insufficient funds please enter more')
                enter_moeny()

        except ValueError:

            print('this is not a snack option')
            main_menu()
    else:
        print('not in range')


    return

def main_menu():
    global balance
    global beginning_balance
    print('Select a category: \n 1.Drinks \n 2,Snacks \n 3.Exit')
    option_selected=int(input('select an option:'))
    if option_selected==1:
        drinks_menu()
    elif option_selected==2:
        snack_menu()
    else:
        print('Inserted amount',beginning_balance,'Paid amount: ',beginning_balance-balance,'Change: ,',balance )

        sys.exit(0)

enter_moeny()

main_menu()


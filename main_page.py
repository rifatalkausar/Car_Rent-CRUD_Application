from utils import menu
from utils import menu_read
from utils import menu_create
from utils import menu_delete
from utils import menu_update
from utils import menu_rent

def main_page():
    while True:
        menu()
        option = input('Choose your option (1-6) : ')
        if option == '1':
            menu_read()
        elif option == '2': 
            menu_create()
        elif option == '3':
            menu_update()
        elif option == '4': 
            menu_delete()
        elif option == '5': 
            menu_rent()
        elif option == '6': 
            print('Thank Your for Using This Application\nHave a Great Day!')
            break
        else:
            print('Wrong Input')

main_page()
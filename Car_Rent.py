car_list = [
        ['TOY-AVA-1', 'TOYOTA'        , 'AVANZA'  , 2022, 6, 400_000,'MONDAY'],
        ['DAI-XEN-1', 'DAIHATSU'      , 'XENIA'   , 2020, 6, 300_000,'MONDAY'],
        ['TOY-RAI-1', 'TOYOTA'        , 'RAIZE'   , 2021, 5, 250_000,'WEDNESDAY'],
        ['MIT-XPA-1', 'MITSUBISHI'    , 'XPANDER' , 2019, 6, 350_000,'THURSDAY'],
        ['HON-HRV-1', 'HONDA'         , 'HRV'     , 2023, 6, 600_000,'FRIDAY'],
]

#Main Page
def menu():
    menu = '''
    ====================================
    Welcome to Purwadhika Car Rental!
    
    Menu: 
    1. Show Car List
    2. Add Car List
    3. Edit Car List
    4. Delete Car List
    5. Rent Car
    6. Exit Application
    ====================================
    ''' 
    print(menu)

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

def print_one(list):
        for car in list:
                print(f'''
Car Code                : {car[0]}
Car Brand               : {car[1]}
Car Name                : {car[2]}
Car Manufacturing Year  : {car[3]}
Car Capacity            : {car[4]}
Car Price               : {car[5]:,}
Car Availability Day    : {car[6]}
                ''')
# Read
def option_read():
    read_option = '''
    ====================================
    Welcome to Read Menu
    Choose Option: 
    1. Show Car List
    2. Show Specific Car
    3. Back to Main Page
    ====================================
    '''
    print(read_option)

def menu_read():
    while True:
        option_read()
        option = input('Please choose option (1-3): ')
        if option == '1':
            show_stock()
        elif option == '2':
            show_unique()
        elif option == '3':
            print('Back to Main Page')
            break
        else:
            print('Wrong Input\nPlease Input Again')

def show_stock():
        if len(car_list) >0:
                print('--------------------------------------------------------------------------------------------------------------------')
                print('Our Available Stock')
                print(f"No\t{'Car Code':<10}\t{'Car Brand':<10}    Car Type    Year  Capacity   Price  Day Available")
                for idx,car in enumerate(car_list):
                        print(f'{idx+1}\t{car[0]}\t{car[1]:<15} {car[2]:<10} {car[3]:<8} {car[4]}      {car[5]:,}   {car[6]}')
                print('--------------------------------------------------------------------------------------------------------------------')
        else:
            print('Data Does Not Exist')

def show_unique():
        if len(car_list) != 0:
                show_stock()
                while True:
                        car_id = input('\nPlease input Car Code: ').upper().strip()
                        found_car = []
                        for car in car_list:
                                if car_id == car[0]: 
                                        found_car.append(car)
                        if found_car:
                                print_one(found_car)
                                break  
                        else:
                                print('Car Not Found\nPlease Try Again.')
                                break
        else:
                print('Data Does Not Exist')

# Create
def option_create():
    create_option = '''\n
    ====================================
    Welcome to Add Data Section
    Choose Option: 
    1. Add Stock
    2. Back to Main Page
    ====================================
    '''
    print(create_option)

def menu_create():
    while True:
        option_create()
        option = input('Please choose option (1-2): ')
        if option == '1':
            unqiue_check()
        elif option == '2':
            break
        else:
            print('Wrong Input\nPlease Input Again')

def unqiue_check(): # To check if the new car code not duplicate
        while True:
                show_stock()
                not_unique = True
                unique_code = input('Please Create New Car Code: ').upper().strip()
                if unique_code !='' and len(unique_code) >8:
                        for car in car_list:
                                if unique_code == car[0]:
                                        not_unique = False
                                        break
                        if not not_unique:
                                print('The Unique Code is Already Exist\nPlease Input Again')
                                break
                        else:
                                add_data(unique_code)
                                break
                else:
                        print('Must Input Unique Code and at Least 9 Character\nPlease Input Again')
                        break

def add_data(unique):
        new_car = [[]]
        unique_code = unique
        while True:
                new_car_brand = input('Input the Car Brand: ').upper().strip()
                if new_car_brand !='':
                        break
                else:
                        print('Must Input Car Brand\nPlease Input Again')
        
        while True:
                new_car_name = input('\nInput the Car Name: ').upper().strip()
                if new_car_name != '':
                        break
                else:
                        print('Must Input Car Name\nPlease Input Again')
        while True: 
                new_car_year = input('\nInput the Car Manufacture Year: ')
                if new_car_year.isnumeric():
                        new_car_year = int(new_car_year)
                        if new_car_year >= 2010 and new_car_year <= 2023:
                                break
                        else:
                                print('Car Manufacture Year should be Between 2010 - 2023\nPlease Input Again')
                else:
                        print('Car Manufacture Year should be a Numeric Value\nPlease Input Again')
        while True:
                new_car_capacity = input('\nInput the Car Capacity: ')
                if new_car_capacity.isnumeric():
                        new_car_capacity = int(new_car_capacity)
                        if new_car_capacity <1:
                                print('Wrong Capacity\nShould be More Than 0')
                        else:
                                break
                else:
                        print('Car capacity should be a Positive Numeric value and Integer Number\nPlease Input Again')

        while True:
                new_car_price = input('\nInput the Rent Price / Day: ')
                if new_car_price.isnumeric():
                        new_car_price = int(new_car_price)
                        if new_car_price >= 250_000:
                                break
                        else:
                                print('Car Price Should be Bigger Than 250,000\nPlease Input Again')
                else:
                        print('Car Price Should be a Numeric Value Only and Bigger Than 0\nPlease Input Again')

        while True:
                day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
                new_car_availabilty = input('\nInput the Car Availability (Monday - Sunday): ').upper().strip()
                if new_car_availabilty.isalpha():
                        if new_car_availabilty not in day:
                                print('Wrong Input\nAvailability Day Should be Name of Day (Monday - Sunday)\nPlease Input Again')
                        else:
                                break
                else:
                        print('Wrong Input\nAvailability Day Should be Alphabet\nPlease Input Again')

        new_car[0].insert(0,new_car_availabilty)
        new_car[0].insert(0,new_car_price)
        new_car[0].insert(0,new_car_capacity)
        new_car[0].insert(0,new_car_year)
        new_car[0].insert(0,new_car_name)
        new_car[0].insert(0,new_car_brand)
        new_car[0].insert(0,unique_code)
        print_one(new_car)
        
        while True:
                question = input('\nDo You Want to Save This? (Yes/No) : ').capitalize()
                if question == 'Yes' or question == 'No':
                        if question == 'Yes':
                                print('Data Successfully Updated')
                                car_list.append(new_car[0])
                                break
                        else:
                                break
                else:
                        print('\nWrong Input\nPlease Input Yes/No\nPlease Input Again')

# UPDATE
def option_update():
    update_option = '''\n
    ====================================
    Welcome to Update Data Section
    Choose Option: 
    1. Update Data
    2. Back to Main Page
    ====================================
    '''
    print(update_option)

def menu_update():
    while True:
        option_update()
        option = input('Please choose option (1-2): ')
        if option == '1':
                update_data_is_unique()
        elif option == '2':
            break
        else:
            print('Wrong Input')

def update_data_is_unique(): #  To check if the unique code inputted is in the inventory
        tgt_idx = 0
        target_update_list = []
        while True:
                if len(car_list) != 0:
                        show_stock()
                        unique_code = input('Please Input the Unique Code to Update: ').upper().strip()
                        is_found = True
                        for idx, car in enumerate(car_list):
                                if unique_code == car[0]:
                                        is_found = False
                                        target_update_list.append(car)
                                        tgt_idx = idx
                                        break
                        if is_found:
                                print("The Data You're Looking for Does Not Exist")
                                break
                        else:
                                print_one(target_update_list)
                                while True:
                                        confirmation = input('\nDo You Want to Update Data? (Yes/No): ').capitalize().strip()
                                        if confirmation == 'No':
                                                break
                                        elif confirmation == 'Yes':
                                                menu_update_cat(tgt_idx,target_update_list)
                                                break
                                        else:
                                                print('Wrong Input\nPlease Input Again')
                        break
                else:
                        print('Data Does Not Exist')
                        break

def update_cat():
        update_cat = '''\n
        ====================================
        Choose Category to Update
        Choose Option: 
        1. Unique Code
        2. Car Brand
        3. Car Name
        4. Car Manufacture Year
        5. Car Capacity
        6. Car Price
        7. Car Availability Day
        8. Exit
        ====================================
        '''
        print(update_cat)

def menu_update_cat(tgt_idx,target_update_list):
        update_cat()
        while True:
                choose_category = input('Please Input Name of Category to Update: ').lower().strip()
                if choose_category == 'unique code':
                        new_unique(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car brand':
                        new_car_brand(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car name':
                        new_car_name(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car manufacture year':
                        new_year_car(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car capacity':
                        new_capacity(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car price':
                        new_price(tgt_idx,target_update_list)
                        break
                elif choose_category == 'car availability day':
                        new_availability(tgt_idx,target_update_list)
                        break
                elif choose_category == 'exit':
                        break
                else:
                        print('Wrong Input Category\nPlease Try Again')

def new_unique(tgt_idx,target_update_list):
        while True:
                origin_unique = car_list[tgt_idx][0]
                new_unique = input('Please Input the New Car Code: ').upper().strip()
                is_unique = True
                if new_unique != '' and len(new_unique)>8:
                        for car in car_list:
                                if new_unique == car[0]:
                                        is_unique = False
                        if not is_unique:
                                print('The Unique Code is Already Exist\nPlease Input Again')
                        else:
                                target_update_list[0][0] = new_unique
                                print_one(target_update_list)
                                confirmation = input('Do you want to save this? (Yes/No): ').capitalize().strip()
                                if confirmation == 'Yes':
                                        car_list[tgt_idx][0] = new_unique
                                        print('Data Successfully Updated!')
                                else:
                                        car_list[tgt_idx][0] = origin_unique
                                        print('Update Canceled')
                                break
                else:
                        print('Input Must be Filled and at Least 9 Character\nPlease Input Again')

def new_car_brand(tgt_idx,target_update_list):
        while True:
                origin_brand = car_list[tgt_idx][1]
                new_brand = input('Please Input the New Car Brand: ').upper().strip()
                if new_brand != '':
                        target_update_list[0][1] = new_brand
                        print_one(target_update_list)
                        confirmation = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                        if confirmation == 'Yes':
                                car_list[tgt_idx][1] = new_brand 
                                print('Data Successfully Updated!')
                                break
                        if confirmation == 'No':
                                car_list[tgt_idx][1] = origin_brand
                                print('Update Canceled')
                                break
                        else:
                                print('Wrong Input\nPlease Input Again')
                else:
                        print('Must Input New Car Brand\nPlease Input Again')

def new_car_name(tgt_idx,target_update_list):
        while True:
                origin_name = car_list[tgt_idx][2]
                new_name = input('Please Input the New Car Name: ').upper().strip()
                if new_name != '':
                        print('\nCar ID, Car Brand, Car Name, Year, Capacity, Price, Day Available\n')
                        target_update_list[0][2] = new_name
                        print_one(target_update_list)        
                        yes_no = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                        if yes_no == 'Yes':
                                car_list[tgt_idx][2] = new_name
                                print('Data Successfully Updated!')
                                break
                        elif yes_no == 'No':
                                car_list[tgt_idx][2] = origin_name
                                print('Update Canceled')
                                break
                        else:
                                print('Wrong Input\nPlease Input Again')
                else:
                        print('Must Input New Car Name\nPlease Input Again')

def new_year_car(tgt_idx,target_update_list):
        while True:
                origin_year = car_list[tgt_idx][3]
                new_year = input('\nInput the Car Manufacture Year: ')
                if new_year.isnumeric():
                        new_year = int(new_year)
                        if new_year >= 2010 and new_year <= 2023:
                                break
                        else:
                                print('Car Manufacture Year should be Between 2010 - 2023\nPlease Input Again')
                else:
                        print('Car Manufacture Year should be a Numeric Value\nPlease Input Again')
        while True:
                target_update_list[0][3] = new_year
                print_one(target_update_list)
                yes_no = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                if yes_no == 'Yes':
                        car_list[tgt_idx][3] = new_year
                        print('Data Successfully Updated!')
                        break
                elif yes_no == 'No':
                        car_list[tgt_idx][3] = origin_year
                        print('Update Canceled')
                        break
                else:
                        print('Wrong Input\nPlease Input Again')

def new_capacity(tgt_idx,target_update_list):
        while True:
                origin_capacity = car_list[tgt_idx][4]
                new_cap = input('\nInput the Car Capacity: ')
                if new_cap.isnumeric():
                        new_cap = int(new_cap)
                        if new_cap > 0 :
                                break
                        else:
                                print('Car Capacity should be More Than 0 \nPlease Input Again')
                else:
                        print('Car Capacity should be a Positive Numeric Value\nPlease Input Again')
        while True:
                target_update_list[0][4] = new_cap
                print_one(target_update_list)  
                yes_no = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                if yes_no == 'Yes':
                        car_list[tgt_idx][4] = new_cap
                        print('Data Successfully Updated!')
                        break
                elif yes_no == 'No':
                        car_list[tgt_idx][4] = origin_capacity
                        print('Update canceled')
                        break
                else:
                        print('Wrong Input\nPlease Input Again')

def new_price(tgt_idx,target_update_list):
        while True:
                origin_price = car_list[tgt_idx][5]
                new_price = input('\nInput the New Car Rent Price / Day : ')
                if new_price.isnumeric():
                        new_price = int(new_price)
                        if new_price >= 250_000 :
                                break
                        else:
                                print('Car price should be More Than 250,000 \nPlease Input Again')
                else:
                        print('Car Capacity should be a Positive Numeric Value\nPlease Input Again')
        while True:
                target_update_list[0][5] = new_price 
                print_one(target_update_list)
                yes_no = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                if yes_no == 'Yes':
                        car_list[tgt_idx][5] = new_price
                        print('Data Successfully Updated!')
                        break
                elif yes_no == 'No':
                        car_list[tgt_idx][5] = origin_price
                        break
                else:
                        print('Wrong Input\nPlease Input Again')

def new_availability(tgt_idx,target_update_list):
        while True:
                origin_avail = car_list[tgt_idx][6]
                day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
                new_avail = input('\nInput the New Car Availability Day (Monday - Sunday) : ').upper().strip()
                if new_avail.isalpha():
                        if new_avail in day:
                                break
                        else:
                                print('Wrong Input\nAvailability Day Should be Name of Day (Monday - Sunday)\nPlease Input Again')
                else:
                        print('Wrong Input\nAvailability Day Should be Alphabet\nPlease Input Again')
        while True:
                target_update_list[0][6] = new_avail
                print_one(target_update_list)
                yes_no = input('\nDo You Want to Save This? (Yes/No) : ').capitalize().strip()
                if yes_no == 'Yes':
                        car_list[tgt_idx][6] = new_avail
                        print('Data Successfully Updated!')
                        break
                elif yes_no == 'No':
                        car_list[tgt_idx][6] = origin_avail
                        print('Update Canceled')
                        break
                else:
                        print('Wrong Input\nPlease Input Again')

# DELETE
def option_delete():
    delete_option = '''\n
    ====================================
    Welcome to Delete Data Section
    Choose Option: 
    1. Delete Data
    2. Back to Main Page
    ====================================
    '''
    return print(delete_option)

def menu_delete():
    while True:
        option_delete()
        option = int(input('Please Choose Option (1-2): '))
        if option == 1:
            delete_data()
        elif option == 2:
            break
        else:
            print('Wrong Input')

def delete_data():
        while True:
                if len(car_list) == 0:
                        print('Data Does Not Exist')
                        break
                else:
                        show_stock()
                        index = None
                        is_found = True
                        deleted_list = []
                        deleted = input('Please Input Car Code to Delete : ').upper().strip()
                        for idx, list in enumerate(car_list):
                                if deleted == list[0]:
                                        index = idx
                                        is_found = False
                                        deleted_list.insert(0,list)
                                        break
                        if is_found:
                                print("The Data You're Looking for Does Not Exist")
                                break
                        else:
                                while True: 
                                        print('\nCar ID, Car Brand, Car Name, Year, Capacity, Price, Day Available\n')
                                        print_one(deleted_list)
                                        delete_question = input('\nDo You Want to Delete the Data? (Yes/No) : ').capitalize().strip()
                                        if delete_question == 'No':
                                                print('Delete is Cancelled')
                                                return False
                                        elif delete_question == 'Yes':
                                                del car_list[index]
                                                print('Data Successfully Deleted')
                                                return True
                                        else:
                                                print('Wrong Input\nPlease Input Again')

# RENT CAR 
def option_rent():
        rent_option = """
        ====================================
        Welcome to Rent Menu
        
        1. Rent Car  
        2. Back to Main Page 
        ====================================
        """
        print(rent_option)

def menu_rent():
        while True:
                option_rent()
                option = input("Plase Choose Your Option (1-2) : ")
                if option == '1':
                        choose_day()
                elif option =='2':
                        break
                else:
                        print('Wrong Input\nPlease Input Again')

def choose_day():
        while True:
                if len(car_list) != 0:
                        day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
                        day_name = input('Please Input Your Starting Day (Monday - Sunday) : ').upper().strip()
                        if day_name.isalpha():
                                if day_name in day:
                                        rent_car(day_name)
                                        break
                                else:
                                        print('Wrong Input\nInput Must be Name of Days i.e Monday\nPlease Input Again')
                                        break
                        else:
                                print('Wrong Input\nInput Must be Name of Days i.e Monday\nPlease Input Again')
                                break
                else:
                        print("Sorry We're Run Out of Stock")
                        break

def rent_car(day_name):
        available_car = []
        origin_idx = None
        for index,car in enumerate(car_list):
                if day_name == car[6]:
                        available_car.append(car)
        if len(available_car) != 0:
                choosen_car = []
                not_is_found = True
                tgt_idx = 0
                print(f'Here is Our Stock for {day_name}')
                print(f"{'Car Code':<10}\t{'Car Brand':<10}    Car Type    Year  Capacity   Price  Day Available")
                for index,car in enumerate(available_car):
                        if day_name == car[6]:
                                print(f'{car[0]}\t{car[1]:<15} {car[2]:<10} {car[3]:<8} {car[4]}      {car[5]:,}   {car[6]}')
                while True:
                        rented_code = input('Please Input the Car Code: ').upper().strip()
                        for idx, car_opt in enumerate(available_car):
                                if rented_code == car_opt[0]:
                                        not_is_found = False
                                        choosen_car.append(car_opt)
                                        tgt_idx = idx
                                        break
                        for index,origin_car in enumerate(car_list):
                                if rented_code == origin_car[0]:
                                        origin_idx = index
                                        break
                        if not_is_found:
                                print("The Data You're Looking for Does Not Exist")
                                continue
                        else:
                                # print(choosen_car)
                                print_one(choosen_car)
                                rent_proceed(tgt_idx,choosen_car,origin_idx)
                        break
        else:
                print('Data Does Not Exist')

def rent_proceed(tgt_idx,choosen_car,origin_idx):
        while True:
                cnt = input('\n\nDo You Want to Proceed? (Yes/No): ').capitalize().strip()
                if cnt.isalpha():
                        if cnt == 'Yes':
                                total_days(choosen_car,origin_idx)
                                break
                        elif cnt == 'No':
                                break
                        else:
                                print('Wrong Input\nPlease Input Again')
                else:
                        print('Input Have to be Alphabet')

def total_days(choosen_car,origin_idx):
        while True:
                num_days = input('\nPlease Input How Many Days You Want to Rent : ')
                if num_days.isnumeric():
                        num_days = int(num_days)
                        if num_days <1:
                                print('You Need to Rent At Least 1 (One) Day')
                        else:
                                break
                else:
                        print('Input Must be Numeric Value Only')
        while True:
                bill = num_days * choosen_car[0][5]
                print(f'Your Total Bill for {num_days} Days is : {bill:,}')
                money = input('Please Input Your Money: ')
                if money.isnumeric():
                        money = int(money)
                        if money < bill:
                                print(f'Your Money is {bill - money:,} Less\nPleaes Input Again')
                        elif money > bill:
                                print(f'Thank You\nYour Change Is : {money-bill:,}\nYour Car Will be Deliver in your Choosen Day')
                                del car_list[origin_idx]
                                break
                        elif money == bill :
                                print('Thank You\nYour Car Will be Deliver in your Choosen Day')
                                del car_list[origin_idx]
                                break
                else: 
                        print('Input Must be A Numeric Value')

main_page()
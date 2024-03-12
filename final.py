# introductory print statements
# ANSI codes used for colored output
print('\033[30;45mWELCOME TO CRUMBLY DELIGHTS\033[0m')
print('-' * 80)
print('\033[30;45mDELIGHTS: WHERE EVERY CRUMB TELLS A DIFFERENT STORY\033[0m')
print('-' * 80)
print('\033[30;45mThis is a basic shopping cart designed by AMNA, FATIMA, AND LAIBA\033[0m')
print('-' * 80)
print('\033[30;45mWE SELL BAKED ITEMS\033[0m')

# initializing empty variables for storage
cart_d = {}
bill_price = []

# A function to halt the program and continue when the user wants
def press_enter_to_proceed():
    print("Press enter to proceed...")
    input()

# Function to display user order history according to the username
def display_history(username):
    print(f'\033[30;45mOrder History:\033[0m')
    with open("order_history.txt", "r") as history_file:
        orders = False
        hist = history_file.read()
        count=1
        for line in hist.split('\n'):
            if line:
                history = eval(line)
                if username in history:
                    orders = True
                    print(f'order no.{count}')
                    user_order = history[username]
                    print(f'Order Date: {user_order[0]}')
                    print(f'Product: {user_order[1]}')
                    print(f'Flavor: {user_order[2]}')
                    print(f'Quantity: {user_order[3]}')
                    print(f'Total Price: Rs.{user_order[4]}')
                    print('-' * 80)
                    count+=1

        if not orders:
            print(f"\033[41;30mNo order history found for {name}.\033[0m")

# Function to create an account for a new user
def create_account():
    while True:
        username = input("Enter a username: ")
        with open('user_pass.txt', 'a+') as file:
            file.seek(0)
            F = file.read()
            username_taken = False

            for line in F.split('\n'):
                if line:
                    user = eval(line)
                    if username in user:
                        print('\nThis username is already taken. Enter another.')
                        username_taken = True
                        break

            if not username_taken:
                print('\033[41;30mNOTE: Password must be at least 7 characters long\033[0m')
                password = input('Enter your password: ')
                password1 = input('Confirm your password: ')

                if password1 != password:
                    print('\nPasswords do not match. Restarting')
                elif len(password) < 6:
                    print('\nPassword too short! Restarting')
                else:
                    print('\nYour account has been successfully created!')
                    d = {username: password}
                    file.write('\n' + str(d))
                    file.close()
                    print('\nTo display the menu', end=', ')
                    press_enter_to_proceed()
                    display_categories()
                    MENU(username)
                    break

# Function to login for an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('user_pass.txt', 'a+') as file:
        file.seek(0)
        F = file.read()
        F = F.split('\n')

    for line in range(len(F)):
        user = F[line]
        user = eval(user)

        if (username in user) and (user[username] == password):
            print('\nLogin successful!')
            while True:
                answer = input('\033[42;37mENTER [H] TO VIEW SHOPPING HISTORY OR [M] TO BROWSE MENU\033[0m:')
                if answer.capitalize() == 'H':
                    display_history(username)
                    continue
                elif answer.capitalize() == 'M':
                    display_categories()
                    MENU(username)
                    return
                else:
                    print('\nInvalid choice. Please enter either [H] or [M].')
                    continue
    else:
        print('\nLogin failed. Invalid username or password.')
        login()

# BAKERY MENU stored in the form of a dictionary
# Flavours stored in a list as values
bakery_menu = {'brownies (4 pieces box)': ['classic fudge', 'triple chocolate', 'peanut butter'],
               'cookies (10 per jar)': ['chocolate', 'peanut', 'vanilla'],
               'pastry (single)': ['chocolate', 'strawberry', 'coffee'],
               'bread (single loaf)': ['brown', 'white', 'banana special'],
               'doughnuts (4 pieces box)': ['chocolate', 'glazed', 'strawberry'],
               'cake (1/2 pound)': ['coffee', 'chocolate', 'strawberry']}

# PRICES stored as a dictionary
# PRICES{CATEGORY:PRICE}
prices = {'brownies (4 pieces box)': 400,
          'cookies (10 per jar)': 750,
          'pastry (single)': 100,
          'bread (single loaf)': 100,
          'doughnuts (4 pieces box)': 400,
          'cake (1/2 pound)': 1000}

# Function to display categories by using both dictionaries created above
def display_categories():
    print('\033[43;37m--MENU--\033[0m\n')
    # FORMATTING DONE TO DISPLAY A PRESENTABLE READABLE MENU
    print('\033[43;37m{:<30}{}\033[0m'.format('FOOD ITEM', 'PRICE'))
    index = 1
    for category in bakery_menu:
        print('{:<30}Rs. {}'.format(f'{index} - {category.capitalize()}', prices[category]))
        index += 1

# Function to display flavors for a chosen category
def display_flavors(chosen_category):
    if chosen_category.lower() in bakery_menu:
        print(f"\n\033[43;37mAvailable {chosen_category.capitalize()} Flavors:\033[0m")
        num = 1
        for flavours in bakery_menu[chosen_category.lower()]:
            print(num, ')', flavours)
            num += 1
    else:
        print("\nInvalid choice. Please choose a valid category.")

# Function to remove items from the cart
def remove_from_cart(cart_d, username):
    if username in cart_d:
        user_cart = cart_d[username]

        if not user_cart:
            print("Your cart is empty.")
            return

        print("\033[41;30mItems in your cart:\033[0m")
        for i in range(len(user_cart)):
            item = user_cart[i]
            print(f"{i + 1}. Category: {item[1]} | Flavor: {item[2]} | Quantity: {item[3]} | Total Price: {item[4]}")

        remove_index = input("\033[42;37mEnter the number corresponding to the item you want to remove (or enter 'C' to cancel)\033[0m:")

        if remove_index.isdigit():
            remove_index = int(remove_index)
            if 1 <= remove_index <= len(user_cart):
                user_cart.pop(remove_index - 1)
                bill_price.remove(item[4])
                print("Item removed from cart")
            else:
                print("Invalid item number. Please try again.")
                remove_from_cart(cart_d, username)
                return
        elif remove_index.capitalize() == 'C':
            print("\nRemoval canceled.")
        else:
            print("\nInvalid input. Please enter a valid item number or 'C' to cancel.")
            remove_from_cart(cart_d, username)
            return
    else:
        print("\nYour cart is empty.")

# Function to generate the bill and clear the cart
def generate_bill(cart_d, local_time, username):
    if username in cart_d:
        user_cart = cart_d[username]
        if not user_cart:
            print("Your cart is empty.")
            return
        # Writing order details to the order history file
        # with open("order_history.txt", "a+") as history_file:
        #     for item in user_cart:
        #         history_file.write(str(cart_d) + '\n')
        address = input('Enter your home address:')
        print('-' * 80)
        print("\n//BILL//")
        print('-' * 80)
        print('time:', local_time)
        print('customer:', name)
        print(f"Total Price: Rs {sum(bill_price)}")
        print('-' * 80)
        print('THANK YOU FOR ORDERING FROM "CRUMBLY DELIGHTS"\nYOUR ORDER WILL BE DELIVERED SOON')
        print('-' * 80)

        with open("order_history.txt", "a+") as history_file:
            for item in user_cart:
                history_file.write(str({username: item}) + '\n')

        # Clearing the cart for the user
        cart_d.pop(username)
    else:
        print('Your cart is empty')

# Function to handle the shopping cart
def cart(chosen_category, username, cart_d):
    import time
    local_time = time.ctime()
    if chosen_category.lower() in prices:
        quantity = (input(f"How many {chosen_category.capitalize()} do you want to order? "))
        flavor_index = (input("Enter the number corresponding to your desired flavor: "))
        flavors = bakery_menu[chosen_category.lower()]

        if flavor_index.isdigit() and quantity.isdigit():
            if 1 <= int(flavor_index) <= len(flavors):
                selected_flavor = flavors[int(flavor_index) - 1]
                item_price = prices[chosen_category.lower()]
                total_price = item_price * int(quantity)
                bill_price.append(total_price)
                if username not in cart_d:
                    cart_d[username] = []
                cart_item = [local_time, chosen_category, selected_flavor, quantity, total_price]
                cart_d[username].append(cart_item)
                while True:
                    ask1 = input('\033[42;37mEnter [R] if you want to remove from cart OR Enter [C] if you want to checkout OR Enter [B] if you want to browse menu\033[0m:')
                    if ask1.isalpha():
                        if ask1.capitalize() == 'R':
                            remove_from_cart(cart_d, username)
                        elif ask1.capitalize() == 'C':
                            generate_bill(cart_d, local_time, username)
                            break
                            return
                        elif ask1.capitalize() == 'B':
                            display_categories()
                            MENU(username)
                            return
                        else:
                            print('Invalid choice. TRY AGAIN')
                    else:
                        print('Invalid choice. TRY AGAIN')
            else:
                print('Invalid choice. TRY AGAIN')
                cart(chosen_category, username, cart_d)




# Function to handle the main menu
def MENU(username):
    choice = input("Enter your choice (e.g., [1] for 'brownies', [2] for 'cookies' .... etc.):")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(bakery_menu):
            chosen_category = list(bakery_menu.keys())[choice - 1]
            display_flavors(chosen_category)
            ask = input("\n\033[42;37mEnter [Y] if you want to add to cart OR Enter [M] if you want to continue browsing menu\033[0m:")
            if ask.capitalize() == 'Y':
                print(' Proceeding to place order')
                cart(chosen_category, username, cart_d)
                return
            elif ask.capitalize() == 'M':
                MENU(username)
                return
            else:
                print("Invalid choice. Please try again.")
                MENU(username)
        else:
            print("Invalid choice. Please try again.")
            MENU(username)
    else:
        print("Invalid input. Please enter a number.")
        MENU(username)

# Main program loop
while True:
    choice = input('\033[42;37m\nENTER [1] TO CREATE ACCOUNT OR [2] TO LOGIN INTO EXISTING ACCOUNT\033[0m:')

    if choice.isdigit() and (choice == '1' or choice == '2'):
        if choice == '1':
            name = input('Enter your name:')
            create_account()
        elif choice == '2':
            name = input('Enter your name:')
            login()
        break
    else:
        print('\nInvalid choice. Please enter either [1] or [2]. RESTARTING...')

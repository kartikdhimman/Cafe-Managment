# Items that are in menu
food={'momos': [70], 'pizza': [200], 'burger': [70], 'maggi': [30]}
# Empty Dictionary to add items
bill={}
# Initalising the loop
wellcome=input('Enter "Yes" if you want to order\nEnter "Exit" if you want to exit the menu. ').lower()
# Command to enter the loop
if wellcome == 'yes':
    while wellcome != 'exit':
        # Asking the customers name
        name= input('Please enter your Name ')
        # Enter the loop if name alredy pesent in dictionary
        if name in bill :
            # Printing the name of food items
            for i,j in food.items():    
                print(i,j)
            print('Select one of the above')
            # Asking the customer to sellect one food item
            order=input('Enter name of food item to add it to your order. ').lower()
            # Checking if the customer input exists in our menu
            if order in food:
            # Appending food item to customers existing records in dictionary
                bill[name]['Item ordered'].append(order)
                bill[name]['Total bill'].append(food[order][0])
            # If food do not exist the re-start the loop
            elif order not in food:
                print('Enter a valid input')  
            wellcome=input('Enter "Yes" if you want to order\nEnter "Exit" if you want to exit the menu. ').lower()
        # Entering another conditin if name is not alredy present in dictionary
        else:
            #Printing the name of food items
            for i,j in food.items():
                print(i,j)
            print('Select one of the above')
            # Asking the customer to sellect one food item
            order=input('Enter name of food item to add it to your order. ').lower()
            # Checking if food item present in menu
            if order in food:
                # Adding new entery in dictionary if food item present in menu
                bill[name]= {'Item ordered': [order], 'Total bill': [food[order][0]]}
            # If food do not exist the re-start the loop
            elif order not in food:
                print('Enter a valid input')
            wellcome=input('Enter "Yes" if you want to order\nEnter "Exit" if you want to exit the menu. ').lower()
# If customer enters a worng commend at start of loop re-start the loop
else:
    print('Enter a valid input')
    wellcoem= input('Enter "Yes" if you want to order\nEnter "Exit" if you want to exit the menu. ').lower()
                
print('Thanks for visiting')

# Asking for the customer name whose data is to be displayed
bill_name=input('Enter the name to display details ')
# displying the data of the user whose name was entered
print(f'Details of {bill_name} are {bill[bill_name]}')
print(f'Items orderd by {bill_name} are {bill[bill_name]['Item ordered'][:]}')
print(f'Total bill is {sum(bill[bill_name]['Total bill'][:])}')

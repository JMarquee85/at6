# The first extremely terrible and limited text-based version of the future AT-6 app
# Remember to look into TKinter when you want to start building a GUI.  A Django webapp
# would probably also do the trick.

# from Tkinter import *
# from kivy import *
	

##### CAR SERVICES #####

car_services = {
    'Name': '', 'Phone Number': '', 'Address': '' +
    ''
}



##### MAKE RESERVATION FUNCTION #####

def make_reservation(name, time, guests, number):
	new_reservation = {'name': name, 'time': time, 'guests': guests, 'number': number}
	return new_reservation
	

##### RESERVATIONS LIST OR DICTIONARY/ IES #####
# Alright, how about a dictionary with four keys?
# Or, separate lists for each category that are put back together in the dictionary?


reservation_names = []
reservation_times = []
reservation_guests = [] 
reservation_numbers = []

reservations = {'names': [], 'times': [], 'guests': [], 'numbers': []}



##### RESTAURANT OPEN FLAG ####
restaurant_open = True

# The lists need to be referenced globally in the below function in
# order to be changed in the program.
AT6d = []
dishes = ['Oyster Steak', '12oz. Ribeye', '16oz. Ribeye', 'Skirt Steak',
                  'Hanger Steak', 'Chilean Sea Bass', 'Salmon', 'Lamb Chops',
                  'Lamb Burger', 'Lamb Cigars', 'Rib Brochette', 'Apple Tart',
                  'French Crepe', 'Beef Tartare']
almost_out = []

# Dictionaries and/ or lists to contain the specials
# specials = [special_soup, special_1, special_2, special_3, special_4, special_app]

special_soup = []
specials = []
special_app = []


##### MAIN LOOP #####
def selections():
    while restaurant_open:
        # Global variable calls, so the lists will be changed.
        global AT6d
        global almost_out
        global dishes
        global special_soup
        global specials
        global special_app
        global reservations
        global reservation_guests
        global reservation_names
        global reservation_numbers
        global reservation_times
        global names
        global times
        global guests
        global numbers
        # Status Checks at the top of each loop.
        print("""
             .----------------.  .----------------.  .----------------.  .----------------.
            | .--------------. || .--------------. || .--------------. || .--------------. |
            | |      __      | || |  _________   | || |              | || |    ______    | |
            | |     /  \     | || | |  _   _  |  | || |              | || |  .' ____ \   | |
            | |    / /\ \    | || | |_/ | | \_|  | || |    ______    | || |  | |____\_|  | |
            | |   / ____ \   | || |     | |      | || |   |______|   | || |  | '____`'.  | |
            | | _/ /    \ \_ | || |    _| |_     | || |              | || |  | (____) |  | |
            | ||____|  |____|| || |   |_____|    | || |              | || |  '.______.'  | |
            | |              | || |              | || |              | || |              | |
            | '--------------' || '--------------' || '--------------' || '--------------' |
            '----------------'  '----------------'  '----------------'  '----------------'
                        """)
        print("\n---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---")

        print("\nCURRENTLY AT6'd:")
        if not AT6d:
            print("\tNothing!")
        else:
            for at6d_dishes in AT6d:
                print("\t- " + at6d_dishes.title())
        print("\nTODAY'S SPECIALS:")
        print("\nSoup of the day: ")
        if not special_soup:
            print("\tNo special soup found...")
        else:
            print("\t " + str(special_soup))
        print("\nSpecials:")
        if not specials:
            print("\tNo Specials Today!")
            print("\tPlease select option 4 to change the specials!")
        else:
            for specials in specials:
                print("\t- " + specials.title())
        print("\nRUNNING OUT:")
        if not almost_out:
            print("\tNot low on anything at the moment...")
        else:
            for running_out in almost_out:
                print("\t- " + running_out.title())
        # User choice Section.
        print("\n\n---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---AT6---")
        print(""" _____     _                 _____     _         _   _         _
|     |___| |_ ___    ___   |   __|___| |___ ___| |_|_|___ ___|_|
| | | | .'| '_| -_|  | .'|  |__   | -_| | -_|  _|  _| | . |   |_
|_|_|_|__,|_,_|___|  |__,|  |_____|___|_|___|___|_| |_|___|_|_|_|

                                                                               """)


        user_choice = int(input('What would you like to do?' +
                                '\n\t - 1. AT-6 an Item' +
                                '\n\t - 2. Un-AT6 an Item' +
                                '\n\t - 3. Clear the AT6 List' +
                                '\n\t - 4. Enter the Specials' +
                                '\n\t - 5. Add a Reservation' +
                                '\n\t - 6. View Tonight\'s Reservations' +
                                '\n\t - 7. Show a list of local Car Services' +
                                '\n\t - 8. Open the vegetable glossary'
                                '\n\t - 9. Exit '
                                ))
        if user_choice == 1:
            print("\n")
            print("ALL DISHES: ")
            for all_dishes in dishes:
                print("- " + all_dishes.title())
            print("\n")
            print("CURRENTLY AT6'd:")
            for at6d_dishes in AT6d:
                print("- " + at6d_dishes.title())
            user_input1 = input("\nWhat would you like to AT6? (Input an item from the list or Press Enter to exit)")
            if user_input1 in dishes:
                # Add a function here that loops through dishes and lets the user select by number
                AT6d.append(user_input1)
                print(user_input1)
                print("OK! AT6 " + user_input1 + "!")
            elif user_input1 == '':
                print("Exiting AT-6 screen! ")
                # Specials that have been input for a strange for loop that displays them vertically here. Not sure what the fix is to this
            else:
                print("\tSorry, I don't recognize that dish...Please try again!")
        elif user_choice == 2:
            if not AT6d:
                print("The AT6 list is currently empty!")
            else:
                print("\nCURRENTLY AT6'd:")
                for at6d_dishes in AT6d:
                    print("- " + at6d_dishes.title())
                user_input2 = input("\nGreat! What would you like to take off the AT6 List? ")
            if user_input2 in AT6d:
                AT6d.remove(user_input2)
                print("\tYou got it! " + user_input2.title() + " back in stock!")
            else:
                print("Unrecognized item...")
        elif user_choice == 3:
            choice4 = input('Are you sure you would like to clear the list? (y/n) ')
            if choice4 == 'y' or 'yes':
                AT6d = []
            elif choice4 == 'n' or 'no':
                print("No?  OK, no problem.")
            else:
                print("Unrecognized response!  Please try again!")
        elif user_choice == 4:
            # Add special soup
            print("\nPLEASE ENTER TODAY'S SPECIALS:")
            soup_entry = True
            while soup_entry:
                if not special_soup:
                    # This section will not accept an input in the if statement of n or y and react to it.
                    soup_input = input("\n\t What is the soup of the day? ")
                    soup_confirm = input("Ok, so we have " + soup_input.title() + " soup today? (y or n) ")
                    if soup_confirm == 'n':
                        print("OK, try again!")
                        continue
                    elif soup_confirm == 'y':
                        print("Alright, adding " + soup_input.title() + " soup.")
                        special_soup.append(soup_input)
                        soup_entry = False
                    elif soup_confirm == '':
                        print("Alright, no Soup du Jour today!")
                        special_soup = ['No Special Soup Today...']
                    else:
                        print("Sorry, unrecognized response!  Please try again!")
                        #continue
                else:
                    print("Soup Du Jour is currently " + str(special_soup))
                    soup_change = input("\n\tWhat would you like to change the soup to? (Press Enter to leave soup unchanged) ")
                    if soup_change == '':
                        print("\tAlright, the soup remains " + str(special_soup))
                        soup_entry = False
                    else:
                        soup_change_confirm = input("Change the Soup du Jour to " + soup_change.title() + " soup? (y or n) ")
                        if soup_change_confirm == 'y':
                            print("You got it! Soup changed to" + soup_change.title())
                            special_soup = []
                            special_soup.append(soup_change)
                            soup_entry = False

            # Add Special Mains
            # Not accepting the NO response when inputting specials.  Come back to this later. (Same issue as in the loop above.)
            special_entry = True
            while special_entry:
                specialinput = input("\n\tPlease input a special... \n\t(Press Enter if no specials...)")
                if specialinput == '':
                    no_specials_confirm = input("So there are not any specials today? (y or n) ")
                    if no_specials_confirm == 'y':
                        print("OK, just the menu today!")
                        specials = []
                        break
                else:
                    print("OK, this is what you typed in: \n\t " + specialinput.title() +
                      "\n")
                    confirm1 = input("Is this correct? (y/n)")
                    if confirm1 == 'y':
                        specials.append(str(specialinput))
                        any_more_specials = input("Any more specials to input? (y or n) ")
                        if any_more_specials == 'y':
                            continue
                        elif any_more_specials == 'n':
                            print("Alright, Today's Specials saved! ")
                            special_entry = False
                    elif confirm1 == 'n':
                        print("No? OK, try again..")
                    else:
                        print("Sorry, unrecognized response!")
                continue
        elif user_choice == 5:
            take_reservation = True
            while take_reservation:
                print("\nTAKE NEW RESERVATION: ")
                new_reservation_name = input("(Press Enter to quit...)\n\tWhat is the name? ")
                if not new_reservation_name:
                    take_reservation = False
                    break
                new_reservation_time = input("\tFor what time? ")
                new_reservation_guests = input("\tHow many guests? ")
                new_reservation_number = input("\tWhat is the phone number? ")
                new_reservation_confirm = input("\nPlease confirm the details of the new reservation: \n\t"
                                            "\nName: " + new_reservation_name.title() +
                                            "\nTime: " + new_reservation_time +
                                            "\nNum. of Guests: " + new_reservation_guests +
                                            "\nPhone Number: " + new_reservation_number +
                                            "\n\tIs this correct? (y or n)? ")
                if new_reservation_confirm == 'y':
					# Instead, append directly to the dictionary?
                    """reservations[names] = new_reservation_name
                    reservations[times] = new_reservation_time
                    reservations[guests] = new_reservation_guests
                    reservations[numbers] = new_reservation_number"""
                    reservation_names.append(new_reservation_name)
                    reservation_times.append(new_reservation_time)
                    reservation_guests.append(new_reservation_guests)
                    reservation_numbers.append(new_reservation_number) # Need to instead put this into a dictionary or something to make it better readable
                    
                    print("\n\tNew reservation confirmed!")
                elif new_reservation_confirm == 'n':
                    print("\tAlright! Please try again!")
                elif new_reservation_name == '':
                    print("\tExiting New Reservation mode!")
                    take_reservation = False
        elif user_choice == 6:
            if not reservations:
                print("\nSorry, no reservations as of yet! Keep watching that phone... ")
            else:
                print("TONIGHT'S RESERVATIONS: ")
                for names, times, guests, numbers in reservations:
                   print("\n\tName: " + names.title() + "\n\tTime: " + times + "\n\tGuests: " + guests + "\n\tContact: " + numbers)
        elif user_choice == 7:
            print("Print a list of nearby car services.")
        elif user_choice == 8:
            print("\nThis will be a vegetable glossary.")
            veg_glossary_selection = (input("\nWhat would you like the definition of? (Enter a number...) \n " +
                                            ""))
        elif user_choice == 9:
            exit_confirmation = input("\nDo you really want to exit the program? Changes will not be saved! (y or n) ")
            print("You got it. Now exiting the program. Good Shabbos.")
            break
        else:
            print("Prus?! Unrecognized command! Try again- you can do it!")
            selections()
    print("\n")



# The magic actually begins HERE.  Remember that the above just defines the function.
selections()



# Need to work at putting some of this shit into functions I think.


# Write a function called almost_out that accepts dish and a number.
# If the name of the dish is in the dishes list, ask how many are left.
# Print that or write it to some other list.
# Maybe almost_out should be a dictionary instead? To store both the name of the dish, the number left, and perhaps
# the category?

"""
    def almost_out(dish_name, number_left):
        low_item = input("What are we running out of? (Type a name) ")
        if low_item in dishes:
            almost_out.append(low_item)


almost_out
"""
"""
######################################################################################################

def AT6_item(dish_name, category, **dish_info):
"""

# L'Chaim: A Party Planning Application that will allow user to structure the backroom
# for parties, adjust seating, print table setups, menus, etc.  Should also better codify
# seat numbers.


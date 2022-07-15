import getpass  # helps to masks the user's input, thereby securing the system
# from keyboard spying
from datetime import datetime  # Helps to fetch date
import time  # Helps to create momentary stops that make the program seamless


class DoorLockSystem():
    # ALL CLASS MEMBERS AND SOME METHODS HAVE BEEN MADE PRIVATE.
    # THIS IS TO PREVENT USERS FROM CIRCUMVENTING THE SYSTEM
    # HOWEVER, WE HAVE USED NAME-MANGLING WITHIN THE SYSTEM
    # TO ALLOW US TO CHANGE THE STATE OF THESE MEMBERS INTERNALLY

    __door_closed = True  # Switches to False when the door opens
    # Starts as True because by default, the Door Lock System is closed,
    # and so is the door.

    __door_opened = False  # Switches to True when the door closes

    __session_on = False  # Once the password is entered successfully,
    # This switches to True
    __session_count = 0  # Pays attention to how many times you log into the system
    # Any count should prompt the system to ask for your password
    __commands = ['open', 'close', 'quit']  # User can't change, add, or remove
    # commands, unless they understand name-mangling. That makes the system
    # solid, and only OOP expert can crack it.

    __times_password_entered = 0  # Keep count of the number a user enters
    # their password. After 3 wrong tries, the system will display the password
    # and give the user another round of chances

    __password_created = False  # Switches to True when a user successfully
    # creates a password. Password should not be a space, it
    __password_success = False  # Switches to False when a user logs into his/her
    # session successfully
    __first_time = True  # Helps to control a particular display message
    # Switches to False when user has already interacted with the system once

    def __init__(self, current_user='user'):
        # We treat users of the Group 28 Door Lock System as objects
        # One important attribute is {current_user}, which is 'user' by default,
        # and {new_password}, which is a NoneType by default since
        # it will be changed when the user creates one
        self.__current_user = current_user
        self.__password = None
        # The password is a private member for security purposes


def create_password(self):
        created_password = getpass.getpass(
            f'Hey {self._DoorLockSystem__current_user}, Create Your Lock Door Password: ')
        # Any 4-character password works for the system
        if ' ' in created_password:
            print('ALERT: Password Cannot be Blank or Have a Blank Space')
            self.create_password()
        elif len(created_password) < 3:
            print('ALERT: Password Cannot be Shorter than 4 Characters')
            self.create_password()
        if len(created_password) > 3:
            print('SUCCESS: Password Created')
            self._DoorLockSystem__password = created_password
            self._DoorLockSystem__password_created = True
            # Once the password entered is valid, state of password_created changes

    # Throughout our code have use name-mangling to access private class and
    # instances members to make the system functional

def enter_password(self):
    # Before the system enters a password, the state of password_success is
    # False. Then, when the password is entered successfully
    # The state changes to True, same goes for session_on.
    # That means the system is ready to be used
    while self._DoorLockSystem__password_success == False:
        if self._DoorLockSystem__times_password_entered < 3:
            if self._DoorLockSystem__session_count == 0:
                entered_password = getpass.getpass(f'Hey {self._DoorLockSystem__current_user}, Please Enter Your Lock Door Password: ')
            else:
                entered_password = getpass.getpass(f'Welcome Back, {self._DoorLockSystem__current_user}, Please Enter Your Lock Door Password Again: ')

            if entered_password != self._DoorLockSystem__password:
                print("ERROR: Password Entered Doesn't Match Password Created \n")
                time.sleep(1)
                self._DoorLockSystem__times_password_entered += 1
                self._DoorLockSystem__session_on = False
                self._DoorLockSystem__password_success = False
                self.enter_password()
            else:
                print("SUCCESS: Password Correctly Entered, Door Session Started")
                self._DoorLockSystem__session_on = True
                self._DoorLockSystem__password_success = True
                break
        elif self._DoorLockSystem__times_password_entered == 3:
            print(f'ALERT: Password Entered 3 Times')
            time.sleep(1)
            print(f'ALERT: System Will Now Show Your Password')
            time.sleep(1)
            print(f'ALERT: Password Entered: {self._DoorLockSystem__password}')
            self._DoorLockSystem__times_password_entered = 0
            self._DoorLockSystem__password_success = False
            time.sleep(1)
            self.enter_password()

def enter_command(self):
        # MAIN METHOD
        # Checks if password was created
        # If it wasn't (meaning that it is still None),
        # this method sends the user back to creating a password.
        # Then, command execution will continue.
        if self._DoorLockSystem__password is None:
            print('ERROR: You First Need to Set a Password')
            self.create_password()
            self.enter_command()
        else:
            if self._DoorLockSystem__session_count > 0:
                 self.enter_password()
            if self._DoorLockSystem__first_time == True:
                time.sleep(1)
                print('ALERT: Opening Command Box [First Time]')
                time.sleep(1)
                self._DoorLockSystem__first_time = False


            command_given = input('Enter Your Command: ')

            # Checks the validity of the command that the user has entered
            if command_given not in self._DoorLockSystem__commands:
                print(f'ERROR: Invalid Input, Enter Any of These Commands: {self._DoorLockSystem__commands}')
                self.enter_command()

            elif command_given == 'open':
                if self._DoorLockSystem__door_opened == True:
                    print('ERROR: Door is Currently Open')
                    time.sleep(1)
                    print('ALERT: Loading Command Box...')
                    time.sleep(1)
                    self.enter_command()
                elif self._DoorLockSystem__door_opened == False:
                    self._DoorLockSystem__open_command()

                elif command_given == 'close':
                    if self._DoorLockSystem__door_closed == True:
                        print('ERROR: Door is Currently Closed')
                        self.enter_command()
                    elif self._DoorLockSystem__door_closed == False:
                        self._DoorLockSystem__close_command()

            elif command_given == 'quit':
                if self._DoorLockSystem__door_opened == True:
                    print('ERROR: Door Still Open, Cannot Quit System')
                    time.sleep(1)
                    print('ALERT: Loading Command Box...')
                    time.sleep(1)
                    self.enter_command()

                elif self._DoorLockSystem__door_closed == True:
                    self._DoorLockSystem__quit_command()


def __open_command(self):
        # Triggered if the door is open, switches door_opened to True
        # and, for code robustness, it switches door_closed to False
        self._DoorLockSystem__door_opened = True
        self._DoorLockSystem__door_closed = False
        door_open_time = datetime.now()
        print(f"PROCESS: Door Opening...")
        time.sleep(1)
        print(f"SUCCESS: Door Last Opened at {door_open_time}")
        time.sleep(1)
        print('ALERT: Loading Command Box...')
        time.sleep(1)
        self.enter_command()

def __close_command(self):
    # Triggered if the door is closed, switches door_opened to False
    # and, for code robustness, it switches door_closed to True
    self._DoorLockSystem__door_opened = False
    self._DoorLockSystem__door_closed = True
    door_open_time = datetime.now()
    print(f"PROCESS: Door Closing...")
    time.sleep(1)
    print(f"SUCCESS: Door Last Closed at {door_open_time}")
    time.sleep(1)
    print('ALERT: Loading Command Box...')
    time.sleep(1)
    self.enter_command()

def __quit_command(self):
    # Triggered if a user closes the system
    # Importantly, it reverts password_success back to False
    # Since the event is now complete
    # And the user will now need to enter his/her password again
    door_open_time = datetime.now()
    print(f"SUCCESS: System Closed at {door_open_time}")
    self._DoorLockSystem__session_count += 1
    self._DoorLockSystem__password_success = False

cindy = DoorLockSystem('Cindy')

cindy.create_password()

cindy.enter_password()

cindy.enter_command()

cindy.enter_command()

cindy.enter_command()



import time
import os 
from plyer import notification
from AppOpener import run 
from bs4 import BeautifulSoup
import requests
import numbers
import pywhatkit
import random
import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

os.system("color 0c")
print('''
                            ___      __        _______  ___      ___  __      ________      
                           |"  |    /""\      /"      \|"  \    /"  ||" \    /"       ) 
                           ||  |   /    \    |:        |\   \  //  / ||  |  (:   \___/  
                           |:  |  /' /\  \   |_____/   ) \\  \/. ./  |:  |   \___  \    
                        ___|  /  //  __'  \   //      /   \.    //   |.  |    __/  \\   
                       /  :|_/ )/   /  \\  \ |:  __   \    \\   /    /\  |\  /" \   :)  
                      (_______/(___/    \___)|__|  \___)    \__/    (__\_|_)(_______/   
                                                                                          
''')
 
 # JARVIS is ready to be your assistant
name = input("Enter name: ").capitalize()
print("Hello", name, "I am JARVIS, your personal asssistant")
IconPath = r"Jarvis_logo_ico.ico"
notification_title = 'JARVIS ACTIVATED!'  # notify you that jarvis is activated 
notification_message = (f'Hello {name} JARVIS is ready to be your assistant 🤖') # it look like "Hello "Abhi" JARVIS is ready to be your assistant 🤖

# Sends a notification.
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = IconPath,  
    timeout = 1,  
    toast = False  
    )

# Get the icon path for the Hello notification and display the notification
print("Do you prefer Sir or Miss")
C = input().capitalize()
print("Understood", C)
IconPath = r"Jarvis_logo_ico.ico"
notification_title = 'HELLO'  
notification_message = (f'Hello {C}')
  
# send the notification with a messae with time of 1 second 
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = IconPath,  
    timeout = 1,  
    toast = False  
    )

# Asks for user to enter the command for the jarvis to acccess the features of it
while 1:
    print("How can I help you", C)
    # Lowers the words of the user
    user_input = input().lower()
    
    # if the user enter the following words to interact with jarvis it can reply with hi or hey to the user for intraction
    if user_input == ("hello") or user_input == ("hi") or user_input == ("hey") or user_input == ("jarvis"):
        print("Hello", C)
    
    # if the user types open google command this opens the browsers with the google search page
    elif user_input == ("open google"):
        os.system('start chrome www.google.com')
        print("Opening chrome to google.com")

    # if the user enters the exit command then the jarvis performs the 3 second animation and exits the jarvis
    elif user_input == ("exit"):
        print("Exiting in")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        os.system('TASKKILL /F /IM py.exe')
        break

    # if the user enters the shutdown commands then jarvis asks for confirmation and if the user reply yes then it shutdown the computer
    elif user_input == ("shutdown"):
        print("Are you sure", C)
        Y = input("yes/no\n>>").lower()
        if Y == ("yes"):
            os.system('shutdown /p')

        # if the user cancels the shutdown then it prints canceling shutdown
        else:
            print("Canceling shutdown", C)
            
    # if the user enters the command restart then it asks for confirmation for restarts and if the user agrees then it restarts the computer
    elif user_input ==("restart"):
        print("Are you sure",C)
        Y = input("yes/no\n>>").lower()
        if Y ==("yes"):
            os.system('shutdown /r')
        
        # if the user cancel restarts then it prints cancelling restarts
        else:
            print("Cancelling Restart",C)
            
    # This block of code is for performing the arthimatic operations in jarvis 
    elif user_input in ["add" or "subtract" or "multiply" or "divide" or "modulus" or "exponentiation" or "floor division"]:
        print("Do you want me to perform arthimatic operations ?")
        Y = input("yes/no\n>>").lower()
        if Y == ("yes"):
            Y = int(input("Select the Operation to perform : \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n6) Exponential\n7) Floor Division\n>>"))
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            if Y == 1:
                print("The sum of two numbers are :",a+b)
            elif Y == 2:
                print("The subtraction of two numbers are : ",a-b)
            elif Y == 3:
                print("The multiplication of two numbers are : ",a*b)
            elif Y == 4:
                print("The division of two numbers are : ",a/b)
            elif Y == 5:
                print("The modulus of two numbers are : ",a%b)
            elif Y == 6:
                print("The exponential of two numbers are : ",a**b)
            elif Y == 7:
                print("The floor division of two numbers are : ",a//b)    
            else:
                print("Invalid Input")
                      
    # Below code is for performing open application function which opens the application on user input
    elif user_input in ["open" or "application"]:
        print("Do you want me to open an application?")
        Y = input("yes/no\n>>").lower()
        if Y == ("yes"):
            # Takes the input of the name of the application to open
            app = input("ENTER APPLICATION TO OPEN: ").strip()
        if input:
            run(app)
        else:
            print("Please check the application name you have typed")
            
    # This set of code returns the weather condition of your city
    elif user_input in ["weather"]:
        headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


        def weather(city):
         city = city.replace(" ", "+")
         res = requests.get(
          f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
         print("Searching...\n")
         soup = BeautifulSoup(res.text, 'html.parser')
         location = soup.select('#wob_loc')[0].getText().strip()
         time = soup.select('#wob_dts')[0].getText().strip()
         info = soup.select('#wob_dc')[0].getText().strip()
         weather = soup.select('#wob_tm')[0].getText().strip()
         print(location)
         print(time)
         print(info)
         print(weather+"°C")
         

        city = input("Enter the Name of City -> ")
        city = city+" weather"
        weather(city)
        print("Have a Nice Day:)")
        

    # This set of code can play any video from youtube it is basically the search bar of youtube to play videos
    elif user_input in ["youtube"]:
        try:
            user_input = input("Enter the video name to play : ")
            pywhatkit.playonyt(user_input)
            print("Playing")

        except:
            print("An unexpected error occurred")
            
    # This set of code can schedule a whats app message . But you should have whats app login in your web browser in order to schedule a whatsapp message
    elif user_input in ["whatsapp"]:
        numberr = input("Enter the number with country code : ")
        message = input("Enter the message you want to send :\n")
        hour = int(input("Enter the hour in 24 hour fomat :\n"))
        minute = int(input("Enter the minute :\n"))
        pywhatkit.sendwhatmsg(numberr,
             message,
             hour, minute)
        
    # This set of code gets activated once the user enters the game command it displays two of the game available
    elif user_input in ["game"]:
        print("I can play 2 games : \n1- Snake Water Gun\n2- Random Number Guess")
        Y = int(input())
        if Y == (1):
          # if user enters 1 then the snake water gun game starts 
            print('''
           .---. .-. .-.  .--.  ,-. .-.,---.   .-.  .-.  .--.  _______ ,---.  ,---.      ,--,   .-. .-..-. .-. 
          ( .-._)|  \| | / /\ \ | |/ / | .-'   | |/\| | / /\ \|__   __|| .-'  | .-.\   .' .'    | | | ||  \| | 
         (_) \   |   | |/ /__\ \| | /  | `-.   | /  \ |/ /__\ \ )| |   | `-.  | `-'/   |  |  __ | | | ||   | | 
         _  \ \  | |\  ||  __  || | \  | .-'   |  /\  ||  __  |(_) |   | .-'  |   (    \  \ ( _)| | | || |\  | 
        ( `-'  ) | | |)|| |  |)|| |) \ |  `--. |(/  \ || |  |)|  | |   |  `--.| |\ \    \  `-) )| `-')|| | |)| 
         `----'  /(  (_)|_|  (_)|((_)-'/( __.' (_)   \||_|  (_)  `-'   /( __.'|_| \)\   )\____/ `---(_)/(  (_) 
                (__)            (_)   (__)                            (__)        (__) (__)           (__)     
''')
            def Gamewin(a,b):
        
                if a == b:
                    return None

                    
                elif a == 's':
                    if b == 'w':
                        return False
                    elif b == 'g':
                        return True

                        
                    elif a == 'w':
                     if b == 'g':
                        return False
                    elif b == 's':
                        return True

                        
                    elif a == 'g':
                     if b == 's':
                        return False
                    elif b== 'w':
                        return True

            print("Jarvis Turn: Snake(s) Water(w) or Gun(g)")    
            randomNo = random.randint(1,3)    
            if randomNo == 1:
                a = 's'
            elif randomNo == 2:
                a = 'w'
            elif randomNo == 3:
                a = 'g'
            
            b=input("Your Turn: Snake(s) Water(w) or Gun(g)")
            c = Gamewin(a,b)
            print(f"Jarvis Chose {a}")
            print(f"You Chose {b}")
            if c == None:
                print("The game is a tie")
            elif c:
                print("You Win!")
            else:
                print("You loose!")
        
        if Y == (2):
          # if the user enters the 2 then the random number guess game starts
          
            print('''
      ____     _    _   _ ____   ___  __  __   _   _ _   _ __  __ ____  _____ ____     ____ _   _ _____ ____ ____  
     |  _ \   / \  | \ | |  _ \ / _ \|  \/  | | \ | | | | |  \/  | __ )| ____|  _ \   / ___| | | | ____/ ___/ ___| 
     | |_) | / _ \ |  \| | | | | | | | |\/| | |  \| | | | | |\/| |  _ \|  _| | |_) | | |  _| | | |  _| \___ \___ \ 
     |  _ < / ___ \| |\  | |_| | |_| | |  | | | |\  | |_| | |  | | |_) | |___|  _ <  | |_| | |_| | |___ ___) ___) |
     |_| \_/_/   \_|_| \_|____/ \___/|_|  |_| |_| \_|\___/|_|  |_|____/|_____|_| \_\  \____|\___/|_____|____|____/ 
                                                                                                               
''')
            randNumber = random.randint(1,100)
            userGuess = None
            guesses = 0

            while (userGuess != randNumber):
                userGuess = int(input("Enter your guess:"))
                guesses += 1
                if (userGuess == randNumber):
                    print("You guessed it right")
                else:
                    if(userGuess>randNumber):
                        print("You guessed it wrong! Enter a smaller number")
                    else:
                        print("You guessed it wrong! Enter a larger number")

            print(f"You guessed the number in {guesses} guesses")
            
    # This set of returns the details of a phone number
    elif user_input == ("phonenumber"):
        number = input("Enter the phone number with county code: ")
        number = ph.parse(number)
        print(timezone.time_zones_for_number(number))
        print(carrier.name_for_number(number, "en"))
        print(geocoder.description_for_number(number, "en"))
            
    elif user_input == ("help"):
        # Help command is for displaying all the commands a user can input for jarvis to work 
        print("It Seems That You Need Help")
        time.sleep(1)
        print("\nSo Jarvis could perform the folllowing tasks with following command")
        time.sleep(1)
        print('''\n
                   "hello"  --------->  Intracts with user
                   "open google"  --->  Opens google in browser
                   "exit"  ---------->  Jarvis exits
                   "shutdown"  ------>  Shutdowns the system
                   "restart"  ------->  Restarts the system
                   "add"  ----------->  Perform arthimatic operations
                   "open"  ---------->  Can open any installed applications
                   "weather"  ------->  Checks the weather of your city
                   "youtube"  ------->  Plays the video from youtube
                   "whatsapp"  ------>  Schedule whatsapp's message
                   "game"  ---------->  Can play games with JARIVS
                   "help"  ---------->  Shows all the commands of JARVIS
                   "phonenumber"  --->  Gets the detail about phonenumber''')
            
    else:
      # if the above command is not entered then it prints the following line
        print("I'm not sure I understand", C)

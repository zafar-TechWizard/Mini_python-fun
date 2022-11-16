from ast import main
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
print(voices[1].id) 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak(f"Hellow there, welcome to the virtual ATM machine")
    
def main():
    balance = 500000

    time.sleep(0.2)
    print("""
    Welcome to ATM Machine""")
    time.sleep(0.2)
    print(" ")
    print("""
        1)BALANCE
        2)WITHDRAW
        3)DEPOSIT
        4)EXIT

        """)
    time.sleep(0.3)
    speak("Choose your query :- ")
    option = int(input("Choose any option:- "))

    if(option == 1):
            speak("Gathering your Bank details...")
            print("Gathering Bank details...")
            time.sleep(0.4)
            print("Your current account balance is:-", balance)
            speak("Your crrent account balance is")
            speak(balance)
            speak("Do you want to exit ?")
            ans1=input("Do you want to exit ? (Y/N) :-- ")
            if "N" and "n" in ans1:
                speak("okay-Then !")
                main()   
            else:
                speak("Thank you for using our servies!")
                time.sleep(0.2)
                exit()
            
    elif(option==2):
            time.sleep(0.2)
            speak("Please Enter the amount to withdraw")
            withdraw = int(input("Please enter the amount to withdraw "))
            speak("you have entered")
            speak(withdraw)
            if(balance > withdraw):
                total = balance - withdraw
                time.sleep(0.5)
                print("Withdrawal sucessfull")
                speak("Withdrawal sucessfull")
                time.sleep(0.8)
                print("Now your balance is : ",total)
                speak("Now your balance is ")
                speak(total)
                speak("Do you want to exit ?")
                ans2=input("Do you want to exit ? (Y/N) :-- ")
                if "N" and "n" in ans2:
                    speak("ok")
                    main()   
                else:
                    speak("Thank you for using our servies !")
                    time.sleep(0.2)
                    exit()
                
            else:
                time.sleep(1)
                print("Hey Sir...")
                time.sleep(0.1)
                print("Check your balance")
                speak("I think you should first check your account balance, before going for this-much of the amount")
                time.sleep(0.1)
                print("Thank You.")
                speak("Thank You.")
                time.sleep(5)
    elif(option==3):
            speak("Enter amount to deposit ")
            deposit = int(input("Enter amount to deposit "))
            speak("you have entered")
            speak(deposit)
            totalbalance = balance + deposit
            time.sleep(1)
            print("Deposit successfull")
            speak("Deposit successfull")
            time.sleep(0.5)
            print("Total balnace is now : ", totalbalance)
            speak("Total balnace is now : ")
            speak(totalbalance) 
            speak("Do you want to exit ?")
            ans3=input("Do you want to exit ? (Y/N) :-- ")
            if "N" and "n" in ans3:
                speak("ok")
                main()   
            else:
                speak("Thank you for using our servies")
                time.sleep(0.2)
                exit()
            
    elif(option==4):
            speak("All-right")
            exit()
    else:
            speak("You have not selected a valid option")
            speak("please go through the options again")
            time.sleep(2)
            main()
            print("No selected transaction")
            time.sleep(4)

if __name__ == "__main__":
    
    main()
import csv
import pandas as pd
def platform():
    UserLocker = {}
    Begin = True
    while Begin:
        platform = input("Enter the name of the platform You want to save its' username and password!!! ").upper()
        if platform != "":
            UserLocker["Platform"] = platform
            UserName = input(f"Enter The UserName You used on {platform}: ")
            if UserName != "":
                UserLocker["UserName"] = UserName
                Password = input(f"Enter the Password You used on {platform}: ")
                if Password != "":
                    UserLocker["Password"] = Password
                    Begin = False
                    return UserLocker

                else:
                    continue
            else:
                continue
        else:
            continue
            
if __name__ == "__main__":
    # the input is intended to be converted into pandas dataframe
    userlocker_data = platform()
    
    with open('PasswordBank.csv', 'a+', newline='') as write_obj:
    
        fieldnames = ['Platform','UserName','Password']
        writer = csv.DictWriter(write_obj,fieldnames=fieldnames)
        
        writer.writerow(userlocker_data)
        
   

                
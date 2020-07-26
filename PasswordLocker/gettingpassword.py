#! python3.6
# gettingpassword.py


# this goes into the excelspreedheet and collects the items in it
# but first we use a dictionary
import sys
import pandas as pd
import pyperclip as pc

def the_dataset(somecsv):
    Platformlist = []
    UserNamelist  = []
    Passwordlist = []
    PasswordBank_dict = {}
    for i,row in somecsv.iterrows():
        Platform = row["Platform"]
        UserName = row["UserName"]
        Password = row["Password"]
        if Platform not in PasswordBank_dict:
            Platformlist.append(Platform)
            UserNamelist.append(UserName)
            Passwordlist.append(Password)
            PasswordBank_dict["Platform"] = PasswordBank_dict.get("Platform",Platformlist)
            PasswordBank_dict["UserName"] = PasswordBank_dict.get("UserName",UserNamelist)
            PasswordBank_dict["Password"] = PasswordBank_dict.get("Password",Passwordlist)
        
    PasswordBank_df = pd.DataFrame.from_dict(PasswordBank_dict,orient="index")
   
    return PasswordBank_df
if __name__ == "__main__":
    PasswordBank_csv = pd.read_csv("C:\\Users\\Oke Oladunsi\\Desktop\\Azure\\AutomateBoringStuffProjects\\PasswordLocker\\PasswordBank.csv")
    new = the_dataset(PasswordBank_csv)
    #print(new[0])
    if len(sys.argv) < 2:
        print("Usage: py platform.py [platform] - copy account password")
        #we will now check if the input is in dataframe using a variable account
        account = sys.argv[1]
        for i in new:
            if new[0]["Platform"] == account.upper():
                pc.copy(new[i])
                print(f"the details of the account you selected is {new[i]} and is copied to clipboard")
            else:
                print("Account not found")
    
        
        
   
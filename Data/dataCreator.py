import pandas as pd
import random

def create_Passwords(count,digit_count):
    listOfCount= list(range(0,count))

    listOfPasswords=[]

    for a in listOfCount:
        password=""
        print(a)
        for j in range(0,digit_count):
            k=random.randint(0,9)
            password = password + str(k)
        listOfPasswords.append(password)

    df=pd.DataFrame({
        'id': listOfCount,
        'password': listOfPasswords
    })

    df.to_csv(f"{count}-{digit_count}Digit.csv",index=False)



create_Passwords(99,4)
#
# yingyue3 lab D07 MA4.py
# I declare that I did not collaborate with anyone in this micro-assignment. 
# Besides the lab and class notes, I used the following resources: 
# provided sample Python code in eclass
# 

import sqlite3
import time

connection = None
cursor = None

def connect(path):
    global connection, cursor
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def get_data():
    age = int(input(">> Which age A would you like to use in your query? "))
    percentage = int(input(">> What percentage P would you like to use in your query? "))
    return age, percentage

def select_data(age, percentage):
    global connection, cursor
    cursor.execute("SELECT NEIGHBOURHOOD FROM Census WHERE AGE = :A AND (FEMALE - MALE)*100/MALE > :P OR AGE = :A AND MALE = 0 AND FEMALE <> 0;",
        {"A":age, "P":percentage})

    rows = cursor.fetchmany(5)
    if rows != []:
        for i in range(len(rows)):
            print(rows[i][0])
    else: 
        print("End of results.")
        return
    
    while True:
        rows = cursor.fetchmany(5)
        if rows == []:
            print("End of results.")
            break
        input(">> Press enter to continue ...")
        for i in range(len(rows)):
            print(rows[i][0])
    return

def main():
    global connection, cursor
    path = "./ma4.db"
    connect(path)
    print("Connection to the database open.")
    age, percentage = get_data()
    select_data(age, percentage)
    connection.commit()
    connection.close()
    print("Connection to the database close.")
    return

if __name__ == "__main__":
    main()
    

from dotenv import load_dotenv
import os
from tasks import task

load_dotenv()

password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")


open_admin = input("do you want to open admin mod? yes/no :")
while True:
    if open_admin == "yes" : 
        password_1 = input("enter the password : ")

        if password_1 == password:
            print("right")
            break
            
        else:
            print("worng")
            continue
 


else : 
    print("ok")


pleas_enter_priority = input("please enter a priority (mediom , high, low : )")

name = input("whats your name : ")
print("welcome")

for i in task:
    task_1 = i["task_1"]

task_task = input(task_1)



print(f"{name} your task is {task_task} and your priority is {pleas_enter_priority}")

with open("task.txt", "a") as a:
    a.write(f"{name} your task is {task_task} your priority is {pleas_enter_priority}\n")



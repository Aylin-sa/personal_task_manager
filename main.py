from tasks import task

name = input("whats your name : ")
print("welcome")

for i in task:
    task_1 = i["task_1"]

t = input(task_1)

print(f"{name} your task is {t}")

s = "Artificial Intelligence"
print(s.split()[0])
print("hello python".upper())
print("abcdef"[::-1])
nums = [1, 2, 3, 4, 5]
for i in nums:
    if i%2==1:
        nums.remove(i)
unsort=[3, 1, 5, 2]
unsort.sort()
print(unsort)
unsort.remove(3)
print(unsort)
a = [1, 2, 3]
b=a.copy()
b[0]=10
print(a)
print(b)
user = ("Tom", 22)
print(f"name: {user[0]}, age: {user[1]}")

def show_menu():
    todos=[]
    while(True):
        choice=int(input("""
======TODO======

1.查看todo
2.添加todo
3.删除todo
4.退出

================
请选择："""))
        if choice==1:
            show_todo(todos)
        elif choice==2:
            add_todo(todos)
        elif choice==3:
            delete_todo(todos)
        elif choice==4:
            print("bye！")
            break

def show_todo(todos):
    print("======TODO======")
    for i in range(len(todos)):
        print(f"{i+1}.[]{todos[i]}")
    print("================")
    pass

def add_todo(todos):
    todo=input("输入todo名: ")
    todos.append(todo)
    print("添加成功")
    pass

def delete_todo(todos):
    num=int(input("输入todo编号："))
    todos.pop(num-1)
    print("删除成功")
    pass

def main():
    show_menu()

main()
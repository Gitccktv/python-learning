
def show_menu():
    todos=[]
    while(True):
        choice=int(input("""
====================
    TODO APP
====================

1. 查看任务
2. 添加任务
3. 删除任务
4. 完成任务
5. 退出

请选择："""))
        
        if choice==1:
            show_todos(todos)
        elif choice==2:
            add_todo(todos)
        elif choice==3:
            delete_todo(todos)
        elif choice==4:
            complete_todo(todos)
        elif choice==5:
            print("bye!")
            break
    pass


def show_todos(todos):
    print("====== TODO ======\n")
    for i in range(len(todos)):
        if(todos[i]["completed"]):
            print(f"{i+1}.[x]{todos[i]['title']}")
        else:
            print(f"{i+1}.[ ]{todos[i]['title']}")
    print("\n==================")
    pass


def add_todo(todos):
    title=input("请输入任务：")
    task={
        "title":title,
        "completed":False,

    }
    todos.append(task)
    print("添加成功！")
    pass


def delete_todo(todos):
    n=int(input("请输入任务编号："))
    todos.pop(n-1)
    print("删除成功！")
    pass


def complete_todo(todos):
    n=int(input("请输入任务编号："))
    todos[n-1]["completed"]=True
    print("任务已完成！")

def main():
    show_menu()
    pass

if __name__ == "__main__":
    main()
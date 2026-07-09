from datetime import datetime
import os

from task import Task
from storage import save_tasks, load_tasks
print(os.getcwd())


def get_mark(task):
    if task.done:
        return "☑"
    else:
        return "☐"
    
def print_task(i, task):
    mark = get_mark(task)

    print(f"{i + 1}. {mark} [{task.priority}] {task.name}")
    print(f"    期限: {task.deadline}") 

def input_task_number(tasks,message):
    show_tasks(tasks)

    try:
        number = int(input(message))
    except ValueError:
        print("数字を入力してください")
        return None

    if 1 <= number <= len(tasks):
        return number
    else:
        print("正しい番号を入力してください")
        return None

    
def show_tasks(tasks):
    print('=== タスク一覧 ===')

    if len(tasks) == 0:
        print('タスクはありません')
    else:
        today = datetime.today().date()
        
        for i, task in enumerate(tasks):
            deadline = datetime.strptime(task.deadline,"%Y-%m-%d").date()

            print_task(i,task)

            if deadline < today and not task.done:
                print('⚠ 期限切れ')

def delete_task(tasks):  
    if len(tasks) == 0:
            print('タスクはありません')
    else:
        number = input_task_number(tasks, "削除する番号:")

        if number is None:
            return
        
        tasks.pop(number - 1)
        save_tasks(tasks)
        print('タスクを削除しました')

        

def edit_task(tasks):
    if len(tasks) == 0:
        print('タスクはありません')
    else:
        number = input_task_number(tasks, "編集する番号:")

        if number is None:
            return
        new_task = input('新しいタスク:')
        tasks[number - 1].name = new_task
        save_tasks(tasks)
        print('タスクを編集しました')

        


def complete_task(tasks):
    if len(tasks) == 0:
        print('タスクはありません')
        return
    
    number = input_task_number(tasks, "完了する番号:")

    if number is None:
        return
    tasks[number - 1].done = True
    save_tasks(tasks)
    print('タスクを完了しました！')
    
def search_task(tasks):
    keyword = input("検索する文字:")

    found = False

    for i, task in enumerate(tasks):

        if keyword in task.name:
            found = True
            print_task(i,task)

    if not found:
        print('一致するタスクはありません')




def add_task(tasks):
    task = input('追加するタスク:')
    while True:
        priority = input('優先度(高・中・低):')
       
        if priority in ["高", "中", "低"]:
            break
        else:
            print("高・中・低のどれかを入力してください")
            
    while True:
        deadline = input("期限（例: 2026-07-10）:")

        try:
            datetime.strptime(deadline,"%Y-%m-%d")
            break
        except ValueError:
            print("2026-07-10の形式で入力してください")

    tasks.append(
        Task(
            task,
            priority,
            deadline
        )
    )

    save_tasks(tasks)
    print('タスクを追加しました!')

def show_menu():

    print('=== ToDOアプリ ===')
    print('1. タスクを追加')
    print('2. 一覧表示')
    print('3. タスクを削除')
    print('4. タスクを編集')
    print('5. タスクを完了')
    print('6. タスク検索')
    print('7. 終了')

tasks = load_tasks()
while True:
    
    show_menu()
    choice = input('番号を入力してください:')
    

    
    if choice == "1":
        add_task(tasks)

    elif choice == "2":       
        show_tasks(tasks)
    
    elif choice =='3':
        delete_task(tasks)
    
    elif choice == '4':
        edit_task(tasks)

    elif choice == '5':
        complete_task(tasks)

    elif choice == '6':
        search_task(tasks)

    elif choice == '7':
        print('終了します')
        break

    else:
        print('正しい番号を入力してください')




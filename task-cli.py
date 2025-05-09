import argparse
import json
import datetime
import os

data = "file.json"

def load_json():
    if not os.path.exists(data):
        return []
    with open (data, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def save_json(task):
    with open (data, "w") as file:
        return json.dump(task, file, indent=4, default=str)
    
def main():
    parser = argparse.ArgumentParser(description="todo list")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add", help="add task")
    add.add_argument("task", type=str, help="task")

    mark = subparsers.add_parser("mark-in-progress", help="mark task as progress")
    mark.add_argument("progress", type=int, help="in-progress")
    
    mark_1 =subparsers.add_parser("mark-done", help="mark task as done")
    mark_1.add_argument("done", type=int, help="done")

    delete = subparsers.add_parser("delete", help="delete task by id")
    delete.add_argument("id", type=int, help="delete task")

    update = subparsers.add_parser("update", help="update task")
    update.add_argument("id", type=int, help="update list")
    update.add_argument("task", type=str, help="update task desc")

    list = subparsers.add_parser("list-all", help="Listing all task")
    
    list_status = subparsers.add_parser("list", help="listing task by status")
    list_status.add_argument("status", help="done/progress")
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.task)
    elif args.command == "update":
        update_task(args.id, args.task)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_progress(args.progress)
    elif args.command == "mark-done":
        mark_done(args.done)
    elif args.command == "list-all":
        list_all_task()
    elif args.command == "list":
        list_task(args.status)

def date():
    time = datetime.datetime.now()
    return time.strftime("%Y-%m-%d %H:%M")

def add_task(des):
    tasks = load_json()
    id = 1 + len(tasks)
    task = {
        "id": id,
        "description": des,
        "status": "todo",
        "createdAt": date(),
        "updateAt": date()
    }
    tasks.append(task)
    save_json(tasks)
    print(f"task added succesfully {task["id"]}")

def update_task(id, t):
    tasks = load_json()
    for task in tasks:
        if task["id"] == id:
            task["description"] = t
            task["updateAt"] = date()
            save_json(tasks)
    print(f"update task succesfully")

def delete_task(id):
    tasks = load_json()
    tasks = [item for item in tasks if item["id"] != id]
    save_json(tasks)
    print(f"delete task {id} succesfully")

def mark_done(id):
    tasks = load_json()
    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            task["updateAt"] = date()
            save_json(tasks)
    print(f"mark task {id} as done succes")

def mark_progress(id):
    tasks = load_json()
    for task in tasks:
        if task["id"] == id:
            task["status"] = "progress"
            task["updateAt"] = date()
            save_json(tasks)
    print(f"mark task {id} as progress succes")

def list_all_task():
    tasks = load_json()
    print(json.dumps(tasks, indent=4))
    
def list_task(task):
    tasks = load_json()
    for i in tasks:
        if i["status"] == task:
            print(json.dumps(i, indent=4))
       

if __name__ == "__main__":
    main()
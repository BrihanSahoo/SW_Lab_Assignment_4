import csv
import os
import datetime

TASKS_FILE = "A2_07_4_3_59.csv"
HISTORY_DIR = ".task_history"
HEADERS = ["id", "title", "completed"]

def initialize_storage():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()

    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)


def save_tasks(tasks, message="Update"):
    # Save main tasks file
    with open(TASKS_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(tasks)

    # Save history snapshot
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_path = os.path.join(HISTORY_DIR, f"tasks_{timestamp}.csv")

    with open(snapshot_path, 'w', newline='') as f:
        f.write(f"# Change: {message}\n")
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(tasks)


def load_tasks():
    tasks = []

    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                row['id'] = int(row['id'])
                row['completed'] = row['completed'] == 'True'
                tasks.append(row)

    return tasks


def add_task(title):
    tasks = load_tasks()

    new_id = max([t['id'] for t in tasks], default=0) + 1

    tasks.append({
        "id": new_id,
        "title": title,
        "completed": False
    })

    save_tasks(tasks, f"Added task: {title}")
    print(f"Task '{title}' added.")


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        status = "[x]" if t['completed'] else "[ ]"
        print(f"{t['id']}. {status} {t['title']}")


def complete_task(task_id):
    tasks = load_tasks()
    found = False

    for t in tasks:
        if t['id'] == task_id:
            t['completed'] = True
            found = True
            break

    if found:
        save_tasks(tasks, f"Completed task ID: {task_id}")
        print(f"Task {task_id} marked as complete.")
    else:
        print("Task ID not found.")


def show_history():
    print("\n--- Task Change History ---")

    if not os.path.exists(HISTORY_DIR):
        print("No history found.")
        return

    files = sorted(os.listdir(HISTORY_DIR))

    for file in files:
        with open(os.path.join(HISTORY_DIR, file), 'r') as f:
            first_line = f.readline().strip()
            time_str = file.replace("tasks_", "").replace(".csv", "")
            print(f"[{time_str}] {first_line.replace('# Change: ', '')}")


# CLI Interface
if __name__ == "__main__":
    initialize_storage()

    while True:
        print("\n--- CLI Task Manager (CSV) ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. View History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            try:
                tid = int(input("Enter task ID to complete: "))
                complete_task(tid)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == '4':
            show_history()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

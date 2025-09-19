
import random
import datetime
import csv
import os


# random affirmations
affirmations = [
            "You’re improving every day.",
            "you're a good person"
            "Consistency beats perfection.",
            "Small steps = big results.",
            "Your work matters.",
            "Stay consistent.",
            "stay positive"
        ]

# journal class
class journalEntry:
    def __init__(self,entry_text,mood,line,time):
        self.entry_text = entry_text
        self.mood = mood
        self.line = line
        self.time = time

    def add_journal_entry(self):
        with open("data/journal_entries.txt", "a") as file:
            file.write(f" Date: {self.time}\nMood: {self.mood}\nEntry: {self.entry_text}\nAffirmation: {self.line}\n")
            file.write("-----------------------------------------------\n")


# task class
class Task:
    def __init__(self,T_name,T_deadline,T_priority):
        self.T_name = T_name
        self.T_deadline = T_deadline
        self.T_priority = T_priority
        self.status = "pending"


    def save_to_csv(self):
        os.makedirs("data", exist_ok=True)  # Ensure folder exists

        filename = "data/tasks.csv"
        file_exists = os.path.exists(filename)

        add_header = False
        if file_exists:
            with open(filename, "r") as file:
                first_line = file.readline()
                if "Task" not in first_line:
                    add_header = True
        else:
            add_header = True

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if add_header:
                writer.writerow(["Task", "Deadline", "Importance", "Status"])
            writer.writerow([self.T_name, self.T_deadline, self.T_priority, self.status])

# function to view all the journal entries
def view_journal_entries():
    if os.path.exists("data/journal_entries.txt"):
        with open("data/journal_entries.txt", "r") as file:
            content = file.read()
            print("your joournal entries")
            print(content)
    else:
        print(f"NO journal entries found yet.")


# function to view all the tasks from the tasks.csv
def view_task():
    if os.path.exists("data/tasks.csv"):
        with open("data/tasks.csv","r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("no tasks added yet")
                return

            print("your tasks")
            for row in rows[1:]:  # Skip the header
                print(f"Task: {row[0]} | Deadline: {row[1]} | Priority: {row[2]} | Status: {row[3]}")
    else:
        print("no task file found")


# function to mark tasks complete
def mark_task_completed():
    filename = "data/tasks.csv"

    if not os.path.exists(filename):
        print("No tasks found.")
        return

    # Step 1: Read all tasks
    with open(filename, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No tasks to mark.")
        return

    # Step 2: Show tasks with index
    print("\nYour Tasks:")
    for index, row in enumerate(reader[1:], start=1):  # Skipping header
        print(f"{index}. {row}")

    # Step 3: Ask which task to mark
    try:
        choice = int(input("Enter the task number to mark as completed: "))
        if choice < 1 or choice >= len(reader):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 4: Mark as completed (assume status is the last column)
    reader[choice][-1] = "Completed"

    # Step 5: Save back to CSV
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    print("Task marked as completed successfully!\n")



# creaing objects for journalEntry class and calling its function
def add_journal():
    entry_text = input("How was your day? ")
    mood = input("What is your mood today? ")
    time = datetime.datetime.now().strftime("%d-%m-%y %I:%M %p")
    line = random.choice(affirmations)

    entry = journalEntry(entry_text, mood, line, time)
    entry.add_journal_entry()
    print("Journal saved!")
    print("Affirmation for you:", line)


# creating the object for Task class and calling its function
def add_task():
    T_name = input("Enter task name: ")
    T_deadline = input("Enter deadline (DD-MM-YYYY): ")
    T_priority = input("Enter priority (High/Medium/Low): ")

    task = Task(T_name, T_deadline, T_priority)
    task.save_to_csv()
    print("Task saved successfully!")


# delete data from the journal_entries.txt
def delete_all_journal_entries():
    if os.path.exists("data/journal_entries.txt"):
        confirm = input("Are you sure you want to delete all journal entries? (yes/no): ").lower()
        if confirm == "yes":
            open("data/journal_entries.txt", "w").close()
            print("All journal entries deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("No journal entries found.")


# delete data from tasks.csv
def delete_all_tasks():
    if os.path.exists("data/tasks.csv"):
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
        if confirm == "yes":
            open("data/tasks.csv", "w").close()
            print("All tasks deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("No task file found.")


# menu to control all the function
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Journal Entry")
        print("2. Add Task")
        print("3. View Journal Entries")
        print("4. View Tasks")
        print("5. Mark Task as Completed")
        print("6. delete all data from journal")
        print("7 delete all data from tasks")
        print("8 exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_journal()
        elif choice == "2":
            add_task()
        elif choice == "3":
            view_journal_entries()
        elif choice == "4":
            view_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            delete_all_journal_entries()
        elif choice == "7":
            delete_all_tasks()
        elif choice == "8":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please enter (1-6).")

# main function calling
if __name__ == '__main__':
    menu()

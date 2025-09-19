import datetime
import os
print(datetime.datetime.now().strftime("%d-%m-%y %I:%M %p"))
def view_journal_entries():
    if os.path.exists("data/journal_entries.txt"):
        with open("data/journal_entries.txt", "r") as file:
            content = file.read()
            print("your joournal entries")
            print(content)
    else:
        print(f"NO journal entries found yet.")

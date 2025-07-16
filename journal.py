
import random
import datetime
import os
import sys

affirmations = [
            "You’re improving every day.",
            "Consistency beats perfection.",
            "Small steps = big results.",
            "Your work matters.",
            "Stay consistent."
        ]

class journalEntry:
    def __init__(self,entry_text,mood,line,time):
        self.entry_text = entry_text
        self.mood = mood
        self.line = line
        self.time = time

    def add_journal_entry(self):
        with open("data/journal_entries.txt", "a") as file:
            file.write(f" Date: {self.time}\nMood: {self.mood}\nEntry: {self.entry_text}\nAffirmation: {self.line}\n")
            file.write("----------------------------------------------\n")


class Task:
    def __init__(self):
        pass


entry_text = input("📝 How was your day?" )
mood = input("😊 What is your mood today?")

time = datetime.datetime.now().strftime("%d-%m-%y %I:%M %p")
line = random.choice(affirmations)

entry = journalEntry(entry_text,mood,line,time)

print(entry.time)
print(entry.line)
entry.add_journal_entry()
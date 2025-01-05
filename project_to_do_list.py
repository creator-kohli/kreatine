# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 03:02:02 2025

@author: harshit
"""

import json
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# List of motivational quotes in different categories
start_quotes = [
    "\"The only way to do great work is to love what you do.\" – Steve Jobs",
    "\"Don’t watch the clock; do what it does. Keep going.\" – Sam Levenson"
]

task_management_quotes = [
    "\"Success is the sum of small efforts, repeated day in and day out.\" – Robert Collier",
    "\"The future belongs to those who believe in the beauty of their dreams.\" – Eleanor Roosevelt"
]

completion_quotes = [
    "\"It always seems impossible until it’s done.\" – Nelson Mandela",
    "\"The secret of getting ahead is getting started.\" – Mark Twain"
]

general_quotes = [
    "\"Success doesn’t come from what you do occasionally, it comes from what you do consistently.\" – Marie Forleo",
    "\"You don’t have to be great to start, but you have to start to be great.\" – Zig Ziglar"
]

# Initialize the task list as an empty dictionary
TaskList = {}

# Function to save TaskList to a file
def save_to_file():
    try:
        with open("tasks.json", "w") as file:
            json.dump(TaskList, file, indent=4)  # Pretty-print the JSON file
    except Exception as e:
        print(Fore.RED + f"Error saving to file: {e}")

# Function to load tasks from the file
def load_from_file():
    try:
        with open("tasks.json", "r") as file:
            global TaskList
            TaskList = json.load(file)
    except FileNotFoundError:
        print(Fore.YELLOW + "No saved tasks found. Starting with an empty list.")
    except Exception as e:
        print(Fore.RED + f"Error loading from file: {e}")

# Function to add a task to the list
def add_to_list(x='', entry='', DeadLine='', status='Pending....'):
    try:
        # Ensure task is not already in the list based on the entry value
        if entry not in TaskList.values():
            TaskList[x] = f'{x} :- ' + DeadLine + '  ' + entry + '       ' + status
            save_to_file()  # Save the updated TaskList to file
        else:
            print(Fore.YELLOW + "Task already exists in the list!")
    except Exception as e:
        print(Fore.RED + f"Error adding task: {e}")

# Function to remove a task from the list using its serial number
def remove_from_list(serial_no):
    try:
        if serial_no in TaskList:
            del TaskList[serial_no]
            print(Fore.GREEN + f'Task {serial_no} removed successfully.')
            # Reassign serial numbers after deletion
            reassign_serial_numbers()
            save_to_file()  # Save the updated TaskList to file
        else:
            print(Fore.RED + "Task with this serial number doesn't exist!")
    except Exception as e:
        print(Fore.RED + f"Error removing task: {e}")

# Reassign serial numbers after deletion
def reassign_serial_numbers():
    global TaskList
    TaskList = {str(i+1): TaskList[task] for i, task in enumerate(TaskList)}
    print(Fore.YELLOW + "Serial numbers re-assigned successfully.")

# Function to print a random quote from a list of categories
def print_quote(quote_list):
    print(Fore.MAGENTA + random.choice(quote_list)) # Display the first quote for now

# Main loop to interact with the user
x = 0  # Initialize task serial number
load_from_file()  # Load saved tasks when the program starts
__ = True
while __ == True:
    try:
        # Display a motivational quote at the start of the program
        print_quote(start_quotes)

        # Display menu to user
        command = int(input(Fore.CYAN + '==============TO-DO-LIST=============== \n Welcome to your personal Task Manager\n With this New Year, start your journey of discipline and hard work\n1 :- Add a Task \n2 :- Delete a Task \n3 :- Mark a Task as completed.\n4 :- View The List\n5 :- Exit\nChoose one of the serial numbers: '))

        if command == 1:  # Add a Task
            print_quote(task_management_quotes)  # Display a task management quote
            _ = True
            while _ == True:
                entry = input(Fore.LIGHTCYAN_EX + 'Let\'s get started! What\'s your task? ')
                DeadLine = input(Fore.LIGHTCYAN_EX + 'Set the Dead-Line for your Task (format: DD/MM/YY): ')
                
                while True:
                    moreTask = input(Fore.YELLOW + 'Want to add more tasks?\n1. Yes\n2. No: ')
                    if moreTask == '1':
                        _ = True
                        break
                    elif moreTask == '2':
                        _ = False
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please enter '1' for Yes or '2' for No.")
                x += 1
                add_to_list(str(x), entry, DeadLine)

        elif command == 2:  # Delete a Task
            print_quote(general_quotes)  # Display a general quote
            del_ = True
            while del_ == True:
                print(Fore.CYAN + "Here are your current tasks:")
                for y in TaskList.values():
                    print(Fore.CYAN + y)
                serial_no = input(Fore.YELLOW + 'Type the serial number of the task you want to remove\nEnter Here: ')
                remove_from_list(serial_no)
                
                while True:
                    more_to_delete = input(Fore.YELLOW + 'Want to delete more tasks?\n1. Yes\n2. No: ')
                    if more_to_delete == '1':
                        del_ = True
                        break
                    elif more_to_delete == '2':
                        del_ = False
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please enter '1' for Yes or '2' for No.")

        elif command == 3:  # Mark a Task as Completed
            print_quote(completion_quotes)  # Display a completion quote
            _ = True
            while _ == True:
                print(Fore.CYAN + "Here are your current tasks:")
                for y in TaskList.values():
                    print(Fore.CYAN + y)

                updateTask = input(Fore.LIGHTGREEN_EX + 'Completed a task? Mark it here (enter task serial number): ')
                
                if updateTask.isdigit() and updateTask in TaskList:
                    task = TaskList[updateTask]
                    TaskList[updateTask] = task[0:-12] + 'Completed....'
                    print(Fore.GREEN + f'Task {updateTask} marked as completed.')
                    save_to_file()  # Save the updated TaskList to file
                else:
                    print(Fore.RED + "Invalid task number or task doesn't exist!")

                while True:
                    updatemoretask = input(Fore.YELLOW + 'Want to update more tasks?\n1. Yes\n2. No: ')
                    if updatemoretask == '1':
                        _ = True
                        break
                    elif updatemoretask == '2':
                        _ = False
                        break
                    else:
                        print(Fore.RED + "Invalid input! Please enter '1' for Yes or '2' for No.")

        elif command == 4:  # View the List of Tasks
            print(Fore.MAGENTA + '==============View your List============')
            print(Fore.YELLOW + 'Remember, stay focused and tackle one task at a time.')
            if TaskList:
                for y in TaskList:
                    if 'Completed' in TaskList[y]:
                        print(Fore.LIGHTGREEN_EX + f'{y}: {TaskList[y]}')
                    else:
                        print(Fore.LIGHTRED_EX + f'{y}: {TaskList[y]}')
            else:
                print(Fore.RED + "No tasks in the list.")
            
            print('============end of list=============')

        elif command == 5:  # Exit
            print(Fore.CYAN + 'Thank you for using the To-Do List')
            print(Fore.CYAN + 'Good luck with your tasks!')
            print(Fore.GREEN + '  __________\n /          \\ \n|            |\n|  O      O  |\n|     ^      |\n|   \\\\___//  |                   BYE BYE \n \\   \___//  // \n  \\________//')
            __ = False  # Exit the loop

        else:
            print(Fore.RED + "Invalid option. Please choose a valid command.")

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")









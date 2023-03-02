import os
import time

def run_command(directory, command):
    try:
        os.chdir(directory)
        os.system(f'start cmd /k {command}')
    except Exception as e:
        print('Error while running command')
        print(f'Error: {e}')
        print(f'Command: {command}')

def read_file(file_name):
    try:
        with open(file_name) as file:
            return file.readlines()
    except FileNotFoundError as e:
        print('Error while reading file')
        print(f'Error: {e}')
        print(f'File: {file_name}')

def read_base_dir():
    base_dir = ''

    try:
        with open('data/base_path.txt') as base_file:
            base_dir = base_file.readline()
    except FileNotFoundError:
        base_dir = input('Enter base directory: ')

    return base_dir

def get_command_collection(**commands) -> list:
    print(os.getcwd())

    files = os.listdir(f'data')

    command_file = 'default'

    if 'default.txt' not in files:
        command_file = input('Enter command file: ')

    file = f'data/{command_file}.txt'

    file_commands = read_file(file)
        
    commands = [tuple(command.split('|')) for command in file_commands]

    return commands

# Enter the base directory where the frontend and site folders are located
# Else input the base directory when running the script
# Example: C:\\Users\\User\Work\\project\\ui
base_dir = read_base_dir()

# Enter additional command collections in the data folder
commands = get_command_collection()

for directory, command in commands:
    print(f'Running command: {command} in directory: {base_dir + directory}')
    run_command(base_dir + directory, command)
    time.sleep(0.2)
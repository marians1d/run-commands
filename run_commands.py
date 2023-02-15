import os
import time

def run_command(directory, command):
    try:
        os.chdir(directory)
        os.system(f'start cmd /k {command}')
    except Exception as e:
        print('Error while running command')
        print(f'Error: {e}')

# Enter the base directory where the frontend and site folders are located
# Else input the base directory when running the script
# Example: C:\\Users\\User\Work\\project\\ui
BASE_DIR = ''

base_dir = BASE_DIR or input('Enter base directory: ')

# Enter the commands to run
# Example: (f'{base_dir}\\frontend', npm run dev)
commands = [
    (f'{base_dir}', 'echo "Hello World"'),
]

for directory, command in commands:
    print(f'Running command: {command} in directory: {directory}')
    run_command(directory, command)
    time.sleep(0.5)
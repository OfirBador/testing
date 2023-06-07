import subprocess
import os 

def install_requirements(requirements_file):
    try:
        subprocess.run(['python', '-m', 'pip', 'install', '-r', requirements_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing requirements from {requirements_file}: {e}")
        
        
def run_script(script_name, script_args):
    try:
        command = ['python', script_name] + script_args
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")


def check_message_to_trigger_script(automation_list_insert):
    with open('OEC/log_message.txt', 'r') as file:
        content = file.read()
    for name_and_script in automation_list_insert:
        if name_and_script[0] in content:
            install_requirements(name_and_script[2])
            run_script(f'OEC/{name_and_script[1]}',name_and_script[3])


def main():
    secret_value1 = os.environ.get('SECRET_VALUE_1')
    secret_value2 = os.environ.get('SECRET_VALUE_2')

    automation_list = [['test1', 'test1.py', 'OEC/requirements.txt', [secret_value1, secret_value2]],
                   ['test2', 'test2.py', 'OEC/requirements.txt', [secret_value1, secret_value2]]]
    
    check_message_to_trigger_script(automation_list)


if __name__ == '__main__':
    main()

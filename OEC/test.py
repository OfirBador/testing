import subprocess
import os 

secret_value1 = os.environ.get('SECRET_VALUE_1')
secret_value2 = os.environ.get('SECRET_VALUE_2')

automation_list = [['test1', 'test1.py', [secret_value1]],
                   ['test2', 'test2.py', [secret_value1, secret_value2]]]


def run_script(script_name, secret_list):
    try:
        subprocess.run(['python', script_name, secret_list], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")


def check_message_to_trigger_script(automation_list_insert):
    with open('OEC/log_message.txt', 'r') as file:
        content = file.read()
    for name_and_script in automation_list_insert:
        if name_and_script[0] in content:
            run_script(f'OEC/{name_and_script[1]}',name_and_script[2])


def main():
    check_message_to_trigger_script(automation_list)


if __name__ == '__main__':
    main()

import subprocess

automation_list = [['Yondu dead pods successfully removed', 'script1.py'],
                   ['another alert', 'script2.py']]


def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")


def check_message_to_trigger_script(automation_list_insert):
    with open('OEC/log_message.txt', 'r') as file:
        content = file.read()
    for name_and_script in automation_list_insert:
        if name_and_script[0] in content:
            run_script(f'Automation_Scripts/{name_and_script[1]}')


def main():
    check_message_to_trigger_script(automation_list)


if __name__ == '__main__':
    main()

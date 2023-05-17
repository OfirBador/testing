import subprocess

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

def main():
    with open('file.txt', 'r') as file:
        content = file.read()
    
    if 'name1' in content:
        run_script('code1.py')
    
    if 'name2' in content:
        run_script('code2.py')

if __name__ == '__main__':
    main()

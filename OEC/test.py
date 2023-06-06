import os
import subprocess

print("in script 1")
secret_value = os.environ.get('SECRET_VALUE')

if secret_value:
    subprocess.run(['python', 'OEC/test2.py', secret_value])
else:
    print("Secret not found or not set.")
print("out script 1")

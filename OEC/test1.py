import os
import subprocess

print("in script 1")
secret_value1 = os.environ.get('SECRET_VALUE1')
secret_value2 = os.environ.get('SECRET_VALUE2')
if secret_value1 and secret_value2:
    subprocess.run(['python', 'OEC/test2.py', secret_value1, secret_value2])
else:
    print("Secret not found or not set.")
print("out script 1")

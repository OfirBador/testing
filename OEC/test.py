import os

my_secret = os.environ.get('TEST')

if my_secret:
    print(f"The secret value is: {my_secret}")
else:
    print("Secret not found.")

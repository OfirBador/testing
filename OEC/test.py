import os

secret_value = os.environ.get('TEST')

if secret_value:
    print("Secret value:", secret_value)
else:
    print("Secret not found or not set.")

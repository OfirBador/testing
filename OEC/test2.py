import sys

print("in script 2")
if len(sys.argv) > 2:
    secret_value1 = sys.argv[1]
    secret_value2 = sys.argv[2]
    print("Secret value:", secret_value)
else:
    print("Secret not provided.")
    
if secret_value1 == '1234':
    print("secret 1 ok")
if secret_value2 == '5678':
    print("secret 2 ok")
    
print("out script 2")

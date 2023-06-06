import sys

print("in script 2")
if len(sys.argv) > 1:
    secret_value = sys.argv[1]
    print("Secret value:", secret_value)
else:
    print("Secret not provided.")
print("out script 2")

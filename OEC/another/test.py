import sys
import os 


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
function_dir = os.path.join(parent_dir, 'function')
sys.path.append(function_dir)
import fun


def main():
    fun.fun1()


if __name__ == '__main__':
    main()

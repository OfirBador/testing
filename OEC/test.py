import sys
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from function.fun import *

def main():
    fun1()


if __name__ == '__main__':
    main()

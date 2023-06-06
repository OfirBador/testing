import os
import argparse

def get_cli_args():
    """
    Get command line arguments
    :return: command line argument object
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--test', required=True, dest='test', help='test'
    )
    return parser.parse_args()

def print_secret(secret1):
    try:
        print(secret1)
    except:
        print("no secert")
    
def main():
    args = get_cli_args()
    print_secret(args.test)

if __name__ == '__main__':
    main()

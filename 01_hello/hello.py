#!/Users/yida.wang/miniconda3/envs/py39/bin/python3
"""
Author:  Yida Wang <yidaalex.wang@gmail.com>
Purpose: Say hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    args = parser.parse_args()
    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : Yida Wang <yidaalex.wang@gmail.com>
Date   : 2021-07-02
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    to_sort = args.sorted

    num = len(items)

    if to_sort:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = items[0] + ' and ' + items[1]
    else:
        bringing = ', '.join(items[:-1]) + ', and ' + items[-1]

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()

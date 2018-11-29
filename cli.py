#!/usr/bin/python3

import readline

def setup_cli():
    readline.parse_and_bind('tab: complete')

if __name__ == '__main__':
    setup_cli()

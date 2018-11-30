#!/usr/bin/python3

import argparse
import readline
import shlex

class InputManager:
    def __init__(self):
        self._parser = None
        self._running = False

    def _create_parser(self):
        self._parser = argparse.ArgumentParser()
        subparsers = self._parser.add_subparsers()
        connect_parser = subparsers.add_parser('connect', help='connect to server')
        connect_parser.set_defaults(func=connect_to_server)
        disconnect_parser = subparsers.add_parser('disconnect', help='disconnect from server')
        disconnect_parser.set_defaults(func=disconnect_from_server)
        exit_parser = subparsers.add_parser('exit', help='exit CLI')
        exit_parser.set_defaults(func=exit_cli)

    def run(self):
        while self._running:
            command = input('cli> ')
            args = self._parser.parse_args(shlex.split(command))
            args = vars(args)
            args['func'](args)

    def setup(self):
        readline.parse_and_bind('tab: complete')
        self._create_parser()
        self._running = True

    def stop(self):
        print('Stopping CLI')
        self._running = False

input_manager = InputManager()

def exit_cli(args):
    input_manager.stop()

def connect_to_server(args):
    print('Connecting to server')

def disconnect_from_server(args):
    print('Disconnecting from server')

if __name__ == '__main__':
    input_manager.setup()
    input_manager.run()

#!/usr/bin/python3

import argparse
import readline

class InputManager:
    def __init__(self):
        self._parser = None
        self._running = False

    def _create_parser(self):
        self._parser = argparse.ArgumentParser()
        subparsers = self._parser.add_subparsers()
        connect_parser = subparsers.add_parser('connect', help='connect to server')
        disconnect_parser = subparsers.add_parser('disconnect', help='disconnect from server')
        exit_parser = subparsers.add_parser('exit', help='exit CLI')
        exit_parser.set_defaults(func=self._stop_cli)

    def _stop_cli(self):
        print('Stopping CLI')
        self._running = False

    def run(self):
        command = input('cli> ')
        print('Processing command: %s' % (command))
        args = self._parser.parse_args(command)
        print(args)

    def setup_cli(self):
        readline.parse_and_bind('tab: complete')
        self._create_parser()
        self._running = True

if __name__ == '__main__':
    input_manager = InputManager()
    input_manager.setup_cli()
    input_manager.run()

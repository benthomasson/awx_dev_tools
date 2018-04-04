#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    get_message_types [options]

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import yaml

logger = logging.getLogger('get_message_types')


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    with open('designs/messages.yml') as f:
        data = yaml.load(f.read())
    
    print (" / ".join(["'{0}'".format(x['msg_type']) for x in data['messages']]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


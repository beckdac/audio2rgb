#!/usr/bin/env python

# system imports
import argparse

# local/app imports
from audio2rgb import Audio2RGB

# setup the argument parser
parser = argparse.ArgumentParser(description='audio2rgb CLI')
parser.add_argument('filename', help='filename of audio input')
parser.add_argument("--verbose", help="enable verbose mode",
                            action="store_true")
parser.add_argument("--debug", help="enable debug mode",
                            action="store_true")

# parser engage!
args = parser.parse_args()

# handle any CLI argument preprocessing
if args.verbose:
    print("verbose mode enabled")


# main
Audio2RGB(args.filename, args.verbose, args.debug)


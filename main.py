#!/usr/bin/env python

# system imports
import argparse

# local/app imports
import audio2rgb

# setup the argument parser
parser = argparse.ArgumentParser(description='audio2rgb CLI')
parser.add_argument('input', help='filename of audio input')
parser.add_argument("--verbose", help="enable verbose mode",
                            action="store_true")
# parser engage!
args = parser.parse_args()

# handle any CLI argument preprocessing
if (args.verbose):
    print("verbose mode enabled")

# main


# postprocessing

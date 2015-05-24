#!/usr/bin/env python

# system imports
import os
import argparse
import tempfile

# local/app imports
import audio2rgb

# setup the argument parser
parser = argparse.ArgumentParser(description='audio2rgb CLI')
parser.add_argument('input', help='filename of audio input')
parser.add_argument("--verbose", help="enable verbose mode",
                            action="store_true")
parser.add_argument("--debug", help="enable debug mode",
                            action="store_true")

# parser engage!
args = parser.parse_args()

# prepare environment

# create temporary files
tmpfp = tempfile.NamedTemporaryFile(delete=False)
if args.debug:
    print("tmp file: " + tmpfp.name)

# handle any CLI argument preprocessing
if args.verbose:
    print("verbose mode enabled")


# main


# postprocessing
# close and remove the tmp file
tmpfp.close()
if not args.debug:
    os.unlink(tmpfp.name)

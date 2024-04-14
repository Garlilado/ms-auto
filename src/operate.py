from player import *
from globals import DEVICES
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--join", help="Only join the room, internal use only")
parser.add_argument("--pass-stage", help="Pass the stage, internal use only")
args = parser.parse_args()

# Only join the room
if args.join:
    acc = Account(DEVICES[args.join])
    acc.join()
elif args.pass_stage:
    acc = Account(DEVICES[args.pass_stage])
    acc.pass_level()

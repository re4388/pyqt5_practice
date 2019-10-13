# https://docs.python.org/zh-tw/3/howto/argparse.html

import argparse

# create parser obj
parser = argparse.ArgumentParser()

# add arg
parser.add_argument("square", 
                    help="display a square of a given number",
                    type=int)

parser.add_argument("--verbosity", 
                    help="increase output verbosity")


# use parser to add new arg
args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")



# implement
print(args.square**2)

"""

 How to parse arguments from CLI (command line interface)

"""
import sys
from argparse import ArgumentParser

"""
if len(sys.argv)<2:
    times = 3
else:
    times = int(sys.argv[1])

for i in range(times):
    print("Hello world!")
"""

parser = ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="shows outputs")
parser.add_argument("-n", "--name", required=True, help="file name", metavar="FILE")
parser.add_argument("-d", type=int, help="digits precision", default=2, metavar=2 )
parser.add_argument("-f", "--folder", help="folder or folders", nargs="+", default=".", metavar="c:/tmp/")
parser.add_argument("-t", "--time", type=float, default=10.0, help="time delay", metavar="deltatime")

arguments = parser.parse_args()
print(f"Name = {arguments.name}")
print(f"Digits precision = {arguments.d}")
print(f"Verbose = {arguments.verbose}")
print(f"Folder/s = {arguments.folder}")
print(f"Time delay = {arguments.time}")


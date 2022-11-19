import argparse

parser = argparse.ArgumentParser(description='find the file')
parser.add_argument('path', metavar= 'path', type= str, help= 'eneter you file path: ')
parser.add_argument('fileName', metavar= 'fileName', type= str, help= 'eneter you file name: ')
args = parser.parse_args()

path = args.path
fileName = args.fileName

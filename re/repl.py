#!/user/bin/env python

# This script runs through the replacement patterns 
# in patterns.yaml and replaces them in the text file provided

import argparse
from pprint import pprint
import os
import re
import yaml

# Settings
verbose = False  # for debugging


def main(args):
  '''Reads the input yaml patters file and performs replacements
  '''
  patterns=yaml.load(args.yaml_patterns,Loader=yaml.BaseLoader) # read everything as text
  # make the list of questions = get rid of the root node if it exists
  if not isinstance(patterns,list):
    keys = list(patterns.keys())
    patterns = patterns[keys[0]]
    RuntimeWarning('The yaml file does not require top level node, should just be a list of patters')
  if verbose:
    print(f'Imported {len(patterns)} patterns file as list/dictionary:')
    pprint(patterns)

  # read the whole text file into a string
  content = args.text_file.read()
  # (---(?:\s|\S)*?---)\n((?:\s|\S)*)
  regexp = re.match(r"(?P<preamble>---(?:\s|\S)*?---)\n(?P<body>(?:\s|\S)*)", content)
  if regexp:
    redict = regexp.groupdict()
    preamble = redict['preamble']
    body = redict['body']
  else:
    preamble = ''
    body = content
  for p in patterns:
    pt = p['pattern']['re'].strip() # remove trailing and leading spaces
    st = p['pattern']['st'].strip()
    if verbose:
      pprint(f"Applying pattern {pt} --> {st}")
    body = re.sub(pt,st,body)
    # run space reducing pattern after each replacement
    body = re.sub(r'(?<![\n ])[ ]{2,}(?![ #])',r' ',body) # replace multiple spaces not at the beginning of line and not followed by # (comment)
    body = re.sub(r'(?m)\n\n\n',r'\n\n',body) # remove double empty lines
  args.text_file.close() # in case we are replacing
  with open(args.outfile, 'w') as file:
    file.write(preamble + '\n' + body)
  print(f'{len(patterns)} patterns applied successfully to {args.text_file.name}, results saved to {args.outfile}')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Apply a series of regexp patterns given in a YAML file to a give text file. See the code for details.")
  parser.add_argument('yaml_patterns', type=argparse.FileType('r'), help="Path to the yaml file with replacement patters. See examples in the code for the format.")
  parser.add_argument('text_file', type=argparse.FileType('r'), help="Path to the text/markdown file with text for replacements")
  parser.add_argument('-o', '--outfile', help="Output file name, optional. When not given, the input text file is overwritten",required=False,default='overwrite')
  args = parser.parse_args()
  # set output file name to match the input by default
  if args.outfile == 'overwrite':
    args.outfile = args.text_file.name
  main(args)

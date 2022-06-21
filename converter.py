"""
converter.py - A Pandoc script to convert .docx files to .md

Script requires Pandoc installtion. "brew install pandoc" on MacOS


Author: Matthew Sunner, 2022
"""

from asyncio import subprocess
import sys
from pathlib import Path
import os
import getopt
import subprocess


def docx_file_finder():
    """docx_file_finder - Function to locate and return the .docx file added to the foler

    Returns:
        obj: object with .docx relative file path included
    """

    doc_files = []

    for file in os.listdir('./data'):
        if file.endswith('.docx'):
            doc_files.append(file)

    if len(doc_files) != 1:
        return 'Error'
    else:
        return doc_files


def command_runner(input_file_name):
    """command_runner - Function to run bash command for Pandoc file translation

    Args:
        input_file_name (str): file name for the .docx input file
    """

    input_name = input_file_name
    parser = 'gfm' # input('Please Enter a Parser: (gfm): ')
    output_name = input_file_name.split('.')[0] + '.md'

    # bash_command = f'pandoc -t {parser} --extract-media . -o {output_name} {input_name}'
    bash_command = ['pandoc', '-t', parser, '--extract-media','.', '-o', output_name, input_name]
    
    subprocess.run(bash_command)


# Application Loop
if __name__ == '__main__':
    doc_name = docx_file_finder()[0]

    command_runner(doc_name)
    
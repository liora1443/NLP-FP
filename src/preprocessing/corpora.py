# coding: utf-8
"""
corpora python script convert large data of corpus files to one corpus

Input: the folder with the text files
Output: one file with the corpus

"""
import xml.etree.ElementTree as ET
import sys
import re
import os


def match_word(strg, search=re.compile(r'[^a-z]').search):
    return not bool(search(strg))


def parse(file_input_name):
    tree = ET.parse(file_input_name)
    root = tree.getroot()
    text = ''
    for sentence in root.iter('sentence'):
        for line in sentence.iter('token'):
            heb_word = line.attrib['transliterated']
            if match_word(heb_word):
                text += heb_word + ' '
        text += '\n'
    return text


def list_files(root_dir):
    file_set = set()
    for dir_, _, files in os.walk(root_dir):
        for fileName in files:
            if fileName.endswith('.xml'):
                # if fileName.endswith('.txt'):
                relDir = os.path.relpath(dir_, root_dir)
                relFile = os.path.join(relDir, fileName)
                file_set.add(relFile)
    return file_set


def parse_from_folders(path):
    dir_counter = 1
    # Loop all folders of corpus
    while dir_counter < 44:
        dir_ = path + '\\' + str(dir_counter)
        dir_counter += 1

        # Build 1 parsed text file from the entire director
        text = ''
        files = list_files(dir_)
        for text_file in files:
            text += parse(dir_ + '\\' + text_file)
            # Write the file of the directory
        output_file = open(dir_ + 'corpus.txt', 'w')
        output_file.write(text.encode('utf8'))
        output_file.close()


def combine_text_file(path):
    file_set = list_files(path)
    text = ''
    for file_ in file_set:
        opened_file = open(path + file_, 'r')
        text += opened_file.read()
        opened_file.close()
    output_file = open('test.txt', 'w')
    output_file.write(text.encode('utf8'))
    output_file.close()

if __name__ == '__main__':
    path = sys.argv[1]
    # parse_from_folders(path)
    # combine_text_file(path)

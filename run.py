import os
import sys
import argparse
from resparser.resume_parser import ResumeParser
def __init__(self):
    self.__parser = argparse.ArgumentParser()
    self.__parser.add_argument(
            '-f',
            '--file',
            help="resume file to be extracted",
            required=True)
        
def index(file):
    #filePath = os.path.join(os.getcwd(), 'resumes/resume.pdf')
    resume_parser = ResumeParser(file)
    print(resume_parser.get_extracted_data())
    #return [resume_parser.get_extracted_data()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-f',
            '--file',
            help="resume file to be extracted",
            required=True)
    args = parser.parse_args()
    index(args.file)
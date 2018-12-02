#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:34:03 2018

@author: bpiwowar
"""

import sys
import os
import csv


# Relative path to folder containing raw files
# This can be used instead of passing an argument to the script
FOLDER_PATH = "SubjectData25Nov"


# return a list of files contained in a folder
# path: relative path to folder from the program
def get_files(path):
    
    trial_files = os.listdir(path)

    return trial_files



# main function to reformat all files contanined the files list
# list: list of files
def covert_files(files,raw_folder):
    
    #name of the new folder that will contain formatted files
    new_folder = "new_{0}".format(raw_folder)
      
    #check if folder exists, otherwise create new one
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        print("Created new folder for formatted files: {}".format(new_folder))
    
       
    # tries to format each file and save it into new_folder
    for f in files:
        reformat_file(f,raw_folder,new_folder)
        
    return
        
# reformas a text file to proper csv format with ',' as delimiter   
# saves each new file into new_folder     
def reformat_file(file,raw_folder,new_folder):
    
    print("Starting to format: {}".format(file))
    
    # First we open original files as csv with a space delimiter
    with open("{0}/{1}".format(raw_folder,file)) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=' ')
        
        # Second we open a new file to write as csv format with ',' delimeter
        with open("{0}/{1}.csv".format(new_folder,file), mode='w') as formated_file:
            file_writer = csv.writer(formated_file, delimiter=',')
                   
            # for each line/row in the orginal file we writ eto new file
            # Here we elimanate extra spaces so everything aligns
            for row in csv_reader:
                # here we reduce the number of spaces in the orignal file
                # they written as '' values in the list
                reduced_row = [x for x in row if x != '']

                # writes a new row to the new file
                file_writer.writerow(reduced_row)
            
    return


if __name__ == '__main__':
    
    
    # check if folder path of raw files has been passed as an argument
    if len(sys.argv) > 1:
        
        print(sys.argv[1])
        raw_folder = sys.argv[1]
    else:
        # otherwise use static folder path instead
        raw_folder = FOLDER_PATH   
    
    
    # get list of raw files
    files = get_files(raw_folder)
    
    #reformat and save new files
    covert_files(files,raw_folder)

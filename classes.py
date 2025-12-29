# Final Subtraction Program
# Date Created: 11/2/2023
# Author:Celia Mercier, Danielle Alverson

import csv
import pandas as pd
import matplotlib.pyplot as plt

class Subtract_Save:
    def __init__(self, total_signalfile_path, substrate_filepath):
        self.file_path = file_path
        self.total_signalfile_path = total_signalfile_path
        self.substrate_filepath = substrate_filepath
    
    def parse_file(self, file_path):
        """This serves as a helper function to the main subtraction function by "cleaning" up the data
        and removing the explanations at the start to get the numbers alone"""
        data = {}
        with open(file_path, 'r') as file:
            for line in file:
                # Removes lines starting with '#'
                if not line.startswith('#'):
                    values = line.strip().split()
                    # Converts string in .txt to float
                    x = float(values[0])
                    y = float(values[1])
                    

                    data[x] = y
        return data
    
    def subtract_and_store(total_signalfile_path, substrate_filepath):
        """This takes in text files containing coordinates of the integrations and subtracts the substrate from 
        the total signal. While subtracting it is keeping track of the smallest distance in between two points and
        and when it finishes parsing this process, it goes through the dictionary containg the subtracted values and 
        subracts the minumum value found, bring it as close to zero as possible """
        # Gets data from inputs
        data1 = parse_file(total_signalfile_path)
        data2 = parse_file(substrate_filepath)
        # Arbitrarily large number
        min_val = 1000

        result_dict = {}
        # Goes through x,y coordinates for total signal and finds matching x in substrate
        for x, y1 in data1.items():
            if x in data2:
                y2 = data2[x]
                #Subtracts y value of subtrate from total signal
                result_value = y1 - y2
                result_dict[x] = result_value

                if result_value < min_val and result_value != 0:
                    min_val = result_value
                    
        return result_dict

def save_data(path, result_dict):
    """A function to save the data as a csv by taking in the output of subtract_and_store"""
    final_sub_path = path
    # Opens csv file to place values in
    with open(final_sub_path, mode = 'w', newline = '' ) as file:
        # Space as delimiter
        writer = csv.writer(file, delimiter = ' ')
        for x in result_dict:
            # Subtracts by smallest space
            if result_dict[x] >= min_val:
                result_dict[x] = result_dict[x] - min_val
                writer.writerow([x, result_dict[x]])


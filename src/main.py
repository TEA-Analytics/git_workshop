"""
A script with a lot of mistakes. Add or change whatever you want. 

    @Author: Eina Ooka, your name? 
    @Date: what date is today anyway? 
"""

import pyutilitea as tea
import csv
from utils import calculate_average, group_by_column

def load_csv(filepath): # logging
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

def main():
    tea.log("Starting data analysis...")  

    data = load_csv("data/sample_data.csv")

    # Calculate avg of colum
    avg = calculate_average(data, "value")
    formatted_avg = tea.format_number(avrg)  
    print(f"Average Value: {formatted_avg}")

    # Group by "category"
    grouped = group_by_column(data, "catgory")

    for key, items in grouped.items():
        print(f"\nGroup: {key}")
        for row in items:
            print(f"  {row['name']} ({row['value']})")

    tea.log("Analysis completed.")  

if __name__ == "__main__":
    mian()
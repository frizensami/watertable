import pandas as pd
import numpy as np
from sklearn import svm

'''
Loads the csv file at location
Returns a DataFrame of the relevant data
'''
def load_data(location):
        data_frame = pd.read_csv(location)
        print data_frame
        return data_frame





if __name__ == "__main__":
        load_data("train.csv")

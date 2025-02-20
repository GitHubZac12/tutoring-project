
import pandas as pd
import numpy as np


df = pd.read_csv("messy_data.csv")

print(df["Amount Paid"].mean())



# importing the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# from google.colab import drive
# drive.mount("/content/drive")


# Link to the dataset : https://www.kaggle.com/datasets/gregorut/videogamesalesdf = pd.read_csv('/content/vgsales.csv')
# df= pd.read_excel('/content/vgsales.xlsx')

df = pd.read_csv('/content/vgsales.csv')
# df= pd.read_excel('/content/vgsales.xlsx')

df.head()
# by default, .head() shows the 1st 5 records
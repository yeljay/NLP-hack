import pandas as pd
import os
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

os.chdir("C:\\Users\\Lakshmi Jagannathan\\OneDrive - Elastacloud Limited\\GitHub repo\\NLP-hack\\Data\\Genre analysis")
os.getcwd()

movieDF = pd.read_csv('MovieGenre.csv')
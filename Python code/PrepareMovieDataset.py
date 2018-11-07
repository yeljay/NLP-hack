import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


os.chdir("C:\\Users\\Lakshmi Jagannathan\\OneDrive - Elastacloud Limited\\GitHub repo\\NLP-hack\\Data\\Genre analysis")
os.getcwd()

summary_header = ['WikiID','Plot']
summary = pd.read_csv('plot_summaries.txt',sep='\t',header=None,names=summary_header)
summary.info()
summary.head()

moviedata_header = ['WikiID','FreebaseID','Name','Release Date','revenue','runtime','lang','country','genre']
moviedata = pd.read_csv('movie.metadata.tsv',sep='\t',header=None,names=moviedata_header)
moviedata.info()
moviedata.loc[moviedata['WikiID']==23890098]
moviedata_subset = moviedata.loc[:,['WikiID','Name','genre']]
moviedata_subset.info()

summaryNew = pd.merge(summary,moviedata_subset,on='WikiID',how='left')
summaryNew.info()

###removing entries where there is no genre in the movie database
summaryNew = summaryNew.loc[summaryNew['Name'].isnull() == False]
summaryNew.to_csv('MovieGenre.csv')
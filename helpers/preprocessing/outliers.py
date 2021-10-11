# Imports 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
def boxplot_numeric_features(X,
                             rows_for_plot,
                             cols_for_plot):
    
    num_features = X.select_dtypes(include=['int64', 'float64']) \
                    .columns \
                    .tolist()
    
    plt.figure(figsize=(16,10))

    for i,col in enumerate(num_features):    
        plt.subplot(rows_for_plot,cols_for_plot,i + 1)
        sns.boxplot(y=col, data=X)
        #plt.ylabel('')

    plt.tight_layout()

    plt.show()
    
#    
def IQR_Outliers(X):
    
    num_features = X.select_dtypes(include=['int64', 'float64']) \
                    .columns \
                    .tolist()

    print('# of numeric features: ', len(num_features))
    print('Numeric Features: ', num_features)

    indices = [x for x in X.index]
    #print(indices)
    print('Number of samples: ', len(indices))
    
    out_indexlist = []
        
    for col in num_features:
       
        #Using nanpercentile instead of percentile because of nan values
        Q1 = np.nanpercentile(X[col], 25.)
        Q3 = np.nanpercentile(X[col], 75.)
        
        cut_off = (Q3 - Q1) * 1.5
        upper, lower = Q3 + cut_off, Q1 - cut_off
        print ('\nFeature: ', col)
        print ('Upper and Lower limits: ', upper, lower)
                
        outliers_index = X[col][(X[col] < lower) | (X[col] > upper)].index.tolist()
        outliers = X[col][(X[col] < lower) | (X[col] > upper)].values
        print('Number of outliers: ', len(outliers))
        print('Outliers Index: ', outliers_index)
        print('Outliers: ', outliers)
        
        out_indexlist.extend(outliers_index)
        
    #using set to remove duplicates
    out_indexlist = list(set(out_indexlist))
    out_indexlist.sort()
    print('\nNumber of rows with outliers: ', len(out_indexlist), "out of", len(X))
    print('List of rows with outliers: ', out_indexlist)
    
#    
def CustomSampler_IQR(X,
                      y):
    
    num_features = X.select_dtypes(include=['int64', 'float64']).columns
    df = X.copy()
    df['Outcome'] = y
    
    indices = [x for x in df.index]    
    out_indexlist = []
        
    for col in num_features:
       
        #Using nanpercentile instead of percentile because of nan values
        Q1 = np.nanpercentile(df[col], 25.)
        Q3 = np.nanpercentile(df[col], 75.)
        
        cut_off = (Q3 - Q1) * 1.5
        upper, lower = Q3 + cut_off, Q1 - cut_off
                
        outliers_index = df[col][(df[col] < lower) | (df[col] > upper)].index.tolist()
        outliers = df[col][(df[col] < lower) | (df[col] > upper)].values        
        out_indexlist.extend(outliers_index)
        
    #using set to remove duplicates
    out_indexlist = list(set(out_indexlist))
    
    clean_data = np.setdiff1d(indices,out_indexlist)

    return X.loc[clean_data], y.loc[clean_data]
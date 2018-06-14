
# Building a Neural Network in Python
# https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/

# Role of Bias in Neural Networks
# https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks

# How can I interpret Sklearn confusion matrix
# https://stats.stackexchange.com/questions/95209/how-can-i-interpret-sklearn-confusion-matrix

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import itertools

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier    # MLPClassifier: Multi-Layer Perceptron Classifier model
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def main():
#     GET DATA
#     df_wine = pd.read_csv('wine_data.csv', names=["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", 
#                                                  "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
    
    df_wine = pd.read_csv(filepath_or_buffer='train_wine_data.csv')
#     print(df_wine)
#     print()
    
#         -------------------------------------------------------------------------------------
#     print("PRINT 5 FIRST ROWS:") 
#     print(df_wine.head())
#     print()
#     
#     print("PRINT SUMMARY STATS:") 
#     print(df_wine.describe())
# #     print(df_wine.describe().transpose())
#     print()
#         
#     print("PRINT NUMBER OF ROWS AND COLUMNS:")
#     print(df_wine.shape)
#     print()

#     corrmat = df_wine.corr()
#     print(corrmat)
#     print()
#     -------------------------------------------------------------------------------------
        
#     labels or features  (X - upper case as a vector)
    X = df_wine.drop(labels="cultivator", axis=1)
    print(X)
    print()
    
#     get list features name
    X_feature_name = X.columns.tolist()        
    print("X FEATURES NAME")
    print(X_feature_name)
    print()
    
#    target
    y = df_wine["cultivator"]
    print(y)
    print()
    
#     get  list y unique class names
    y_unique_class = list(y.unique())
    print("Y UNIQUE CLASS")
    print(y_unique_class)
    print()
    
#     Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)
    
#     X_train.to_csv("wine_data_x_train.csv")   
#     print(X_train.shape)
#     
#     X_test.to_csv("wine_data_x_test.csv")   
#     print(X_test.shape)
#     
#     y_train.to_csv("wine_data_y_train.csv")   
#     print(y_train.shape)
#       
#     y_test.to_csv("wine_data_y_test.csv")   
#     print(y_test.shape)
     
#     DATA PREPROCESSING
#     this should be StandardScaler(copy=True, with_mean=True, with_std=True)
    scaler = StandardScaler()
    
#     print(scaler) # will print: StandardScaler(copy=True, with_mean=True, with_std=True)
    
#     Fit only to the training data
    scaler.fit(X_train)
    
#     Now apply the transformations to the data:
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    
    print("X TRAIN SCALED")
    print(X_train)
    print()
    
    print("X TEST SCALED")
    print(X_test)
    print()
    
    
#     TRAINING THE MODEL
    mlp_model = MLPClassifier(hidden_layer_sizes=(20, 20, 20, 20), max_iter=1000)
    
#     fit the training data to our mode/
    mlp_model.fit(X_train, y_train)
    
#     Y PREDICTIONS 
#     get predictions
    y_predicted = mlp_model.predict(X_test)
    print("Y PREDICTED")
    print(y_predicted)
    print()
    
#     MODEL EVALUATION    
    confusion_matrix_result = confusion_matrix(y_test, y_predicted)
#     plot confusion matrix
    plot_confusion_matrix(confusion_matrix_result, y_class=y_unique_class, plot_title="Confusion Matrix - Wine Data", plot_y_label="Test Wine Class", plot_x_label="Predicted Wine Class")      
#     print confusion matrix
    print(confusion_matrix_result)
    print()
    
    classification_report_result = classification_report(y_test, y_predicted)        
    print('CLASSIFICATION REPORT')
    print(classification_report_result)
    print()

    accuracy_score_value = accuracy_score(y_test, y_predicted) * 100
    accuracy_score_value = float("{0:.2f}".format(accuracy_score_value))
    print('ACCURACY SCORE')
    print( "{} %".format(accuracy_score_value))
    print()    
    
def plot_confusion_matrix(confusion_matrix, y_class, plot_title, plot_y_label, plot_x_label, normalize=False):
    """
    plot the confusion matrix.
    :param confusion_matrix: confusion matrix value
    :param y_class: target unique class name
    :param plot_title: plot title
    :param plot_y_label: plot y label
    :param plot_x_label: plot x label
    :param normalize: default to false
    :return: None
    """
    try:
        plt.figure()
        plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(plot_title)
        plt.colorbar()
        tick_marks = np.arange(len(y_class))
        plt.xticks(tick_marks, y_class, rotation=45)
        plt.yticks(tick_marks, y_class)
        if normalize:
            confusion_matrix = confusion_matrix.astype('float') / confusion_matrix.sum(axis=1)[:, np.newaxis]
            print("NORMALIZED CONFUSION MATRIX")
        else:
            print('CONFUSION MATRIX WITHOUT NORMALIZATION')    
        thresh = confusion_matrix.max() / 2.
        for i, j in itertools.product(range(confusion_matrix.shape[0]), range(confusion_matrix.shape[1])):
            plt.text(j, i, confusion_matrix[i, j],
                     horizontalalignment="center",
                     color="white" if confusion_matrix[i, j] > thresh else "black")
        plt.ylabel(plot_y_label)
        plt.xlabel(plot_x_label)
        plt.tight_layout()    
        plt.show()
    except Exception as ex:
        print( "An error occurred: {}".format(ex))   
                
#    FOR TESTING ONLY ------------------------------------------
#     y_true = [2, 0, 2, 2, 0, 1]
#     y_pred = [0, 0, 2, 2, 0, 2]
#     print(confusion_matrix(y_true, y_pred))
#     print()
#         
#     y_true = pd.Series(y_true)
#     y_pred = pd.Series(y_pred)
#     ds = pd.crosstab(y_true, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
#     print(ds)
#     print()
#     ---------------------------------------------------------------------------
    
# #     list of weight matrices - no meaning?
#     print(mlp.coefs_[0])
#     print()     
# #     list of bias vectors - no meaning?
#     print(mlp.intercepts_[0])
#     print()
    
    
if __name__ == '__main__':
    main()
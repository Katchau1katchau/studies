###################################################################################################
####################################### Logistic Regression #######################################
###################################################################################################
##################################### Run on Jupyter Notebook #####################################
###################################################################################################

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset, you can just substitute YOUR_DATE for your file's name,
# choose the interval of independent and dependent variables in your CSV file
# And finally run the code, change it on INDEPENDENT_VARIABLES_COLUMNS and
# DEPENDENT_VARIABLES_COLUMN.
dataset = pd.read_csv('YOUR_DATA.csv')
X = dataset.iloc[:, [INDEPENDENT_VARIABLES_COLUMNS]].values
y = dataset.iloc[:, DEPENDENT_VARIABLES_COLUMN].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred

# Checking the Hit Rate
L = []
oc = 0
for i in range(len(y_pred)):
	L.append([y_pred[i]])
for i in range(len(y_test)):
	L[i].append(y_test[i])
	if L[i][0] == L[i][1]:
	oc = oc+1
taxa = oc/(len(L))
print(taxa)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
					np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
					
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
			alpha = 0.75, cmap = ListedColormap(('red', 'green')))
			
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
	plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
				c = ListedColormap(('red', 'green'))(i), label = j)
				
plt.title('Logistic Regression (Training set)')
plt.xlabel('X_VARIABLES (INDEPENDENT VARIABLES)')
plt.ylabel('Y_VARIABLES (DEPENDENT VARIABLES)')
plt.legend()
plt.show()

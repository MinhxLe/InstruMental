
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=2)
print(X.shape)
X_r = pca.fit(X).transform(X)
print(X_r.shape)

lda = LinearDiscriminantAnalysis(n_components=2)
print(X.shape)
X_r2 = lda.fit(X, y).transform(X)
print(X_r2.shape)
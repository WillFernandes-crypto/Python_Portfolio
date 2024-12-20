import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn
from scikeras.wrappers import KerasClassifier 
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Dropout # type: ignore
from sklearn.model_selection import cross_val_score
from ucimlrepo import fetch_ucirepo

# Config. utilizada aumenta o tamanho dos neurônios nas camadas densas de 16 para 32, além do aumento do tamanho do batch_size, de 10 para 32

# fetch dataset
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)

# data (as pandas dataframes)
X = breast_cancer_wisconsin_diagnostic.data.features
y = breast_cancer_wisconsin_diagnostic.data.targets

# metadata
print(breast_cancer_wisconsin_diagnostic.metadata)

# variable information
print(breast_cancer_wisconsin_diagnostic.variables)

# Verificando os tipos de dados
print(X.dtypes)
print(y.dtypes)

# Converter 'Diagnosis' para valores numéricos
y = y['Diagnosis'].map({'M': 1, 'B': 0})

# Verificando se `y` foi convertido corretamente
print(y.head())
print(y.dtypes)

X = pd.DataFrame(X)
y = pd.DataFrame(y)

def criarRede():
    classificador = Sequential()
    classificador.add(Dense(units = 32, activation = 'relu', 
                        kernel_initializer = 'random_uniform', input_dim = 30))
    classificador.add(Dropout(0.3))
    classificador.add(Dense(units = 32, activation = 'relu', 
                        kernel_initializer = 'random_uniform'))
    classificador.add(Dropout(0.3))
    classificador.add(Dense(units = 1, activation = 'sigmoid'))
    otimizador = tf.keras.optimizers.Adam(learning_rate=0.001, decay=0.0001, clipvalue=0.5)
    classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])
    return classificador

classificador = KerasClassifier(model = criarRede, 
                                epochs = 500,
                                batch_size = 32)

resultados = cross_val_score(estimator = classificador,
                             X = X, y = y,
                             cv = 10, scoring = 'accuracy')
media = resultados.mean()
desvio = resultados.std()

print(f'Média: {media}')
print(f'Desvio padrão: {desvio}')

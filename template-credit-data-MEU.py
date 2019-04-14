import pandas as pd

base = pd.read_csv('credit-data.csv')
base.loc[base.age < 0, 'age'] = base.age[base.age > 0 ].mean();

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#importa o modulo que faz a separação de base de teste e treinamento
from sklearn.model_selection import train_test_split
#recebe os previsores, classes e test_size que separa quantos porcento via para teste
# se a base de dados for muito grande, usar 70% para traino e 30% para teste
previsores_train, previsores_teste, classe_train, classe_teste = train_test_split(previsores,classe,test_size=0.25,random_state=0)

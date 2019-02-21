#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:05:35 2019

@author: lauro
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder, StandardScaler

base = pd.read_csv('./census.csv')

#iloc(linhas,colunas)
#slecionando os previsores e a classe
previsores = base.iloc[:,:14].values
classes = base.iloc[:,14:].values

#importanto bibilhoteca de conversao de valores nominais.

labelencoder_previsores = LabelEncoder()
#workclass conversao
#conversao dos atributos que sao nominais
lista = [1,3,5,6,7,8,9,13]
for i in lista:
    previsores[:,i] = labelencoder_previsores.fit_transform(previsores[:,i])

#OneHotEncoder é uma for de trnasformar registros numericos em arrays de combinações
#podendo ser analisados sem perder o valor.

"""
    DUMMY VARIABLES
""" 
#corrrigindo um unico valor
races = base.iloc[:,8:9].values
onehotencoderRace = OneHotEncoder(categorical_features=[0])
races[:,0] = labelencoder_previsores.fit_transform(races[:,0])
races = onehotencoderRace.fit_transform(races).toarray()


#corrigindo previsores
onehotencoder = OneHotEncoder(categorical_features=lista)
previsores = onehotencoder.fit_transform(previsores).toarray()



#Convertendo a classe
labelencoder_classe = LabelEncoder()
classes = labelencoder_classe.fit_transform(classes)

#Escalonizando todos os valores.
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

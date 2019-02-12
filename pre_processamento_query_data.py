# -*- coding: utf-8 -*-
# python 3.6
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# == previsores
#id (nominal pois é unico) = id kkk
#income(continua) = salário
#age(continua) = idade 
#loan(continua)= emprestimo
# == classe
#default(meta(discreta)) = 0-naopaga ,1-paga 

import pandas as pd
import numpy as np
base = pd.read_csv('./credit-data.csv')

#DESCREVE ALGUMAS PROPRIEDADES
#como a media(mean)
#desvio padrao(std)
#minimo(min)
#maximo(max)
base.describe()

#tramaento de dados
# localizar valores
base.loc[base['age'] < 0]
# corrigindo valorees negativos.
# age - coluna , 1 -apagar a coluna toda, inplace - retorna a tabela com alterçaão
base.drop('age',1,inplace=True)
# apagar registros com problema
# padas pode ser acessado com base.age ou base['age']
var = base.drop(base[base.age < 0].index, inplace=False)

#----nao é bom fazer isso ^^

#Preencher registros manualmente, pesquisando os valores corretos de sua idade
# no caso , preencher os valores com as medias
#menor idade
base.age.min()
#meadia
base.mean() 
#media das idades
base.age.mean()
#media das idades maiores que 0
base['age'][base.age > 0].mean()
#atualizando valores, para manter concistencia dos dados
base.loc[base.age<0,'age'] = base['age'][base.age > 0].mean()


#verifiando  valores nulos
#nan = not a number

#proucurando os valores
pd.isnull(base.age)
base.loc[pd.isnull(base['age'])]


#campos ids não ajudam como previsores, podem ser retirados
#separado previsores das classes
# linhas, de qual linha ate qual,
# colunas de qual coluna ate qual.
#base.iloc[:10,1:4]

#.values , tira os titulos

previsores = base.iloc[:,1:4].values
classe = base.iloc[:,4].values

#imputer foi depreciado, usado para normalizar mts dados
from sklearn.preprocessing import Imputer
# oque ele vai proucurar(missing values)
# qual estrategia ele vai usar para substituir (strategy)
# axis , 0-coluna, 1-linha
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
#fit , seta a base de dados, os [] são para dizer qual parte da base
#vai ser trabalhada
imputer = imputer.fit(previsores[:,0:3])
#devolve para a variavel os dados corrigidos 
previsores[:,0:3] = imputer.transform(previsores[:,0:3])

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:05:46 2020

@author: Elodie NGANTCHOU KEMADJOU
"""

"""
Ecrire une ou plusieurs fonctions de test 
(eg utilisant https://docs.pytest.org/en/stable/) 
afin de tester la qualité de votre function.
"""

### Appel du programme detect_duplicates_func.py
import detect_duplicates_func


### Import dataset
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db', echo=False)
con = engine.connect()
df_patient = pd.read_sql('select * from patient', con=con)
df_pcr = pd.read_sql('select * from test', con=con)
con.close()

"""Cette fonction permet de vérifier si ma fonction detect_duplicates_func.py est bonne
En me basant sur le pourcentage, je vérifier si le pourcetage des données duplicaquées est de 100%
Si elle est égale 100% alors il n'y a pas de doublons
"""
def test_detect_duplicates():
    assert detect_duplicates_func.pourCentage(df_patient) == 100
    
 
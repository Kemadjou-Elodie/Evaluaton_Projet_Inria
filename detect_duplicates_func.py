# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:42:30 2020

@author: Elodie NGANTCHOU KEMADJOU
"""

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db', echo=False)
con = engine.connect()
df_patient = pd.read_sql('select * from patient', con=con)
df_pcr = pd.read_sql('select * from test', con=con)
con.close()

""" Ecrire une fonction Python detect_duplicates qui prend en parametère 
le dataframe df_patient et qui renvoit un nouveau dataframe après suppression 
des doublons. """

def detect_duplicates(df_patient):
    df_patient1 = df_patient.dropna()
    df_patient1 = df_patient1.drop_duplicates("patient_id",keep = "last")
    df_patient1 = df_patient1.drop_duplicates("phone_number", keep = "last")
    df_patient1[df_patient1.street_number >999]
    df_patient1 = df_patient1.reset_index(level=None, drop=True, inplace=False,col_level=0, col_fill='')
    return df_patient1

"""Vous estimerez le pourcentage de données dupliquées. Attention, 
les données dupliquées ne sont pas identiques. Il faut imaginer des problèmes 
de saisies de données (typos, information manquante etc.)"""

def pourCentage(df_patient):
    #df_patient.drop("date_of_birth", axis=1, inplace=True)
    #df_patient.drop("address_2", axis=1, inplace=True)
    df_patient2 = detect_duplicates(df_patient)
    pourcentage = 100-100*(len(df_patient2)/len(df_patient))
    return pourcentage

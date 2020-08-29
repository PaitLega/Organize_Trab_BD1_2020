# -*- coding: utf-8 -*-
"""Modelo_BD1_Item_91_Trabalho_Grupo_RafaelXavier_RitaGuimarães_LuizAmancio

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tUOGXht4dBU9PLaaLhd9p48wTsnSgoQS

# Importando bibliotecas e realizando configurações
"""

import psycopg2
import pandas as pd
conn = psycopg2.connect(host="ruby.db.elephantsql.com",database ="zbhwctjp",user ="zbhwctjp", password ="KpKFW6sP3irBObgJf_YJtiCTqyfd-VA2")

"""# Modelo Conceitual

<img src='https://github.com/RafaelXavierBraga/Organize_Trab_BD1_2020/blob/master/images/bd_modeloconceitual.png'/>

# 9.1 CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS(Todas)
"""

pd.read_sql_query("select * from pessoa",conn)

pd.read_sql_query("select * from endereco",conn)

pd.read_sql_query("select * from tipo",conn)

pd.read_sql_query("select * from transacao",conn)

pd.read_sql_query("select * from contato",conn)
#|/usr/bin/env python3


"""
Hello World Multi Linguas

Como usar:

Tenha a viarável LANG devidamente configurada ex:

     export LANG=pt_br

Execucao:
    
     python3 hello.py
      ou
     ./hello.py

"""


# Este programa imprime Hello World


__version__ = "0.0.1"
__author__ = "Fran Rocha"
__license__ = "Unlicense"

import os #Biblioteca externa

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_br":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"


            



print(msg)  #built-in

"""
Dieses Beispiel stammt aus dem Buch "Python for Finance - Second Edition" von Yuxing Yan: https://www.packtpub.com/big-data-and-business-intelligence/python-finance-second-edition
Sämtliche Beispiele sind in leicht abgewandeltet Form zu finden unter: https://github.com/PacktPublishing/Python-for-Finance-Second-Edition

MIT License
Copyright (c) 2017 Packt
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def alternative_smile():
    # Datensatz einlesen
    data2 = pd.read_csv('calls17march.txt', # Datensatz
                        delimiter='\t', # Seperator 
                        skiprows=1, # Überspringe die erste Zeile
                        usecols=['Strike','Implied Volatility']) # Auswahl der einzulesenden Spalten

    x = data2['Strike'] # Speichere die eingelesenen Daten aus der Spalte 'Strike' als die Variable x
    y0 = data2['Implied Volatility'] # Überführe die eingelesenen Daten aus der Spalte 'Implied Volatility' in eine Liste
    n = len(y0) # Bestimme die länge der Liste y0 und speichere diese als die Variable n
    y = [] # Lege die leere Liste y an

    # Führe die folgende Operation n mal durch
    for i in np.arange(n):
        a = float(y0[i].replace("%","")) / 100.0 # Entferne für jedes Element in der Liste y0 das Prozentzeichen und teile den Wert durch 100
        y.append(a) # Füge den modifizierten Wert der Liste y an
        
    plt.title('Volatility smile - IBM Calls mit Fälligkeit: 3/17/2017') # Titel der Grafik
    plt.ylabel('Volatilität') # Beschriftung Y-Achse
    plt.xlabel('Preis des Strikes') # Beschriftung X-Achse
    plt.plot(x,y,'o') # Plotten der Datenpunkte
    plt.grid() # Gitternetz
    plt.show() # Funktion zum anzeigen der Grafik

alternative_smile()

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
    data2 = pd.read_csv('calls17march.txt',
                        delimiter='\t',
                        skiprows=1,
                        usecols=['Strike','Implied Volatility'])

    x = data2['Strike']
    y0 = data2['Implied Volatility']
    n = len(y0)
    y = []

    for i in np.arange(n):
        a = float(y0[i].replace("%","")) / 100.0
        y.append(a)
        
    plt.title('Volatility smile - IBM Calls mit Fälligkeit: 3/17/2017')
    plt.ylabel('Volatilität')
    plt.xlabel('Preis des Strikes')
    plt.plot(x,y,'o')
    plt.grid()
    plt.show()

alternative_smile()

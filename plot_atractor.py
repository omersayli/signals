#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:30:00 2020

@author: omer
"""


import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np

# Set white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

 
app = QApplication(sys.argv)
 
 
pg.plot(x[boolean_],y[boolean_], pen=None, symbol='0', size=0.1)
 
status = app.exec_()
sys.exit(status)

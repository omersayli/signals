#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:29:39 2020

@author: omer
"""
# Inspired by
# https://danielredondo.com/posts/20190210_atractor/

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import time

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        import numpy as np
        
        M = 10000000
        x = np.zeros(M)
        y = np.zeros(M)
        x[0], y[0] = 1 , 1
        a1= -0.8; a2= 0.4; a3 = -1.1; a4 = 0.5; a5 = -0.6; a6= -0.1; a7 = -0.5;
        a8 = 0.8; a9 = 1.0; a10 = -0.3; a11 = -0.6; a12 = -0.3; a13 = -1.2; a14 = -0.3;
        t_0= time.time()
        print('Computing variables.. may take 5 minutes\n')
        # Matrix computation, gain?
        for i in range(1, M):
            # A = np.array([ [a1, a2, a3, a4, a6, 0, 0], 
            #                [a8, a9, a10, 0, 0, a11, a13]])
            # temp_x = np.array([1, x[i-1], y[i-1], np.power(np.abs(x[i-1]),a5) , np.power(np.abs(y[i-1]),a7),
            #                    np.power(np.abs(x[i-1]), a12), np.power(np.abs(y[i-1]), a14)]).reshape(-1,1)
            # x[i] , y[i] = A @ temp_x
            x[i] = a1 + a2 * x[i-1] + a3  * y[i-1] + a4  * np.power(np.abs(x[i-1]), a5)  + a6  * np.power(np.abs(y[i-1]), a7 )
            y[i] = a8 + a9 * x[i-1] + a10 * y[i-1] + a11 * np.power(np.abs(x[i-1]), a12) + a13 * np.power(np.abs(y[i-1]), a14)
            
            
            
        #x[i] = a1 + a2 * x[i-1] + a3  * y[i-1] + a4  * np.power(np.abs(x[i-1]), a5)  + a6  * np.power(np.abs(y[i-1]), a7 )
        #y[i] = a8 + a9 * x[i-1] + a10 * y[i-1] + a11 * np.power(np.abs(x[i-1]), a12) + a13 * np.power(np.abs(y[i-1]), a14)
    
        print(f'Variables computed, took {time.time() - t_0} seconds\n') 
        print('Now plotting, may also take long time ')
        
        
        mx = np.quantile(x, 0.01)
        mX = np.quantile(x, 0.99)
        my = np.quantile(y, 0.05)
        mY = np.quantile(y, 0.95)
        
        boolean_ = (x>mx) & (x<mX) & (y>my) & (y<mY)

        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 255, 255))
        self.graphWidget.plot(x[boolean_],y[boolean_], pen=pen, symbol='o', 
                              symbolSize=0.001, symbolBrush=('b'))
        self.graphWidget.showGrid(x=False, y=False)
        self.graphWidget.getPlotItem().hideAxis('bottom')
        self.graphWidget.getPlotItem().hideAxis('left')


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from collections import namedtuple
from xlrd.formula import colname
import pyqtgraph as pqg
from LCA_Datastructure import LifeCyclePhase

# Creates immutable constants to be used as Keys in dictionaries
Keys = namedtuple('Keys', ['FACTOR', 'PHASES', 'FABMETHOD'])
keys = Keys(FACTOR='factor', PHASES='phases', FABMETHOD='fabmethod')

class StakedBar_Graph_Class():    
    def CreateStakedBarGraphPlot(lca_Data, graphWidget):
        if not lca_Data:
            return graphWidget
        else:
            labels_Dict = lca_Data[0] # Gets labels dictionary    
            lcaData_Dict = lca_Data[1] # Gets LCA data dictionary
            
            factors = labels_Dict[keys.FACTOR] # where 0 = line, 1 = impact factor label, 2 = unit label
            phases = labels_Dict[keys.PHASES]
            
            # https://matplotlib.org/stable/users/explain/colors/colormaps.html
            cmap = cm.get_cmap('tab20')
            colors = [tuple(255*x for x in cmap(i/10))[:-1] for i in range(len(phases))]
            
            barWidth = 0.25  # the width of the bars
            
            # --- Create subplots for each factor ---
            for factor in factors:                          
                data = lcaData_Dict[factor[0]]   
                i=0
                graphWidget.addLabel(text=factor[1], size='10pt', bold=True, colspan=len(phases)) # Set line title with impact factor name
                graphWidget.nextRow()
                
                for fabmethod in data.keys():
                    barPlot = graphWidget.addPlot() #(title=factor[1]) # Set plot title with impact factor name
                    barPlot.addLegend()
                    barPlot.setLabel('left', factor[2]) # Set Y axis label with unit
                    barPlot.setLabel('top', fabmethod) # Set plot title with phase name
                    #barPlot.setLabel('bottom', 'Fabrication Methods') # Set X axis label
                    barPlot.showGrid(y=True)  # Show grid
                    #barPlot.showAxes( True, showValues=(False, False, False, False), size=10 )
                    #barPlot.getAxis('bottom').setTicks(([(j*barWidth + barWidth, fabmethod) for j, fabmethod in enumerate(data.keys())], [])) # Set X axis ticks with fabrication methods
                    barPlot.showAxis('bottom', False)  # Show X axis
                    #barPlot.enableAutoRange('xy', True)  # Enable auto range for both axes
                    
                    values = data.get(fabmethod)
                    bottom = 0
                    i=0
                    
                    for phase, color in zip(phases, colors):
                        if phase == LifeCyclePhase.OVERALL.name:
                            bargraph = pqg.BarGraphItem(x=1, height=values[i], width=barWidth, brush=pqg.mkBrush(color), name=phase)
                        else:
                            bargraph = pqg.BarGraphItem(x=1+barWidth, height=values[i], y0=bottom, width=barWidth, brush=pqg.mkBrush(color), name=phase)
                            bottom += values[i]
                        
                        i += 1
                        barPlot.addItem(bargraph)
                graphWidget.nextRow()        
            
            return graphWidget
# https://stackoverflow.com/questions/70435112/pyqtgraph-stacked-bar-graph
# https://doc.qt.io/qt-6/qtcharts-overview.html
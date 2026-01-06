# Information about PySide
#------------
# https://wiki.freecad.org/PySide
# https://wiki.freecad.org/PySide_Advanced_Examples
# https://www.pythontutorial.net/pyqt/pyqt-qdockwidget/
# https://doc.qt.io/qtforpython-5/overviews/qtwidgets-mainwindows-dockwidgets-example.html
# https://www.pythonguis.com/tutorials/pyside-modelview-architecture/
# https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/
# https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/
#
#------------
# Information about other scripting modules
#------------
#https://wiki.freecad.org/Python_scripting_tutorial
#https://wiki.freecad.org/Extra_python_modules#Usage
#https://wiki.freecad.org/Code_snippets
#https://wiki.freecad.org/FreeCAD_Scripting_Basics
#https://wiki.freecad.org/Python_scripting_tutorial#External_scripts
#
#------------
# Information about matplotlib Subplots
#------------
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
#------------

import FreeCAD, FreeCADGui 
import Spreadsheet
import numpy as np
import matplotlib.pyplot as plt
from widget_ui import Ui_LCAGraphWidget
from PySide import QtCore,QtWidgets
from PySide.QtCore import QSize
from PySide.QtGui import QScrollArea
import pyqtgraph as pqg


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from collections import namedtuple
from xlrd.formula import colname
import LCAData
import PlotGraph as PG
import RadarGraph as RG

# Creates immutable constants to be used as Keys in dictionaries
Keys = namedtuple('Keys', ['FACTOR', 'PHASES', 'FABMETHOD'])
keys = Keys(FACTOR='factor', PHASES='phases', FABMETHOD='fabmethod')

class LCA_Graph_Control_Class():    
    def __init__(self):
        self.FreeCADWindow = FreeCADGui.getMainWindow() # use this line if the 'addDockWidget' error is declared

        # Enable antialiasing for prettier plots
        pqg.setConfigOptions(antialias=True)

        self.LCAWidget = QtWidgets.QDockWidget("LCA Info") # create a new dockwidget 
        #self.LCAWidget.setMinimumSize(QSize(500, 500))
        #LCAFreeCADWidget = QtGui.QWidget() create a floating widget
        self.LCAWidget.ui = Ui_LCAGraphWidget() # load the Ui script
        self.LCAWidget.ui.setupUi(self.LCAWidget) # setup the ui

        labels = LCAData.GetLCALabels()
        if labels:
            factors = labels[keys.FACTOR]
            for x in range(len(factors)):
                row = x+3
                self.LCAWidget.ui.comboFactor.addItem(factors[x],str(row))
            phases = labels[keys.PHASES]
            for x in range(len(phases)):
                self.LCAWidget.ui.comboCycles.addItem(phases[x],colname(x+2))
            #These are the default values
            self.LCAWidget.ui.comboFactor.setDefaultValues(QtCore.Qt.Checked,(0,12,13,15))
            self.LCAWidget.ui.comboFactor.resetDefaultValues()
            self.LCAWidget.ui.comboCycles.setDefaultValues(QtCore.Qt.Checked,0)
            self.LCAWidget.ui.comboCycles.resetDefaultValues()

        self.FreeCADWindow.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.LCAWidget) # add the widget to the main window

    def GetResources(self):
        return {"Pixmap"  : "lca_logo", # the name of a svg file available in the resources
                "MenuText": "LCA Graph",
                "ToolTip" : "Show the graph of the LCA data"}

    def Activated(self): 
        # Get from user the LCA information to show 
        impact_category = self.LCAWidget.ui.comboFactor.currentData()
        impact_category = list(map(int,impact_category))
        #impact_category = [3,15,16,18] # The line number for impact category and unit type is always the same
        cycle_phases =  self.LCAWidget.ui.comboCycles.currentData() # The collumns for the cycle phases to get data from
        
        #categories = ['A' + str(category) for category in impact_category] # Adds the collumn letter for the impact category
        #units = ['B' + str(type) for type in impact_category] # Adds the collumn letter for the unit type
        #phases = [phase + '2' for phase in cycle_phases] # Add the line number, since the phase cycle is always the second line in the spreadsheets
        #data_cells = dict([(cat, cycle_phases) for cat in impact_category]) # Gets the cycle phases collumns and the impact category lines joines them to get the data form those specific data cells
        
        # Call GetSelectedArea() to get the ratio of selected area
        selection_ratio = self.GetSelectedArea()
        
        # Call GetSpecificLCAData() to get the data to populate the graph
        graphLCA_Data = LCAData.GetSpecificLCAData(impact_category, cycle_phases, selection_ratio)

        if not graphLCA_Data:
            self.LCAWidget.ui.textInfo.setText('No LCA spreadsheet found') # Changes the text in the label 
            self.LCAWidget.ui.graphWidget.clear() # Clears previous graph if any
        else: 
            # Checks how many phases there are, if there's less than 3 then show a Bar plot.
            labels_Dict = graphLCA_Data[0] # Gets labels dictionary 
            spoke_labels = labels_Dict[keys.PHASES]
            num_vertices = len(spoke_labels)
            
            self.LCAWidget.ui.textInfo.setText('') # Changes the text in the label 
            self.LCAWidget.ui.graphWidget.clear() # Clears previous graph if any
            self.LCAWidget.ui.graphWidget.sizeAdjustPolicy = QScrollArea.SizeAdjustPolicy.AdjustToContents
            
            #if num_vertices < 4:
            # Call CreateBarGraphPlot() to create the bar plot graph from the LCA data   
            canvas = PG.Bar_Graph_Class.CreateBarGraphPlot(graphLCA_Data, self.LCAWidget.ui.graphWidget)
            #else:
            #    canvas = RG.CreateRadarGraphPlot(graphLCA_Data)

        #------------------------------------------------------------------
        
        self.LCAWidget.show()

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

    def GetSelectedArea(self):
        totalArea = 0
        selectedArea = 0
        ratio = 1
        faces = []
        
        if FreeCAD.ActiveDocument is not None:
            obj = FreeCAD.ActiveDocument.findObjects(Type="Part::Feature") 

            totalArea = obj[0].Shape.Area
            
            if FreeCADGui.Selection.hasSelection():
                selections = FreeCADGui.Selection.getSelectionEx() # Gets selection object, which contains all the selections 
                
                for selection in selections:
                    faces = selection.SubObjects # gets the list of surface faces selected
                
                if faces:                    
                    for face in faces:
                        selectedArea += face.Area # calculates the area of the surface of a specific face
                    
                    ratio = (selectedArea / totalArea)

        print("RATIO: "+ str(ratio))
        return ratio
   
FreeCADGui.addCommand("LCA Graph", LCA_Graph_Control_Class())

#https://singerlinks.com/2023/08/how-to-create-a-user-interface-for-your-freecad-python-scripts/
# https://wiki.opensourceecology.org/wiki/FreeCAD_Workbench_Programming_101
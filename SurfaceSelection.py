import FreeCAD, FreeCADGui 
from widget_ui import Ui_LCAGraphWidget
from PySide import QtCore,QtGui,QtWidgets
import Measure

class Surface_Selection_Class():    
    def GetResources(self):
        return {"Pixmap"  : "Surface_logo", # the name of a svg file available in the resources
                "MenuText": "LCA Surface",
                "ToolTip" : "Show the surface for LCA"}

    def Activated(self):
        # QtWidgets.QToolBar()
        # with:
        # QtWidgets.QComboBox()
        # QtWidgets.QLineEdit()
               
        totalArea = 0
        selectedArea = 0
        faces = []
        
        if FreeCAD.ActiveDocument is not None:
            obj = FreeCAD.ActiveDocument.findObjects(Type="Part::Feature") 

            totalArea = obj[0].Shape.Area
            
            if FreeCADGui.Selection.hasSelection():
                selections = FreeCADGui.Selection.getSelectionEx() # Gets selection object, which contains all the selections 
                
                for selection in selections:
                    faces = selection.SubObjects # gets the list of surface faces selected
                
                for face in faces:
                    selectedArea += face.Area # calculates the area of the surface of a specific face
        
        print("This is the Total area " + str(totalArea*0.01) + "cm^2" + "Sub: " + str(selectedArea*0.01) + "cm^2")        
        return True
    
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
    
FreeCADGui.addCommand("Surface Selection", Surface_Selection_Class())
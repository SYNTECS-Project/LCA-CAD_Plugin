import FreeCAD, FreeCADGui 
import os

class MyWorkbench (Workbench):
    PATH = os.path.dirname('__file__')
        
    MenuText = "LCA Workbench"
    ToolTip = "A description of my workbench"
    Icon = os.path.join(PATH, "resources\lca_logo.svg") #"""paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        # import here all the needed files that create your FreeCAD commands
        import LCAGraphControl # Show the information in a graph of the LCA data
        self.list = ["LCA Graph"] # a list of command names created in the line above
        self.appendToolbar("LCA Tools", self.list) # creates a new toolbar with your commands
        self.appendMenu("LCA Values", self.list) # creates a new menu
        #self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("LCA Commands", self.list) # add commands to the context menu

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(MyWorkbench())
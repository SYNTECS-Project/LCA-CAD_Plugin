# Information about SpreadSheet
#------------
#https://freecad.github.io/API/d3/dac/namespaceSpreadsheet.html
#https://freecad.github.io/API/d3/d33/classSpreadsheet_1_1SheetPy.html
#
#   cellRange = sheets[0].getUsedRange()
#   nonemptyRange = sheets[0].getNonEmptyRange() # Returns the first used cell and the last used cell
#   usedCells = sheets[0].getNonEmptyCells()        
#   usedCells1 = sheets[0].getUsedCells() # Returns a list with all the used cells 
#   return the contents of row A starting from A1 until the first empty cell
#   sheet.cells["A1:-"]
#   return the contents of column A starting from A1 until the first empty cell
#   sheet.cells["A1:|"]
#   __doc__ <-- can manipulate spreadsheet
#
#   if sheet.getContents(cell): # sheet.getContents() can be used to check the cell first.
#       dataList.append = sheet.get(cell)
#   else # When no value is in the cell add 0 to show on the graph, for that sheet
#       dataList.append = 0
#
#------------

from collections import namedtuple
from dataclasses import dataclass
import FreeCAD
import Spreadsheet
import numpy
import re
from LCA_Datastructure import Factor, Phase, LifeCyclePhase, FactorType

# Creates immutable constants to be used as Keys in dictionaries
Keys = namedtuple('Keys', ['FACTOR', 'PHASES', 'FABMETHOD'])
keys = Keys(FACTOR='factor', PHASES='phases', FABMETHOD='fabmethod')

def GetLCALabels(): #impactCat = [3,13]  phases = ['C','F']
    #-------------- Get information from sheets ------------------
    #sheet = FreeCAD.ActiveDocument.getObject('Spreadsheet')
    if FreeCAD.ActiveDocument is not None:
        sheets = FreeCAD.ActiveDocument.findObjects(Type="Spreadsheet::Sheet") # Order should be: conventional then laser
        if sheets:                
            label_factor = sheets[0].cells["A3:|"]
            label_phases = sheets[0].cells["C2:-"]
            label_fabmethod = []
            
            for sheet in sheets:
                label_fabmethod.append(sheet.Label) # Gets the fabrication method from the sheet label
            
            # Dictionary with the labels to be shown on the graph
            dict_labels = {keys.FACTOR: label_factor, keys.PHASES: label_phases, keys.FABMETHOD: label_fabmethod}
            
            return dict_labels

def GetSpecificLCAData(impactCat_cells, phases_cells, ratio):
    #-------------- Get information from sheets ------------------
    #sheet = FreeCAD.ActiveDocument.getObject('Spreadsheet')
    if FreeCAD.ActiveDocument is not None:
        sheets = FreeCAD.ActiveDocument.findObjects(Type="Spreadsheet::Sheet") # Order should be: conventional then laser
        if sheets:                
            #label_ImpactFactor = sheets[0].cells[impactCat_cells]
            #label_Unit = sheets[0].cells[unit_cells]
            #label_phases = sheets[0].cells[phases_cells]
            
            #data_cells = dict([(cat, phases_cells) for cat in impactCat_cells]) # Gets the cycle phases collumns and the impact category lines joines them to get the data form those specific data cells
            
            label_factor_unit = [(cell,) + sheets[0].cells['A'+str(cell)+':B'+str(cell)] for cell in impactCat_cells] # Returns list with ([factor, unit],...)
            label_phases = [(sheets[0].cells[cell + '2']) for cell in phases_cells]
            label_fabmethod = []
            for sheet in sheets:
                label_fabmethod.append(sheet.Label) # Gets the fabrication method from the sheet label
            
            # Dictionary with the labels to be shown on the graph
            dict_labels = {keys.FACTOR: label_factor_unit, keys.PHASES: label_phases, keys.FABMETHOD: label_fabmethod}

            # Dictionary with cell data for a specific fabrication method
            full_data = {}
           
            for line in impactCat_cells:
                method_data = {}
                for sheet in sheets:
                    data = []
                    [data.append(NotNumber(sheet.cells[cell+str(line)])) for cell in phases_cells] # multiplies the value of the cell by the the area ratio, Assuming the LCA data is for the full part                                       
                    method_data[sheet.Label] = [x * ratio for x in data]
                                    
                full_data[line] = method_data
            
            # Tupple with the labels and cell data
            tuple_LCA = (dict_labels, full_data)
            
            return tuple_LCA

def GetSimplifiedLCAData(impactCat_cells, phases_cells, ratio):
    #-------------- Get information from sheets ------------------
    #sheet = FreeCAD.ActiveDocument.getObject('Spreadsheet')
    if FreeCAD.ActiveDocument is not None:
        sheets = FreeCAD.ActiveDocument.findObjects(Type="Spreadsheet::Sheet") # Order should be: conventional then laser
        if sheets:
            label_factor_unit = [(cell,FactorType(cell).name,sheets[0].get('B'+str(cell))) for cell in impactCat_cells] # Returns list with ([factor, unit],...)
            #label_phases = [name for name in dir(LifeCyclePhase) if not name.startswith('_')]
            label_phases = []
            for phase in phases_cells:
                label_phases.append(LifeCyclePhase(phase).name)            
            label_fabmethod = []
            for sheet in sheets:
                label_fabmethod.append(sheet.Label) # Gets the fabrication method from the sheet label        
                
            # Dictionary with the labels to be shown on the graph
            dict_labels = {keys.FACTOR: label_factor_unit, keys.PHASES: label_phases, keys.FABMETHOD: label_fabmethod}
            
            # Dictionary with cell data for a specific fabrication method
            full_data = {}
            
            for line in impactCat_cells:
                method_data = {}
                
                FactList = FactorType(line).getValues() # Gets the list of factor line numbers to get data from
                
                for sheet in sheets:
                    data = []
                    for cell in phases_cells:
                        value = 0
                        for fact in FactList:
                            value += NotNumber(sheet.cells[cell+str(fact)]) # Gets the main factor value

                        data.append(value * ratio) # multiplies the value of the cell by the the area ratio, Assuming the LCA data is for the full part
                    
                    method_data[sheet.Label] = data
                                    
                full_data[line] = method_data
            
            # Tupple with the labels and cell data
            tuple_LCA = (dict_labels, full_data)
            
            return tuple_LCA
            
                

def GetNormalizedData(full_data):

    if not isinstance(data, str):
        # Normalize data
        conjunto = "C"+str(line)+":-"
        subset = list(filter(lambda x: not isinstance(x, str), sheet.cells[conjunto])) # returns a subset of the list without string types
        mean = numpy.mean(subset)
        stdev = numpy.std(subset)

        value_norm = Z_Score_Normalize(data, mean, stdev)

def Z_Score_Normalize(series, mean, stdev):
    norm = [(x - mean) / stdev for x in series]
    #norm = (series - numpy.mean(series)) / numpy.std(series)
    return norm

def NotNumber(value):
    # This needs to be changed to alert the user that there are no values for a specific life cycle phase
    if isinstance(value, str) and re.fullmatch('-', value):
        return 0
    else:
        return value

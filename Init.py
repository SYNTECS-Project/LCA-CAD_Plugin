import subprocess, sys
import FreeCAD

# List of required libraries
libraries = ['matplotlib', 'numpy', 'xlrd', 'collections', 'pyqtgraph', 'qtwidgets', 'qtpy'] #'pyqt6-multiselect-combobox'
for library in libraries:
    try:
        __import__(library)
        print(f"{library} is already installed.")
    except ImportError:
        print(f"{library} is not installed. Installing {library}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
# ----------

"""FreeCAD init script of LCA Visualisation module"""

# ***************************************************************************
# *   Copyright (c) 2024 Jessica Corujeira                                  *
# *       jessica.corujeira@tecnico.ulisboa.pt                              *   
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENSE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************/

# Assumes Import_JSON.py is the file that has the code for opening and reading .ext files
#FreeCAD.addImportType("CSV (*.csv)","Import CSV")
#FreeCAD.addExportType("CSV (*.csv)","Export CSV")

#FreeCAD.addImportType("JSON5 (*.json5)", "read_json5_file")
#FreeCAD.addExportType("JSON5 (*.json5)", "write_json5_to_file")
print("I am executing some stuff here when FreeCAD starts!")

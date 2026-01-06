# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lca_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide.QtGui import (QFont, QVBoxLayout, QHBoxLayout, QScrollArea)
from PySide.QtWidgets import (QLabel, QWidget)

from pyqtgraph import GraphicsLayoutWidget
from qtwidgets import AnimatedToggle
import pyqtgraph as pg
import QCheckComboBox


class Ui_LCAGraphWidget(object):
    def setupUi(self, LCAGraphWidget):
        if not LCAGraphWidget.objectName():
            LCAGraphWidget.setObjectName(u"LCAGraphWidget")
        
        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        
        self.pagelayout = QVBoxLayout()
        self.gridLayoutWidget.setLayout(self.pagelayout)
        
        ## Toggle layout for Designer / Expert profile
        self.toggle_layout = QHBoxLayout()      
        self.pagelayout.addLayout(self.toggle_layout)
        
        labelPdesigner = QLabel()
        labelPdesigner.setObjectName(u"labelPDesigner")
        labelPdesigner.setText("Designer")
        font = QFont()
        font.setPointSize(10)
        labelPdesigner.setFont(font)
        labelPdesigner.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.toggle_layout.addWidget(labelPdesigner)

        self.profileToggle = AnimatedToggle(
            checked_color="#1565AA",
            pulse_checked_color="#44FFB000"
        )
        self.profileToggle.setObjectName(u"profileToggle")
        self.profileToggle.setFixedSize(60, 40)
        self.toggle_layout.addWidget(self.profileToggle)
        
        labelPExpert = QLabel()
        labelPExpert.setObjectName(u"labelPExpert")
        labelPExpert.setText("Expert")
        font = QFont()
        font.setPointSize(10)
        labelPExpert.setFont(font)
        labelPExpert.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.toggle_layout.addWidget(labelPExpert)
        ##---------------------
        
        ## Label and ComboBox layout
        self.label_combo_layout = QHBoxLayout()      
        self.pagelayout.addLayout(self.label_combo_layout)  
        
        textFact = QLabel(self.gridLayoutWidget)
        textFact.setObjectName(u"textFactors")
        textFact.setText("Factors")
        font = QFont()
        font.setPointSize(12)
        textFact.setFont(font)
        textFact.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_combo_layout.addWidget(textFact)

        textCycle = QLabel(self.gridLayoutWidget)
        textCycle.setObjectName(u"textCycles")
        textCycle.setText("Phase Cycles")
        font = QFont()
        font.setPointSize(12)
        textCycle.setFont(font)
        textCycle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_combo_layout.addWidget(textCycle)
                
        self.combo_layout = QHBoxLayout()    
        self.pagelayout.addLayout(self.combo_layout)
                
        # First dropdown (FACTOR main category)
        self.comboFactor = QCheckComboBox.QCheckComboBox(self.gridLayoutWidget)
        self.comboFactor.setObjectName(u"comboBox_Factors")
        self.combo_layout.addWidget(self.comboFactor)
        
        # Second dropdown (Phases main category)
        self.comboCycles = QCheckComboBox.QCheckComboBox(self.gridLayoutWidget)
        self.comboCycles.setObjectName(u"comboBox_Cycles")
        self.combo_layout.addWidget(self.comboCycles)
        ##---------------------
        
        self.textInfo = QLabel(self.gridLayoutWidget)
        self.textInfo.setObjectName(u"textInfo")
        font = QFont()
        font.setPointSize(10)
        self.textInfo.setFont(font)
        self.textInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pagelayout.addWidget(self.textInfo)

        self.graphWidget = GraphicsLayoutWidget(self.gridLayoutWidget, show=True)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(200, 200))
        self.graphWidget.setBackground("#FFFFFFBB")
        self.graphWidget.sizeAdjustPolicy = QScrollArea.SizeAdjustPolicy.AdjustToContents
        
        self.pagelayout.addWidget(self.graphWidget)
        
        #qSA = QScrollArea()
        #qSA.setWidget(self.graphWidget)
                 
        LCAGraphWidget.setWidget(self.gridLayoutWidget)
        
        self.retranslateUi(LCAGraphWidget)

        QMetaObject.connectSlotsByName(LCAGraphWidget)
    # setupUi

    def retranslateUi(self, LCAGraphWidget):
        LCAGraphWidget.setWindowTitle(QCoreApplication.translate("LCAGraphWidget", u"Life-Cycle Analysis Graphics", None))
        #self.textInfo.setText(QCoreApplication.translate("LCAGraphWidget", u"No LCA spreadsheet found", None))
    
    def setupDesignerProfile(self, pagelayout):
        pass
    def setupExpertProfile(self, pagelayout):
        pass
    
    # https://github.com/FreeCAD/freecad.workbench_starterkit
    
    # https://www.pythonguis.com/tutorials/pyqt6-layouts/
    
    # https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/
    # https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/
            
    # https://singerlinks.com/2023/08/how-to-create-a-user-interface-for-your-freecad-python-scripts/
    # https://wiki.opensourceecology.org/wiki/FreeCAD_Workbench_Python_Programming
    
    # https://github.com/user0706/pyqt6-multiselect-combobox
    # https://wiki.freecad.org/index.php?title=Extra_python_modules&section=24
    
    # https://3dpartsforyou.com/2021/07/26/how-to-install-freecad-workbenches/
    
    #https://github.com/Hizoka76/QCheckComboBox
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Esto es raro#
import cmath as cm
import math as m
from functools import reduce

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication

import convertedUI
import machines
import utility


class ExampleApp(QtGui.QMainWindow, convertedUI.Ui_Form):
    # Attribs
    __constants = machines.Constants()
    __trafo = machines.Transformer()
    __load = machines.Load()
    pu = False
    testMode = False
    operationMode = True
    stored = []
    storedTest = []

    styleLeft = {'align': 'left', 'size': '8', 'font-weight': '600'}
    styleCenter = {'align': 'center', 'size': '8', 'font-weight': '600'}
    styleRight = {'align': 'right', 'size': '8', 'font-weight': '600'}
    """
    Corto:
    V = 0.8 * Vnom = 0.08 * 44000 = 3520
    I =  500000 / (m.sqrt(3) * 44000) = 6.560798514 # Debería ser la Inominal
    Pcu = I**2 * 929.28 cos 80 = 1058.701482 20837.78132
    
    Vacío # Comprobada
    V = Vom = 44000
    I = 44000 / abs(Zm) = 44000 / 322169.874 = 0.1365739119
    Pfe = V**2 / Rm = 44000**2 / 387200 = 5000
    """

    # Constructor
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnSolve.released.connect(self.calcule)
        self.cbTestData.released.connect(self.toggleEnable)
        # Define outputs list
        self.__outList = [self.lblanom, self.lbla, self.lblEqImpedance, self.lblVLoad, self.lblSLoad, self.lblIload,
                          self.lblVDrop, self.lblVIn, self.lblRm, self.lblXm, self.lblZm, self.lblIm, self.lblIIn,
                          self.lblPfe, self.lblPcu, self.lbleffi, self.lblreg, self.lblFPin]
        # Store default values
        self.__defaults = [x.text() for x in self.__outList]
        # Define inputs list
        self.__inputs = [self.lnPrimaryV, self.leSecondaryV, self.leRatedPower, self.leLoadV, self.leLoadS, self.lePfe,
                         self.leQfd, self.leSCimpedance, self.leFP]
        # Define toggleable inputs: enabled in normal mode
        self.__toggleInputs = [self.leSCimpedance, self.lePfe, self.leQfd]
        # Define toggleable inputs: enabled in test mode
        self.__testInputs = [self.leRatedVoltage, self.l2ocCurrent, self.leFELosses, self.lescVoltage, self.leSCcurrent,
                             self.leCUlosses]
        # Set initial conditions on the interface initialization
        for x in self.__testInputs:
            # Disable test inputs
            x.setEnabled(False)
            # Store the values of test inputs
            self.storedTest.append(x.text())
        for x in self.__toggleInputs:
            # Store values, used to avoid error log
            self.stored.append(x.text())
        self.toggleEnable()
        return

    def keyPressEvent(self, event):
        # Override this method to detect the keyDown
        if event.key() == QtCore.Qt.Key_F8:
            self.testMode = True
            QtGui.QMessageBox.warning(self, "Debug mode", "     Activated     ")
        elif event.key() == QtCore.Qt.Key_F9:
            self.testMode = False
            QtGui.QMessageBox.warning(self, "Debug mode", "     Deactivated     ")
        elif event.key() == QtCore.Qt.Key_Return:
            self.calcule()
        event.accept()

    def toggleEnable(self):
        """ This method manage the dis/enabling of LineEdits according to the operation mode"""
        # On call restore the stored values
        self.restoreDefautls()
        # With theses conditionals
        if not self.cbTestData.isChecked():
            self.tabWidget.setCurrentIndex(0)
            self.operationMode = True
            # Restoring of the values
            for x in range(len(self.__toggleInputs)):
                self.__toggleInputs[x].setText(self.stored[x])
                self.__toggleInputs[x].setEnabled(True)

            # Store data and disable inputs
            self.storedTest = [x.text() for x in self.__testInputs]
            for x in self.__testInputs:
                x.setEnabled(False)
                x.setText("")

        else:
            self.tabWidget.setCurrentIndex(1)
            self.operationMode = False
            # Store data and disable inputs
            self.stored = [x.text() for x in self.__toggleInputs]
            for x in self.__toggleInputs:
                x.setEnabled(False)
                x.setText("")
            # Enabling ans restoring
            for x in range(len(self.__testInputs)):
                self.__testInputs[x].setText(self.storedTest[x])
                self.__testInputs[x].setEnabled(True)

        return

    def calcule(self):
        """Main method, compute all the output variables"""
        errorMessage = ""
        cond = True
        try:
            # Try to verify the input data
            if self.testMode:
                # Set the default values if TestMode is activated (F8 to enable, F9 to disable)
                self.lnPrimaryV.setText("44000")
                self.leSecondaryV.setText("13200")
                self.leRatedPower.setText("500000")
                self.leLoadV.setText("13100")
                self.leLoadS.setText("400000")
                self.lePfe.setText("3")
                self.leQfd.setText("2")
                self.leSCimpedance.setText("0.08,80")
                self.leFP.setText("0.9")
                self.rbLag.setChecked(True)

                self.leRatedVoltage.setText("13.2e3")
                self.l2ocCurrent.setText("13.2e3 / 9665.096219028392")
                self.leFELosses.setText("(13.2e3)**2 / 11616")

                self.lescVoltage.setText("0.08 * 348.48 * 500 / (44 * m.sqrt(3)) ")
                self.leSCcurrent.setText("500/(44 * m.sqrt(3))")
                self.leCUlosses.setText("(500/(44 * m.sqrt(3))) ** 2 * 0.08 * 348.48 * m.cos(m.radians(80))")

                self.rbOCsecondary.setChecked(True)
                self.rbSCsecondary.setChecked(True)
            # Verification of the inputs
            v1 = utility.validator(self.lnPrimaryV, tag="Rated primary voltage", nonZero=True)
            v2 = utility.validator(self.leSecondaryV, tag="Rated secondary voltage", nonZero=True)
            rpow = utility.validator(self.leRatedPower, tag="Rated power")
            loadV = utility.validator(self.leLoadV, tag="Load voltage")
            loadPow = utility.validator(self.leLoadS, tag="Load power")
            powerf = utility.validator(self.leFP, tag="Power Factor", rang=[0, 1])
            # According to the operation mode the respective inputs are verified
            if self.operationMode:
                Pfe = utility.validator(self.lePfe, tag="Pfe", rang=[0, 100])
                Qfd = utility.validator(self.leQfd, tag="Qfd", rang=[0, 100])
                zsc = utility.validator(self.leSCimpedance, tag="Shortcircuit impedance", isComplex=True)
                verfify = [v1, v2, rpow, loadV, loadPow, Pfe, Qfd, zsc, powerf]
            else:
                Voc = utility.validator(self.leRatedVoltage, tag="Open circuit voltage", nonZero=True)
                Ioc = utility.validator(self.l2ocCurrent, tag="Open circuit current", nonZero=True)
                Woc = utility.validator(self.leFELosses, tag="Iron losees", nonZero=True)
                #
                Vsc = utility.validator(self.lescVoltage, tag="Shortcircuit voltage", nonZero=True)
                Isc = utility.validator(self.leSCcurrent, tag="Shortcircuit current", nonZero=True)
                Wsc = utility.validator(self.leCUlosses, tag="Cupper losses", nonZero=True)
                verfify = [v1, v2, rpow, loadV, loadPow, Voc, Ioc, Woc, Vsc, Isc, Wsc, powerf]

            # Take the sign of the power factor
            if self.rbLag.isChecked():
                sign = -1
            else:
                sign = 1
            # reduce the bool values with the "and" operation
            cond = reduce((lambda x, y: x & y), [i[1] for i in verfify])
            # Take the name of the inputs that are wrong
            errorList = [i[2] for i in verfify if i[1] == False]
            if not (cond):
                # If there is errors in the inputs, these values summaried on a warning text
                errorMessage = reduce((lambda x, y: '' + x + '\n' + y), errorList)
                # Restore the values on error codition
                self.restoreDefautls()
                # Raise an error to jump to except
                raise ValueError("One or more of the input parameters are not valid")

        except:
            # Open a pop-up warning to notify to the user the unvalid paramaters
            QtGui.QMessageBox.warning(self, "Bad data", "Error on inputs:\n\n" + errorMessage)
            # print(errorMessage)
            pass
        if cond:
            # If all is right then store the solution method and the conecction, these ara parameters that evalate the operation mode
            methodsln = ""
            preslnmethod = self.cbMethod.currentText().split()[-1].replace("(", "").replace(")", "").replace(".", "")
            connection = self.cbConection.currentText().split()[-1].replace("(", "").replace(")", "")

            if "pu" in preslnmethod:
                # Per unit is an especial case
                methodsln = "pu"
                self.pu = True
            else:
                self.pu = False
                methodsln = preslnmethod
                methodsln += ","

            # Now we have to add the side or the conection D or Y
            if "P" in methodsln:
                methodsln += str(connection[0]).upper()
            elif "S" in methodsln:
                methodsln += str(connection[-1]).upper()

            self.__trafo.nominal(v1[0], v2[0], rpow[0], connection)  # Give the parameters to the machine
            self.__load.nominal(loadPow[0], loadV[0], powerf[0], sign)

            self.__constants.updateTables(self.__trafo, methodsln[0:2])  # Update the table of constant

            # Another calculus
            # Zbase:
            Zbase = self.__constants.getconstantsln('k1', methodsln) * self.__trafo.Zb

            if self.operationMode:
                # In normal mode Shortcircuit impedance [p.u] is the value of the lineEdit
                Sc = zsc[0]

            else:
                # In the other mode, the values of the shortcircuit impedance is taken in Ohms, and have to been transformed in per unit.
                # Give to the transformer tha values of the tests
                self.__trafo.ShortCircuitTest(Vsc[0], Isc[0], Wsc[0], self.rbSCprimary.isChecked(), self.__trafo.An)
                self.__trafo.OpenCircuitTest(Voc[0], Ioc[0], Woc[0], self.rbOCprimary.isChecked(), self.__trafo.An)
                if self.pu:
                    # additionally if is in testmode and per unit the Shortcircuit impedance it's expressed as follows
                    Sc = self.__trafo.Zeqserie * self.__constants.getconstantsln('k1', methodsln)
                else:
                    # else have to divide by Zbase TODO: check english syntax on this comments
                    Sc = self.__trafo.Zeqserie * self.__constants.getconstantsln('k1', methodsln) / Zbase
                # In the test mode the Pfe and Qfd are not neccesary then set to 0
                Pfe, Qfd = [0], [0]

            self.__trafo.extraData(Sc, Pfe[0], Qfd[0])  # Give to the transformer the additional parameters

            # 00 Summary of additional calculus The numbers marked as # XX can be consulted in the paper on GitHub TODO do the document will be public?
            Zeq = self.__trafo.p_scimpedance * Zbase  # 03
            Vload = self.__constants.getconstantsln('k2', methodsln) * self.__load.voltage  # 04
            Sload = self.__constants.getconstantsln('k3', methodsln) * self.__load.power  # 05
            Iload = cm.rect(self.__constants.getconstantsln('k4', methodsln) * Sload / Vload,
                            self.__load.sign * m.acos(self.__load.powerFactor))  # 06
            Vdrop = self.__constants.getconstantsln('k5', methodsln) * Zeq * Iload  # 07
            Vin = Vdrop + Vload  # 08

            if self.operationMode:
                # According to the operation mode, it's setted the Rm, Xm and Zm impedances
                try:
                    Rm = self.__constants.getconstantsln('k1', methodsln) * self.__trafo.V2 ** 2 / (
                        self.__trafo.Pfe * self.__trafo.Sn)  # 09
                except ZeroDivisionError:
                    Rm = 1e1000
                try:
                    Xm = self.__constants.getconstantsln('k1', methodsln) * self.__trafo.V2 ** 2 / (
                        self.__trafo.Qfd * self.__trafo.Sn)  # 10
                except ZeroDivisionError:
                    Xm = 1e1000
            else:
                Rm = self.__trafo.Rmtest * self.__constants.getconstantsln('k1', methodsln)
                Xm = self.__trafo.Xmtest * self.__constants.getconstantsln('k1', methodsln)

            self.__trafo.setRm(Rm)
            self.__trafo.setXm(Xm)

            Zm = self.__trafo.getZm()  # 11
            Im = self.__constants.getconstantsln('k6', methodsln) * Vin / Zm  # 12
            Ie = Im + Iload  # 13
            IronLosses = self.__constants.getconstantsln('k7', methodsln) * abs(Vin) ** 2 / Rm  # 14
            CupperLosses = self.__constants.getconstantsln('k8', methodsln) * abs(Iload) ** 2 * Zeq.real  # 15
            eff = (Sload * self.__load.powerFactor * 100) / (
                Sload * self.__load.powerFactor + IronLosses + CupperLosses)  # 16
            Vreg = (abs(Vin) - abs(Vload)) * 100 / abs(Vload)  # 17
            FPin = m.cos(m.atan2(Vin.imag, Vin.real) - m.atan2(Ie.imag, Ie.real)) * self.__load.sign  # 18

            # 01

            utility.setOutText(self.lblanom, self.__trafo.An, prefix="a nom: ", pu=self.pu, style=self.styleLeft)

            # 02
            utility.setOutText(self.lbla, self.__constants.workingA, prefix="a real: ", pu=self.pu,
                               style=self.styleLeft)

            # 03
            utility.setOutText(self.lblEqImpedance, Zeq, prefix="Zeq: ", suffix=" Ω", pu=self.pu, polar=True,
                               style=self.styleCenter)

            # 04
            utility.setOutText(self.lblVLoad, Vload, prefix="Vc: ", suffix=" V", pu=self.pu, polar=True)

            # 05
            utility.setOutText(self.lblSLoad, Sload, prefix="Sc: ", suffix=" VA", pu=self.pu, polar=True)

            # 06
            utility.setOutText(self.lblIload, Iload, prefix="Ic: ", suffix=" A", pu=self.pu, polar=True, br=True)

            # 07
            utility.setOutText(self.lblVDrop, Vdrop, prefix="ΔV: ", suffix=" V", pu=self.pu, polar=True, br=True,
                               style=self.styleCenter)

            # 08
            utility.setOutText(self.lblVIn, Vin, prefix="Ve: ", suffix=" V", pu=self.pu, polar=True, br=True,
                               style=self.styleCenter)

            # 09
            utility.setOutText(self.lblRm, self.__trafo.Rm, prefix="Rm: ", suffix=" Ω", pu=self.pu, polar=True,
                               style=self.styleLeft)

            # 10
            utility.setOutText(self.lblXm, self.__trafo.Xm, prefix="Xm: ", suffix=" Ω", pu=self.pu, polar=True,
                               style=self.styleLeft)

            # 11
            utility.setOutText(self.lblZm, Zm, prefix="Zm: <BR>", suffix=" Ω", pu=self.pu, polar=True, br=True,
                               style=self.styleCenter)

            # 12
            utility.setOutText(self.lblIm, Im, prefix="Im: ", suffix=" A", pu=self.pu, polar=True, style=self.styleLeft)

            # 13
            utility.setOutText(self.lblIIn, Ie, prefix="Ie: ", suffix=" A", pu=self.pu, polar=True, br=True,
                               style=self.styleCenter)

            # 14
            utility.setOutText(self.lblPfe, IronLosses, prefix="Pfe: ", suffix=" W", pu=self.pu, style=self.styleLeft)

            # 15
            utility.setOutText(self.lblPcu, CupperLosses, prefix="Pcu: ", suffix=" W", pu=self.pu, style=self.styleLeft)

            # 16
            utility.setOutText(self.lbleffi, eff, prefix="η= ", suffix=" %", pu=True, style=self.styleLeft)

            # 17
            utility.setOutText(self.lblreg, Vreg, prefix="Reg: ", suffix=" %", pu=True, style=self.styleLeft)

            # 18
            utility.setOutText(self.lblFPin, FPin, prefix="Fp e: ", pu=True, style=self.styleLeft)

    def restoreDefautls(self):
        for x in range(len(self.__outList)):  # Restore defaults
            self.__outList[x].setText(self.__defaults[x])


if __name__ == "__main__":
    app = QApplication([])
form = ExampleApp()
form.show()
app.exec_()

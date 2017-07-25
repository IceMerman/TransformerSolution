import math

import utility as u


class Transformer(object):
    # Atributos
    __V1 = 0
    V2 = 0
    Sn = 0
    __Zcc = 0
    connection = ""
    p_scimpedance = 0 + 0j
    Pfe = ""
    Qfd = ""

    # Atributos para el metodo por unidad
    vbase = 0
    sb = 0
    Zb = 0

    # Variables del para calculos
    An = 0
    Rm = 0
    Xm = 0j
    Zm = 0 + 0j

    def __init__(self):
        pass

    def nominal(self, V1: float, V2: float, Sn: float, connection: str):
        """set the transformer nominal values"""
        self.__V1 = V1
        self.V2 = V2
        self.Sn = Sn
        self.connection = connection
        # calculus
        self.An = V1 / V2  # Take the transformer relation
        # Set base parameters
        self.vbase = V2
        self.sb = Sn
        self.Zb = V2 ** 2 / Sn
        return

    def extraData(self, SCimpedance: complex, pfe: float, qfd: float):
        """Set additional information to solve the transformer circuit"""
        self.p_scimpedance = SCimpedance
        self.Pfe = pfe
        self.Qfd = qfd
        return True

    def setRm(self, Rm):
        self.Rm = Rm
        return True

    def setXm(self, Xm):
        self.Xm = 1j * Xm
        return True

    def setZm(self):
        """Set the paralell impedance"""
        r = self.Rm
        x = self.Xm
        if (not math.isinf(r)) and (not math.isinf(x.imag)):
            self.Zm = (r * x) / (r + x)
        elif (math.isinf(r)) and (not math.isinf(x.imag)):
            self.Zm = x
        elif (not math.isinf(r)) and (math.isinf(x.imag)):
            self.Zm = r
        else:
            self.Zm = 1e1000
        return True

    def getZm(self):
        self.setZm()
        return self.Zm

    def OpenCircuitTest(self, v: float, i: float, w: float, transform: bool = False, a: float = 1):
        theta = math.acos(w / (v * i * math.sqrt(1)))
        if theta == 0:
            Xm = 1e1000
        else:
            Xm = v / (i * math.sin(theta))
        if theta == 90:
            Rm = 1e1000
        else:
            Rm = v / (i * math.cos(theta))
        self.Rmtest = Rm * u.ternary(transform, a ** -2,
                                     1)  # Ternary! used according to the side where the measurements were made
        self.Xmtest = Xm * u.ternary(transform, a ** -2, 1)
        self.setZmtest()
        return True

    def ShortCircuitTest(self, v: float, i: float, w: float, transform: bool = False, a: float = 0):
        theta = math.acos(w / (v * i * math.sqrt(1)))
        Zeqtest = (v / i) * u.ternary(transform, a ** -2, 1)
        Rserie = Zeqtest * math.cos(theta)
        Xserie = Zeqtest * math.sin(theta)
        self.Zeqserie = Rserie + 1j * Xserie
        return True

    def setZmtest(self):
        """Set the paralell impedance"""
        r = self.Rmtest
        x = self.Xmtest
        if (not math.isinf(r)) and (not math.isinf(x.imag)):
            self.Zmtest = (r * x) / (r + x)
        elif (math.isinf(r)) and (not math.isinf(x.imag)):
            self.Zmtest = x
        elif (not math.isinf(r)) and (math.isinf(x.imag)):
            self.Zmtest = r
        else:
            self.Zmtest = 1e1000
        return True


class Load(object):
    """Unnecessary defined as object, could be a dictionary"""
    # Attrib
    power = 0
    voltage = 0
    powerFactor = 0
    sign = 0

    def __init__(self):
        pass

    def nominal(self, power: float, voltage: float, powerFactor: float, sign: float):
        self.power = power
        self.voltage = voltage
        self.powerFactor = powerFactor
        self.sign = sign
        return


class Constants(object):
    # Attribs

    # Set some values to save calculation time
    __sqrt3 = math.sqrt(3)
    __invsqrt3 = 1 / __sqrt3
    __one_third = 1 / 3

    __conectionlist = ["Yy", "Dy", "Dd", "Yd"]
    __slntype = ["SS", "TS", "SP", "TP", "pu"]
    __k_constants = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"]
    __methodsln = ["SS,Y", "SS,D", "TS,Y", "TS,D", "SP,Y", "SP,D", "TP,Y", "TP,D", "pu"]

    __atable = []
    __ktable = []

    def __init__(self):
        pass

    def updateTables(self, trafoa: Transformer, method: str):
        """This function build the tables used in the solution of the circuit"""
        a = trafoa.An
        self.__atable = (
            [1, 1, a, a, 1], [1, 1, self.__sqrt3 * a, a, 1], [1, 1, a, a, 1], [1, 1, a * self.__invsqrt3, a, 1])

        self.workingA = self.__atable[self.__conectionlist.index(trafoa.connection)][self.__slntype.index(method)]
        self.__ktable = ([1, 3, 1, 3, a ** 2, 3 * a ** 2, a ** 2, 3 * a ** 2, 1 / trafoa.Zb],
                         [self.__invsqrt3, 1, 1, 1, self.workingA, self.workingA * self.__invsqrt3, self.workingA,
                          self.workingA, 1 / trafoa.vbase],
                         [self.__one_third, self.__one_third, 1, 1, self.__one_third, self.__one_third, 1, 1,
                          1 / trafoa.sb],
                         [1, 1, self.__invsqrt3, self.__invsqrt3, 1, 1, self.__invsqrt3, self.__invsqrt3, 1],
                         [1, 1, self.__sqrt3, self.__invsqrt3, 1, 1, self.__sqrt3, self.__invsqrt3, 1],
                         [1, 1, self.__invsqrt3, self.__sqrt3, 1, 1, self.__invsqrt3, self.__sqrt3, 1],
                         [1, 1, 1, 3, 1, 1, 1, 3, 1], [1, 1, 3, 1, 1, 1, 3, 1, 1])
        return True

    def getconstantsln(self, k_key: str, method: str) -> float:
        """Get the constant K# for the solution"""
        return self.__ktable[self.__k_constants.index(k_key)][self.__methodsln.index(method)] * 1.

    def getWorkingA(self):
        """Get the transformer relation fixed with the connection"""
        return self.workingA * 1.

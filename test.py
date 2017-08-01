import transformer as t
import math as m

conection="Dy"
# TODO: this file is old and must be updated!

a = t.Constans(44000, 13200, 500000, 0.013891854213354433+0.07878462024097664j, 13100, 400000, 0.03, 0.02)

def printpolar(complexnumer: complex):
    mag=abs(complexnumer)
    try:
        angle=m.degrees(m.atan(complexnumer.imag/complexnumer.real))
    except(ZeroDivisionError):
        angle = 90
    return str(mag)+" <_ "+str(angle)

def debug(slntype, method, conection="Dy"):
    fp = 0.9
    sign = -1

    a.buildconstants_table_k(conection, method)

    print("[01]: ", a.a_nom)
    print("[01]: ", a.getalpha(conection, method))
    print("[02]: ", a.baseimpedance(slntype))
    print("[03]: ", printpolar(a.p_equivalentimpedance(slntype)))
    print("[04]: ", a.voltageonload(slntype))
    print("[05]: ", a.aparentpoweronload(slntype))
    print("[06]: ", printpolar(a.p_currentonload(slntype, fp, sign)))
    print("[07]: ", printpolar(a.p_voltagedrop(slntype, fp, sign)))
    print("[08]: ", printpolar(a.p_inputvoltage(slntype, fp, sign)))
    print("[09]: ", a.magnetizationresistance(slntype))
    print("[10]: ", printpolar(a.magnetizationreactance(slntype)))
    print("[11]: ", printpolar(a.p_magnetizationimpedance(slntype)))
    print("[12]: ", printpolar(a.p_magnetizationcurrent(slntype, fp, sign)))
    print("[13]: ", printpolar(a.p_inputcurrent(slntype, fp, sign)))
    print("[14]: ", a.corelosses(slntype, fp, sign))
    print("[15]: ", a.cupperlosses(slntype, fp, sign))
    print("[16]: ", a.efficiency(slntype, fp, sign))
    print("[17]: ", a.regulation(slntype, fp, sign))
    print("[18]: ", a.inputpowerfactor(slntype, fp, sign))

    return True

debug("MS,Y", "MS")





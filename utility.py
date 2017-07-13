import cmath as cm
import math
import math as m

import PyQt4.QtCore as Core
from PyQt4.QtGui import QLineEdit, QLabel

preset = """<html><head/><body><p align={0[align]}><span style=" font-weight:{0[font-weight]}; font-size:{0[size]}pt">raw</span></p></body></html>"""

safe_dict = {'m': math, 'math': math}


def ternary(comp: bool, t: object, f: object):
    if comp:
        return t
    else:
        return f


def myRound(number: float, presition: int =4) -> float:
    return m.ceil(number * 10 ** presition) / 10 ** presition


def magnitudeprefix(number: float, convert: bool = True) -> tuple:
    if convert:
        if number >= 1e9:
            return 1e-9, ' G'
        elif number >= 1e6:
            return 1e-6, ' M'
        elif number >= 1e3:
            return 1e-3, ' k'
        elif number >= 1e0:
            return 1e0, ' '
        elif number >= 1e-3:
            return 1e3, ' m'
        elif number >= 1e-6:
            return 1e6, ' u'
        elif number >= 1e-9:
            return 1e9, ' n'
        else:
            return 1, ' '
    else:
        return 1, ' '


def text2HTML(newValue: object, prefix: str = "", suffix: str = "", polar: bool = False, br=False, pu=False,
              style: dict = {'align': 'center', 'size': '8', 'font-weight': '600'}):
    preset.format(style)
    if pu:
        suffix = ""
        roundvalue = 4
        convert = False
    else:
        roundvalue = 2
        convert = True

    if br:
        extra = "<BR>"
    else:
        extra = ""
    if isinstance(newValue, float) and m.isnan(newValue):
        return preset.replace("RichText", prefix + "inf" + suffix)
    if isinstance(newValue, complex) and m.isnan(newValue.real):
        return preset.replace("RichText", prefix + "inf" + suffix)
    if isinstance(newValue, float):
        numberdata = magnitudeprefix(newValue, convert)
        suffix = numberdata[1] + suffix.replace(" ", "")
        textOut = round(newValue * numberdata[0], roundvalue)
        return preset.replace("RichText", prefix + extra + str(textOut) + suffix)

    if not polar:
        re = newValue.real
        im = newValue.imag
        if re == 0:
            numberdata = magnitudeprefix(im, convert)
        else:
            numberdata = magnitudeprefix(re, convert)
        re = re * numberdata[0]
        im = im * numberdata[0]
        if isinstance(newValue, complex):
            temp = str(round(re, roundvalue) + 1j * round(im, roundvalue))
        else:
            numberdata = magnitudeprefix(abs(newValue), convert)
            temp = str(round(newValue, roundvalue) * numberdata[0])
        # prefix.replace("*n","<BR>")
        suffix = numberdata[1] + suffix.replace(" ", "")
        return preset.replace("RichText", prefix + extra + temp.replace("(", "").replace(")", "") + suffix)
    else:
        magnitude = abs(newValue)
        try:
            angle = round(m.degrees(m.atan(newValue.imag / newValue.real)), 2)
        except:
            angle = 90
        numberdata = magnitudeprefix(magnitude, convert)
        absolute = newValue * numberdata[0]
        suffix = numberdata[1] + suffix.replace(" ", "")
        magnitude = round(abs(absolute), roundvalue)
        complexOut = str(magnitude) + "<BR>∠" + str(angle) + "°"
        return preset.replace("RichText", prefix + str(complexOut) + suffix)


def setOutText(label: QLabel, value, prefix: str = "", suffix: str = "", polar: bool = False, br: bool = False,
               pu: bool = False, style: dict = {'align': 'center', 'size': '8', 'font-weight': '600'}):
    # Replacements
    if br:
        s = "<BR>"
    else:
        s = ""
    if pu:
        pre = "4"
        convert = False
        if not "%" in suffix:
            suffix = ""
    else:
        pre = "2"
        convert = True

    if isinstance(value, complex):
        if polar:
            r, phi = cm.polar(value)

            factor, unit = magnitudeprefix(r, convert)
            suffix = suffix.strip()
            suffix = " " + unit + suffix
            r = factor * r

            r = '{0:.<pre>f}'.replace("<pre>", pre).format(r).strip("0")
            if r == '.':
                r = 0.0
            else:
                r = float(r)
            phi = m.degrees(phi)
            phi = '{0:.<pre>f}'.replace("<pre>", pre).format(phi).strip("0")
            if phi == '.':
                phi = 0.0
            else:
                phi = float(phi)

            value = (r, phi)

            if phi == 90.:
                out = "<prefix>{0}j<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).format(value[0])
            else:
                out = "<prefix>{0}<br>∠{1}°<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).replace(
                    "<br>", s).format(value[0], value[1])

        else:
            out = "<prefix>{0.real:.<pre>f}<br>{0.imag: .<pre>f}j<suffix>".replace("<prefix>", prefix).replace(
                "<suffix>", suffix).replace("<br>", s).replace("<pre>", pre).format(value)
    elif isinstance(value, float) or isinstance(value, int):
        value = ternary(value == ".", 0, float(value))
        factor, unit = magnitudeprefix(value, convert)
        suffix = suffix.strip()
        suffix = " " + unit + suffix
        value = factor * value

        value = '{0:.<pre>f}'.replace("<pre>", pre).format(value).strip("0")
        if value == '.':
            value = 0.0
        else:
            value =float(value)

        out = "<prefix>{0}<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).format(value)
    else:
        print('The value input must be complex or float')
    label.setTextFormat(Core.Qt.RichText)
    label.setText(preset.replace("raw", out).format(style))


def validator2(lineEdit: QLineEdit, desiredtype="float", tag: str = "", nonZero=False, rang: tuple = []):
    # Old version
    value = lineEdit.text()
    lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
    try:
        if value == "":
            lineEdit.setText("Error")
            raise ValueError("The input is empty")
        if len(rang) == 2:
            if rang[0] <= float(value) <= rang[1]:
                pass
            else:
                raise ValueError("The input is out of limits")
        elif len(rang) != 0 or len(rang) == 1 or len(rang) >= 3:
            raise ValueError("Internal error, please report to the autor")
        if desiredtype == "float":
            value = float(value)
            if nonZero and value == 0:
                raise ValueError("The input value can't be 0")
            value = float(value)
        if desiredtype == "complex":
            if "," in value:
                s = value.split(",")
                value = float(s[0]) * (round(m.cos(m.radians(float(s[1])))) + 1j * round(m.sin(m.radians(float(s[1])))))
                if nonZero and abs(value) == 0:
                    raise ValueError("The input value can't be 0")
            else:
                if nonZero and abs(complex(''.join(value.split()))) == 0:
                    raise ValueError("The input value can't be 0")
                value = complex(''.join(value.split()))
        success = True
    except Exception as e:
        print(e)
        warning(lineEdit)
        success = False
    finally:
        return [value, success, tag]


def validator(lineEdit: QLineEdit, isComplex=False, tag: str = "", nonZero=False, rang: list = []):
    lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
    try:
        value = eval(lineEdit.text(), {"__builtins__": None}, safe_dict)
        if not isComplex:
            if isinstance(value, int):
                value *= 1.
            if isinstance(value, float):
                if len(rang) == 2:
                    if rang[0] <= float(value) <= rang[1]:
                        pass
                    else:
                        raise ValueError("The input is out of limits")
            if tag in ('Pfe', 'Qfd'):
                value /= 100
        else:
            if isinstance(value, int):
                value *= 1.
            if isinstance(value, float):
                value = complex(value)
            elif isinstance(value, tuple):
                value = cm.rect(value[0], m.radians(value[1]))
            elif isinstance(value, complex):
                pass
            else:
                print("Not valid", type(value))
        if nonZero and abs(value) == 0:
            raise ValueError("The input value can't be 0")
        sucess = True
    except Exception as e:
        value = lineEdit.text()
        if lineEdit.text() == "": lineEdit.setText("Error")
        print(e)
        warning(lineEdit)
        sucess = False
    finally:
        return [value, sucess, tag]


def warning(lineEdit: QLineEdit):
    argin = lineEdit.text()
    lineEdit.setStyleSheet("color: rgb(255, 0, 0);")
    lineEdit.setText(argin)
    return True

def logger():
    # TODO: make a report file for error
    pass

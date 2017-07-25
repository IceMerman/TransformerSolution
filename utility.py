import cmath as cm
import math
import math as m

import PyQt4.QtCore as Core
from PyQt4.QtGui import QLineEdit, QLabel

# Text pattern with a lot of wilds to be replaced
preset = """<html><head/><body><p align={0[align]}><span style=" font-weight:{0[font-weight]}; font-size:{0[size]}pt">raw</span></p></body></html>"""

# Dictionary of valid function/libs/modules taht can be passed to the eval()
safe_dict = {'m': math, 'math': math}


def ternary(comp: bool, t: object, f: object):
    """Ternary it's cool"""
    if comp:
        return t
    else:
        return f


# Unnecessary method
# def myRound(number: float, presition: int = 4) -> float:
#     return m.ceil(number * 10 ** presition) / 10 ** presition


def magnitudeprefix(number: float, convert: bool = True) -> tuple:
    """Function that fix the value to scientific notation"""
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


# Old version, will be deleted
# def text2HTML(newValue: object, prefix: str = "", suffix: str = "", polar: bool = False, br=False, pu=False,
#               style: dict = {'align': 'center', 'size': '8', 'font-weight': '600'}):
#     # Qt text can be spicified eith HTML !
#     preset.format(style)
#     if pu:
#         # In p.u the values are rounded with 4 decimals
#         suffix = ""
#         roundvalue = 4
#         convert = False
#     else:
#         roundvalue = 2
#         convert = True
#
#     if br:
#         extra = "<BR>" # If the flag its true, the is changed for a bracket in html
#     else:
#         extra = ""
#     # Set de prefix and suffix, also it's verified that the values be diferrent nan (Not A Number)
#     if isinstance(newValue, float) and m.isnan(newValue):
#         return preset.replace("RichText", prefix + "inf" + suffix)
#     if isinstance(newValue, complex) and m.isnan(newValue.real):
#         return preset.replace("RichText", prefix + "inf" + suffix)
#     if isinstance(newValue, float):
#         numberdata = magnitudeprefix(newValue, convert) # Take the fixed value and the  scientfic notation suffix
#         suffix = numberdata[1] + suffix.replace(" ", "") # Add to the original suffix the scientific suffix
#         textOut = round(newValue * numberdata[0], roundvalue) # The the value is rounder
#         return preset.replace("RichText", prefix + extra + str(textOut) + suffix)# Finally return the output text
#
#     if not polar:
#         """Not tested yet"""
#         re = newValue.real
#         im = newValue.imag
#         if re == 0:
#             numberdata = magnitudeprefix(im, convert)
#         else:
#             numberdata = magnitudeprefix(re, convert)
#         re = re * numberdata[0]
#         im = im * numberdata[0]
#         if isinstance(newValue, complex):
#             temp = str(round(re, roundvalue) + 1j * round(im, roundvalue))
#         else:
#             numberdata = magnitudeprefix(abs(newValue), convert)
#             temp = str(round(newValue, roundvalue) * numberdata[0])
#         suffix = numberdata[1] + suffix.replace(" ", "")
#         return preset.replace("RichText", prefix + extra + temp.replace("(", "").replace(")", "") + suffix)
#     else:
#         magnitude = abs(newValue)
#         try:
#             angle = round(m.degrees(m.atan(newValue.imag / newValue.real)), 2)
#         except:
#             angle = 90
#         numberdata = magnitudeprefix(magnitude, convert)
#         absolute = newValue * numberdata[0]
#         suffix = numberdata[1] + suffix.replace(" ", "")
#         magnitude = round(abs(absolute), roundvalue)
#         complexOut = str(magnitude) + "<BR>∠" + str(angle) + "°"
#         return preset.replace("RichText", prefix + str(complexOut) + suffix)


def setOutText(label: QLabel, value, prefix: str = "", suffix: str = "", polar: bool = False, br: bool = False,
               pu: bool = False, style: dict = {'align': 'center', 'size': '8', 'font-weight': '600'}):
    # Replacements, Qt text works with HTML !
    if br:
        s = "<BR>"  # If the flag is true then insert a bracket
    else:
        s = ""
    if pu:
        # In p.u the values are rounded with a precision of 4 decimals
        pre = "4"
        convert = False # in p.u convertions are not enabled (See magnitudeprefix() method)
        if not "%" in suffix:
            # If in p.u and % is in the suffix, then the suffix is overwritten to ""
            suffix = ""
    else:
        pre = "2"
        convert = True

    if isinstance(value, complex):
        if polar:
            # The value is converted to polar coordinates
            r, phi = cm.polar(value)

            factor, unit = magnitudeprefix(r, convert)
            suffix = suffix.strip()
            suffix = " " + unit + suffix
            r = factor * r

            # Used as a fake round
            r = '{0:.<pre>f}'.replace("<pre>", pre).format(r).strip("0")
            # the number is converted to text, also is applied the strip() method, so it's neccesary to verify that the result be dofferent from "."
            if r == '.':
                r = 0.0
            else:
                r = float(r)
            # Convert the output value to degrees
            phi = m.degrees(phi)
            # Used as a fake round
            phi = '{0:.<pre>f}'.replace("<pre>", pre).format(phi).strip("0")
            if phi == '.':
                phi = 0.0
            else:
                phi = float(phi)

            value = (r, phi)

            # An special case, if the angle is 90° then is replaced by j

            if phi == 90.:
                out = "<prefix>{0}j<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).format(value[0])
            else:
                out = "<prefix>{0}<br>∠{1}°<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).replace(
                    "<br>", s).format(value[0], value[1])

        else:
            # Not used can be problematic
            out = "<prefix>{0.real:.<pre>f}<br>{0.imag: .<pre>f}j<suffix>".replace("<prefix>", prefix).replace(
                "<suffix>", suffix).replace("<br>", s).replace("<pre>", pre).format(value)
    elif isinstance(value, float) or isinstance(value, int):
        value = ternary(value == ".", 0, float(value)) # Ternary is cool, but inefficient in python
        factor, unit = magnitudeprefix(value, convert)
        suffix = suffix.strip()
        suffix = " " + unit + suffix
        value = factor * value

        # Conversion and validation
        value = '{0:.<pre>f}'.replace("<pre>", pre).format(value).strip("0")
        if value == '.':
            value = 0.0
        else:
            value = float(value)

        out = "<prefix>{0}<suffix>".replace("<prefix>", prefix).replace("<suffix>", suffix).format(value)
    else:
        print('The value input must be complex or float')
    label.setTextFormat(Core.Qt.RichText)
    label.setText(preset.replace("raw", out).format(style))


# def validator2(lineEdit: QLineEdit, desiredtype="float", tag: str = "", nonZero=False, rang: tuple = []):
#     # Old version
#     value = lineEdit.text()
#     lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
#     try:
#         if value == "":
#             lineEdit.setText("Error")
#             raise ValueError("The input is empty")
#         if len(rang) == 2:
#             if rang[0] <= float(value) <= rang[1]:
#                 pass
#             else:
#                 raise ValueError("The input is out of limits")
#         elif len(rang) != 0 or len(rang) == 1 or len(rang) >= 3:
#             raise ValueError("Internal error, please report to the autor")
#         if desiredtype == "float":
#             value = float(value)
#             if nonZero and value == 0:
#                 raise ValueError("The input value can't be 0")
#             value = float(value)
#         if desiredtype == "complex":
#             if "," in value:
#                 s = value.split(",")
#                 value = float(s[0]) * (round(m.cos(m.radians(float(s[1])))) + 1j * round(m.sin(m.radians(float(s[1])))))
#                 if nonZero and abs(value) == 0:
#                     raise ValueError("The input value can't be 0")
#             else:
#                 if nonZero and abs(complex(''.join(value.split()))) == 0:
#                     raise ValueError("The input value can't be 0")
#                 value = complex(''.join(value.split()))
#         success = True
#     except Exception as e:
#         print(e)
#         warning(lineEdit)
#         success = False
#     finally:
#         return [value, success, tag]


def validator(lineEdit: QLineEdit, isComplex=False, tag: str = "", nonZero=False, rang: list = []):
    """Function to validate the inputs
    tag input is used in the main file to know the name of the failed input"""
    # Set the color to black
    lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
    try:
        value = eval(lineEdit.text(), {"__builtins__": None}, safe_dict)
        # Value is taken using eval, the eval is restricted to a void potential risk code injection
        if not isComplex:
            if isinstance(value, int):
                # If not is complex and is an int then it's conver to float
                value *= 1.
            if isinstance(value, float):
                # then if is float (or was converted to float) is verified that the value be in the range of the rang input
                if len(rang) == 2:
                    # TODO implemtns as assertion
                    if rang[0] <= float(value) <= rang[1]:
                        pass
                    else:
                        raise AssertionError("The input is out of limits")
            if tag in ('Pfe', 'Qfd'):
                # The value is ingrese and percentaje [0,100], the it's is divided by 100
                value /= 100
        else:
            if isinstance(value, int):
                value *= 1.
            if isinstance(value, float):
                value = complex(value)
            elif isinstance(value, tuple):
                if len(value) > 2:
                    # If its complex and polar, two arguments must been taken, else error
                    raise ValueError("This input takes max 2 arguments")
                value = cm.rect(value[0], m.radians(value[1]))
            elif isinstance(value, complex):
                # If its complex and its given as a+bj, there's no need of conversion
                pass
            else:
                print("Not valid", type(value))
        if nonZero and abs(value) == 0:
            # Its possible that some values must be different from 0 tho avoid ZeroDivision exception, so this is verified here
            raise ValueError("The input value can't be 0")
        sucess = True
    except Exception as e:
        # Runtime on exceptions
        value = lineEdit.text()
        if lineEdit.text() == "": lineEdit.setText("Error")
        print(e)
        warning(lineEdit)
        sucess = False
    finally:
        # Return the value, a bool that confirm the right validation, adn the tag
        return [value, sucess, tag]


def warning(lineEdit: QLineEdit):
    # A little function to set the text on red color if there are warnings
    argin = lineEdit.text()
    lineEdit.setStyleSheet("color: rgb(255, 0, 0);")
    lineEdit.setText(argin)
    return True


def logger():
    # TODO: make a report file for errors
    pass

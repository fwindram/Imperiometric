# imconvert.py
# Skeletorfw
# 06/07/17
#
# Python 3.4.1
#
# Conversion module for use in Imperiometric Bot
# Must be called from Imperiometric.py or logging functions will cause errors.

from allowed_units import allowed_units
from collections import namedtuple

import logging
#convert_logger = logging.getLogger(__name__)     # May not work. We'll see?

# Set up logging
# logging.basicConfig(level=logging.INFO)
convert_logger = logging.getLogger(__name__)
convert_logger.setLevel(logging.DEBUG)

# Create logfile handler
handler = logging.FileHandler('log/imperiometric.out')
handler.setLevel(logging.DEBUG)  # File logging level

# Create formatter and add to handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
convert_logger.addHandler(handler)


class UnitError(Exception):
    """Raised when a source unit is not correctly defined."""
    pass


class UnitMismatchError(Exception):
    """Raised when the source and destination units are not of the same type."""
    pass


class UnitIdentityError(Exception):
    """Raised when the source and destination units are the same"""
    pass


def length_convert(srcamt, srcunit, dstunit, default=True):
    """Convert length from one unit to another."""
    dstamnt = 0
    convert_dict_metric = {
        # unit: (default_multiplier, base_unit_multiplier)
        # default_multiplier:   Amount to multiply by to get the default conversion
        # base_unit_multiplier: Amount to multiply by to get the base unit (Often the SI unit)
        "km": (0.6214, 1000),
        "m": (1.094, 1),    # BASE UNIT
        "cm": (0.3937, 0.01),
        "mm": (0.03937, 0.001),
        "µm": (0.00003937, 0.000001),
        "base": (39.37, 1)  # base <-> base converter
    }
    convert_dict_imperial = {
        "mile": (1.609, 63360),
        "yd": (0.9144, 36),
        "ft": (0.3048, 12),
        'in': (0.0254, 1),      # BASE UNIT
        "base": (0.0254, 1)  # base <-> base converter
    }

    if srcunit.scheme == 'Metric':
        srcunit_dict = convert_dict_metric
    else:
        srcunit_dict = convert_dict_imperial
    if dstunit.scheme == 'Metric':
        dstunit_dict = convert_dict_metric
    else:
        dstunit_dict = convert_dict_imperial

    if default:
        src_multiplier = srcunit_dict[srcunit.unit][0]
    else:
        src_multiplier = (srcunit_dict[srcunit.unit][1] * srcunit_dict["base"][0] / dstunit_dict[dstunit.unit][1])

    dstamnt = srcamt * src_multiplier

    return dstamnt, dstunit.unit


def mass_convert(srcamt, srcunit, dstunit, default=True):
    """Convert mass from one unit to another."""
    pass


def volume_convert(srcamt, srcunit, dstunit, default=True):
    """Convert volume from one unit to another."""
    pass


def area_convert(srcamt, srcunit, dstunit, default=True):
    """Convert area from one unit to another."""
    pass


def convert(srcamt, source_unit, destination_unit=None):
    """Convert from source unit to equivalent in the other scheme.
    
    :param srcamt: Amount to convert
    :type srcamt: float
    :param source_unit: Unit to convert from
    :type source_unit: str
    :param destination_unit: Destination unit if given
    :type destination_unit: str
    :return: (rtnamt, rtnunit)
    :rtype: tuple"""

    # TODO: Consider whether input needs preprocessing to deal with formats such as x lb y oz

    # Convert srcamt to float, and allow exception if necessary.
    srcamt = float(srcamt)

    # Put units into named tuple for easy access
    unit = namedtuple("Unit", "unit, fullname, singname, unittype, scheme, default_target")
    source_unit = source_unit.lower()   # Make sure incoming units are in lowercase
    if source_unit in allowed_units:
        srcunit = unit(source_unit,                     # unit
                       allowed_units[source_unit][0],   # fullname
                       allowed_units[source_unit][1],   # singname
                       allowed_units[source_unit][2],   # unittype
                       allowed_units[source_unit][3],   # scheme
                       allowed_units[source_unit][4])   # default_target
    else:
        raise UnitError
    convert_logger.debug("Source unit set to {}.".format(srcunit.fullname))
    using_default = True
    if destination_unit:
        using_default = False
        destination_unit = destination_unit.lower()     # Make sure incoming units are in lowercase
        if destination_unit in allowed_units:
            dstunit = unit(destination_unit,                    # unit
                           allowed_units[destination_unit][0],  # fullname
                           allowed_units[destination_unit][1],  # singname
                           allowed_units[destination_unit][2],  # unittype
                           allowed_units[destination_unit][3],  # scheme
                           allowed_units[destination_unit][4])  # default_target
        else:
            raise UnitError
    else:   # Use default target as destination
        dstunit = unit(srcunit.default_target,                      # unit
                       allowed_units[srcunit.default_target][0],    # fullname
                       allowed_units[srcunit.default_target][1],    # singname
                       allowed_units[srcunit.default_target][2],    # unittype
                       allowed_units[srcunit.default_target][3],    # scheme
                       allowed_units[srcunit.default_target][4])    # default_target
    convert_logger.debug("Destination unit set to {}.".format(dstunit.fullname))

    # Check whether units are convertable.
    if srcunit.unittype != dstunit.unittype:
        raise UnitMismatchError

    # Check whether units are identical.
    if srcunit.unit == dstunit.unit:
        raise UnitIdentityError

    # Call the required conversion
    # TODO: We could return a set of two tuples here, containing a primary unit + amt & a secondary one.
    # This would allow us to return things such as x lb y oz
    if srcunit.unittype == "length":
        final = length_convert(srcamt, srcunit, dstunit, using_default)
    elif srcunit.unittype == "mass":
        mass_convert(srcamt, srcunit, dstunit, using_default)
    elif srcunit.unittype == "volume":
        volume_convert(srcamt, srcunit, dstunit, using_default)
    elif srcunit.unittype == "area":
        area_convert(srcamt, srcunit, dstunit, using_default)
    else:
        convert_logger.error("Source unit type '{}' is not valid! Check allowed_units entry for '{}'."
                             .format(srcunit.unittype, srcunit.unit)
                             )
        raise UnitError

    # Return converted amount & units
    return final

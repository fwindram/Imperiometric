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
convert_logger = logging.getLogger("Imperiometric")     # May not work. We'll see?


class UnitException(Exception):
    """Raised when a source unit is not correctly defined."""
    pass


class UnitMismatchException(Exception):
    """Raised when the source and destination units are not of the same type."""
    pass

def convert(srcamt, source_unit, destination_unit=None):
    """Convert from source unit to equivalent in the other scheme.
    
    :param srcamt: Amount to convert
    :type srcamt: float
    :param source_unit: Unit to convert from
    :type source_unit: str
    :param destination_unit: Destination unit if given
    : 
    :return: (rtnamt, rtnunit)
    :rtype: tuple"""

    # Put units into named tuple for easy access
    unit = namedtuple("Unit", "unit, fullname, singname, unittype, scheme, default_target")
    if source_unit in allowed_units:
        srcunit = unit(source_unit,                     # unit
                       allowed_units[source_unit][0],   # fullname
                       allowed_units[source_unit][1],   # singname
                       allowed_units[source_unit][2],   # unittype
                       allowed_units[source_unit][3],   # scheme
                       allowed_units[source_unit][4])   # default_target
    else:
        raise UnitException
    convert_logger.debug("Source unit set to {}.".format(srcunit.fullname))
    if destination_unit:
        if destination_unit in allowed_units:
            dstunit = unit(destination_unit,                    # unit
                           allowed_units[destination_unit][0],  # fullname
                           allowed_units[destination_unit][1],  # singname
                           allowed_units[destination_unit][2],  # unittype
                           allowed_units[destination_unit][3],  # scheme
                           allowed_units[destination_unit][4])  # default_target
        else:
            raise UnitException
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
        raise UnitMismatchException

    # Call the required conversion
    if srcunit.unittype == "length":
        pass
    elif srcunit.unittype == "mass":
        pass
    elif srcunit.unittype == "volume":
        pass
    elif srcunit.unittype == "area":
        pass
    else:
        convert_logger.error("Source unit type '{}' is not valid! Check allowed_units entry for '{}'."
                             .format(srcunit.unittype, srcunit.unit)
                             )
        raise UnitException

    # Return converted amount & units

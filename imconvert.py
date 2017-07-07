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
from unit_conversions import *

import logging

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


# Exception classes
class UnitError(Exception):
    """Raised when a source unit is not correctly defined."""
    pass


class UnitMismatchError(Exception):
    """Raised when the source and destination units are not of the same type."""
    pass


class UnitIdentityError(Exception):
    """Raised when the source and destination units are the same"""
    pass


def unit_convert(srcamt, srcunit, dstunit, convert_dict_metric, convert_dict_imperial, default=True):
    """Convert measure from one unit to another."""
    # TODO: Add the rest of the conversions to unit_conversions.py
    dstamnt = 0

    # Determine used dicts
    if srcunit.scheme == 'Metric':
        srcunit_dict = convert_dict_metric
    else:
        srcunit_dict = convert_dict_imperial

    if dstunit.scheme == 'Metric':
        dstunit_dict = convert_dict_metric
    else:
        dstunit_dict = convert_dict_imperial

    # Generate final multiplier
    if default:                                 # Use default precalculated factor
        src_multiplier = srcunit_dict[srcunit.unit][0]
    elif srcunit.scheme == dstunit.scheme:      # Use base unit multipliers only
        src_multiplier = srcunit_dict[srcunit.unit][1] / dstunit_dict[dstunit.unit][1]
    else:                                       # Include base converter measure (to convert to other scheme)
        src_multiplier = srcunit_dict[srcunit.unit][1] * srcunit_dict["base"][0] / dstunit_dict[dstunit.unit][1]

    # Apply multiplier to srcamt
    dstamnt = srcamt * src_multiplier

    # TODO: Sanify the returned unit where necessary to return the simplest unit possible if not specified.

    return dstamnt, dstunit.unit


def convert(srcamt, source_unit, destination_unit=None):
    """Convert from source unit to equivalent in the other scheme.
    
    :param srcamt: Amount to convert.
    :type srcamt: float
    :param source_unit: Unit to convert from.
    :type source_unit: str
    :param destination_unit: Destination unit (optional).
    :type destination_unit: str
    
    :returns: (rtnamt, rtnunit)
    :rtype: tuple
    
    :raises UnitError: When a source unit is not correctly defined.
    :raises UnitMismatchError: When the source and destination units are not of the same type.
    :raises UnitIdentityError: When the source and destination units are identical."""

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

    # Call the unit conversion
    # TODO: We could return a set of two tuples here, containing a primary unit + amt & a secondary one.
    # This would allow us to return things such as x lb y oz
    final = ()
    if srcunit.unittype == "length":
        final = unit_convert(srcamt, srcunit, dstunit, length_idents_metric, length_idents_imperial, using_default)
    elif srcunit.unittype == "mass":
        final = unit_convert(srcamt, srcunit, dstunit, mass_idents_metric, mass_idents_imperial, using_default)
    elif srcunit.unittype == "volume":
        final = unit_convert(srcamt, srcunit, dstunit, volume_idents_metric, volume_idents_imperial, using_default)
    elif srcunit.unittype == "area":
        final = unit_convert(srcamt, srcunit, dstunit, area_idents_metric, area_idents_imperial, using_default)
    else:
        convert_logger.error("Source unit type '{}' is not valid! Check allowed_units entry for '{}'."
                             .format(srcunit.unittype, srcunit.unit)
                             )
        raise UnitError

    # Return converted amount & units
    return final

# imconvert.py
# Skeletorfw
# 06/07/17
#
# Python 3.4.1
#
# Conversion module for use in Imperiometric Bot
# Must be called from Imperiometric.py or logging functions will cause errors.

import logging
convert_logger = logging.getLogger('Imperiometric')     # May not work. We'll see?


class UnitException(Exception):
    """Raised when a source unit is not correctly defined."""
    pass


def convert(srcamt, srcunit):
    """Convert from source unit to equivalent in the other scheme.
    
    :param srcamt: Amount to convert
    :type srcamt: float
    :param srcunit: Unit to convert from
    :type srcunit: str
    
    :return: (rtnamt, rtnunit)
    :rtype: tuple"""

    # Allowed units - (fullname, singname, unittype,scheme)
    allowed_units = {
        # Length
        "km": ('kilometers', 'kilometer', 'length', 'Metric'),
        "m": ('meters', 'meter', 'length', 'Metric'),
        "cm": ('centimeters', 'centimeter', 'length', 'Metric'),
        "mm": ('millimeters', 'millimeter', 'length', 'Metric'),
        "µm": ('micrometers', 'micrometer', 'length', 'Metric'),
        "mile": ('miles', 'mile', 'length', 'Imperial'),
        "yd": ('yards', 'yard', 'length', 'Imperial'),
        "ft": ('feet', 'foot', 'length', 'Imperial'),
        'in': ('inches', 'inch', 'length', 'Imperial'),
        # Mass
        "t": ('tonnes', 'tonne', 'mass', 'Metric'),
        "kg": ('kilograms', 'kilogram', 'mass', 'Metric'),
        "g": ('grams', 'gram', 'mass', 'Metric'),
        "mg": ('milligrams', 'milligram', 'mass', 'Metric'),
        "µg": ('micrograms', 'microgram', 'mass', 'Metric'),
        "ng": ('nanograms', 'nanogram', 'mass', 'Metric'),
        "st": ('stone', 'stone', 'mass', 'Imperial'),
        "lb": ('pounds', 'pound', 'mass', 'Imperial'),
        "oz": ('ounces', 'ounce', 'mass', 'Imperial')
    }

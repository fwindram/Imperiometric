# Imperiometric Bot allowed units list
# Is this nice? Probably not. Could it be done in a db? Yes. Do I care? No.
# This is easy to work with and provides visibility of the internal workings, though I may convert it to a csv later.


# Allowed units - (fullname, singname, unittype, scheme, default_target)
allowed_units = {
    # Length
    "km": ('kilometers', 'kilometer', 'length', 'Metric', 'mile'),
    "m": ('meters', 'meter', 'length', 'Metric', 'yd'),
    "cm": ('centimeters', 'centimeter', 'length', 'Metric', 'in'),
    "mm": ('millimeters', 'millimeter', 'length', 'Metric', 'in'),
    "µm": ('micrometers', 'micrometer', 'length', 'Metric', 'in'),
    "mile": ('miles', 'mile', 'length', 'Imperial', 'km'),
    "yd": ('yards', 'yard', 'length', 'Imperial', 'm'),
    "ft": ('feet', 'foot', 'length', 'Imperial', 'm'),
    'in': ('inches', 'inch', 'length', 'Imperial', 'cm'),
    # Mass
    "tonne": ('tonnes', 'tonne', 'mass', 'Metric', 'ton'),
    "kg": ('kilograms', 'kilogram', 'mass', 'Metric', 'lb'),
    "g": ('grams', 'gram', 'mass', 'Metric', 'oz'),
    "mg": ('milligrams', 'milligram', 'mass', 'Metric', 'oz'),
    "µg": ('micrograms', 'microgram', 'mass', 'Metric', 'oz'),
    "ng": ('nanograms', 'nanogram', 'mass', 'Metric', 'oz'),
    "ton": ('tons', 'ton', 'mass', 'Imperial', 'tonne'),     # US Ton
    "st": ('stone', 'stone', 'mass', 'Imperial', 'kg'),
    "lb": ('pounds', 'pound', 'mass', 'Imperial', 'kg'),
    "oz": ('ounces', 'ounce', 'mass', 'Imperial', 'g'),
    # Volume (fluid capacity)
    "l": ('litres', 'litre', 'volume', 'Metric', 'pt'),
    "cl": ('centilitres', 'centilitre', 'volume', 'Metric', 'qt'),
    "ml": ('millilitres', 'millilitre', 'volume', 'Metric', 'floz'),
    "µl": ('microlitres', 'microlitre', 'volume', 'Metric', 'floz'),
    "gal": ('gallons', 'gallon', 'volume', 'Imperial', 'l'),
    "qt": ('quarts', 'quart', 'volume', 'Imperial', 'l'),
    "pt": ('US pints', 'US pint', 'volume', 'Imperial', 'ml'),
    "ukpt": ('UK pints', 'UK pint', 'volume', 'Imperial', 'ml'),
    "floz": ('fluid ounces', 'fluid ounce', 'volume', 'Imperial', 'ml'),
    # # Volume (spatial)
    # "m3": ('cubic meters', 'cubic meter', 'volume', 'Metric'),
    # "cm3": ('cubic centimeters', 'cubic centimeter', 'volume', 'Metric'),
    # "mm3": ('cubic millimeters', 'cubic millimiter', 'volume', 'Metric'),
    # Area
    "km2": ('square kilometers', 'square kilometer', 'area', 'Metric', 'mi2'),
    "m2": ('square meters', 'square meter', 'area', 'Metric', 'yd2'),
    "cm2": ('square centimeters', 'square centimeter', 'area', 'Metric', 'ft2'),
    "mm2": ('square millimeters', 'square millimeter', 'area', 'Metric', 'in2'),
    "mi2": ('square miles', 'square mile', 'area', 'Imperial', 'km2'),
    "yd2": ('square yards', 'square yard', 'area', 'Imperial', 'm2'),
    "ft2": ('square feet', 'square foot', 'area', 'Imperial', 'cm2'),
    "in2": ('square inches', 'square inch', 'area', 'Imperial', 'cm2')
}

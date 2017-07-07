# Imperiometric Bot unit conversion identities.

# unit: (default_multiplier, base_unit_multiplier)
# default_multiplier:   Amount to multiply by to get the default conversion
# base_unit_multiplier: Amount to multiply by to get the base unit (Often the SI unit)

length_idents_metric = {
    "km": (0.6214, 1000),
    "m": (1.094, 1),    # BASE UNIT
    "cm": (0.3937, 0.01),
    "mm": (0.03937, 0.001),
    "µm": (0.00003937, 0.000001),
    "base": (39.37, 1)  # base <-> base converter
}

length_idents_imperial = {
    "mile": (1.609, 63360),
    "yd": (0.9144, 36),
    "ft": (0.3048, 12),
    'in': (0.0254, 1),      # BASE UNIT
    "base": (0.0254, 1)  # base <-> base converter
}

mass_idents_metric = {

}

mass_idents_imperial = {

}

volume_idents_metric = {

}

volume_idents_imperial = {

}

area_idents_metric = {

}

area_idents_imperial = {

}





def hex_to_decimal(hex_value):
    if hex_value == '0x':
        return 0
    return int(hex_value, 16)


def decimal_to_hex(decimal):
    return hex(decimal)

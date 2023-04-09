def binary_excess3_to_decimal(binary_excess3):
    """
    Convert binary excess-3 code to decimal.
    """
    decimal = ""
    # Convert the binary excess-3 code to a string to make it iterable
    binary_excess3_str = str(binary_excess3)
    
    # Loop through the binary excess-3 code in groups of 4 bits
    for i in range(0, len(binary_excess3_code), 4):
        # Extract a group of 4 bits
        group = binary_excess3_code[i:i+4]
        # Convert the group of 4 bits to decimal
        decimal_digit = int(group, 2) - 3
        # Convert the decimal digit back toa string and append to the result
        decimal += str(decimal_digit)
    
    return decimal

# Take input from the user for the binary excess-3 code
binary_excess3_code = input("Enter binary excess-3 code: ")
decimal_num = binary_excess3_to_decimal(binary_excess3_code)

print("Binary Excess-3 Code:", binary_excess3_code)
print("Decimal Number:", decimal_num)
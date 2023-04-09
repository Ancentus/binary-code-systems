def generate_gray_codes(n):
    """
    Generates higher-bit Gray codes using the reflect-and-prefix method.
    
    Args:
    - n (int): The number of bits in the Gray codes.
    
    Returns:
    - list: A list of higher-bit Gray codes.
    """
    # Base case: For n = 1, return the Gray code '0' and '1'
    if n == 1:
        return ['0', '1']
    
    # For n > 1, recursively generate Gray codes for n-1 bits
    gray_codes_n_minus_1 = generate_gray_codes(n - 1)
    
    # Reflect-and-prefix the Gray codes for n-1 bits to generate Gray codes for n bits
    gray_codes_n = []
    for code in gray_codes_n_minus_1:
        gray_codes_n.append('0' + code)
    for code in reversed(gray_codes_n_minus_1):
        gray_codes_n.append('1' + code)
    
    return gray_codes_n

# Test the function with n = 3
n = 3
gray_codes = generate_gray_codes(n)
print(f"Gray codes for {n} bits: {gray_codes}")

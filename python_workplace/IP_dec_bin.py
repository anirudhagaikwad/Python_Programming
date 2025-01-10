"""
Python program that takes an IPv4 address as input, converts it into its binary representation using bitwise operators, and displays the result in the format:

Enter an IPv4 address (e.g., 192.168.1.1): 192.168.1.1
--- IPv4 Conversion ---
IPv4 in Decimal = 192.168.1.1
IPv4 in Binary  = 11000000.10101000.00000001.00000001

Bitwise Conversion:

    Each part of the IPv4 address is shifted right using >> to extract specific bits.
    The & 1 operation extracts the least significant bit of the shifted value.
    The loop constructs the 8-bit binary string for each part.

Binary Representation:

    The binary strings for each part are joined with dots (".") to form the full binary IPv4 address.


"""
def ipv4_to_binary(ipv4_address):
    """Convert an IPv4 address to binary representation using bitwise operators."""
    # Split the IPv4 address into its components
    parts = ipv4_address.split(".")
    binary_parts = []
    
    for part in parts:
        # Convert each part to an integer
        part_int = int(part)
        # Use bitwise operations to get the 8-bit binary value
        binary_part = ""
        for i in range(7, -1, -1):  # Iterate from bit 7 to 0
            binary_part += str((part_int >> i) & 1)
        binary_parts.append(binary_part)
    
    # Join the binary parts with dots to form the final binary representation
    binary_ipv4 = ".".join(binary_parts)
    return binary_ipv4

def main():
    """Main function to get user input and display the IPv4 address in binary."""
    ipv4_address = input("Enter an IPv4 address (e.g., 192.168.1.1): ")
    try:
        binary_representation = ipv4_to_binary(ipv4_address)
        print("\n--- IPv4 Conversion ---")
        print("IPv4 in Decimal =", ipv4_address)
        print("IPv4 in Binary  =", binary_representation)
    except ValueError:
        print("Invalid IPv4 address. Please enter a valid address in the format x.x.x.x.")

# Run the program
main()

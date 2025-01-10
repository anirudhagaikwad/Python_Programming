def calculate_subnet_mask(host_count):
    """Calculate subnet mask and CIDR notation based on host count."""
    bits_needed = 0
    total_addresses = 1
    while total_addresses < host_count + 2:  # Include network and broadcast addresses
        total_addresses <<= 1  # Same as multiplying by 2
        bits_needed += 1
    subnet_bits = 32 - bits_needed
    mask = (0xFFFFFFFF << bits_needed) & 0xFFFFFFFF  # Create subnet mask
    return mask, subnet_bits

def ip_to_int(ip):
    """Convert dotted decimal IP to a 32-bit integer."""
    parts = ip.split(".")
    return (
        (int(parts[0]) << 24)
        | (int(parts[1]) << 16)
        | (int(parts[2]) << 8)
        | int(parts[3])
    )

def int_to_ip(num):
    """Convert a 32-bit integer to dotted decimal IP."""
    return f"{(num >> 24) & 0xFF}.{(num >> 16) & 0xFF}.{(num >> 8) & 0xFF}.{num & 0xFF}"

def calculate_addresses(base_ip, subnet_mask):
    """Calculate network address, broadcast address, and host range."""
    base_ip_int = ip_to_int(base_ip)
    network_address = base_ip_int & subnet_mask
    broadcast_address = network_address | (~subnet_mask & 0xFFFFFFFF)
    first_host = network_address + 1
    last_host = broadcast_address - 1
    return (
        int_to_ip(network_address),
        int_to_ip(broadcast_address),
        int_to_ip(first_host),
        int_to_ip(last_host),
    )

def ipv4_calculator():
    """Main function for IPv4 calculator."""
    # Input the base IP address and number of hosts required
    base_ip = input("Enter the base IP address (e.g., 192.168.0.0): ")
    host_count = int(input("Enter the number of hosts required: "))

    # Calculate subnet mask and CIDR
    subnet_mask, subnet_bits = calculate_subnet_mask(host_count)

    # Calculate addresses
    network_address, broadcast_address, start_ip, end_ip = calculate_addresses(
        base_ip, subnet_mask
    )

    # Convert subnet mask to dotted decimal
    subnet_mask_str = int_to_ip(subnet_mask)

    # Print the results
    print("\n--- IPv4 Calculator Result ---")
    print("Network Address:", network_address)
    print("Broadcast Address:", broadcast_address)
    print("Subnet Mask:", subnet_mask_str + "/" + str(subnet_bits))
    print("Host Range:", start_ip, "-", end_ip)

# Run the calculator
ipv4_calculator()

"""
    Subnet Mask:
        Create the subnet mask by shifting 1s to the left (<<) for unused host bits, then masking with 0xFFFFFFFF to limit it to 32 bits.

    IP Conversion:
        ip_to_int: Converts an IP from dotted decimal to a 32-bit integer using bitwise shifts (<<) and OR (|).
        int_to_ip: Converts a 32-bit integer back to dotted decimal using bitwise shifts (>>) and masking (&).

    Network & Broadcast:
        network_address: Calculated using bitwise AND (&) between the base IP and the subnet mask.
        broadcast_address: Calculated using bitwise OR (|) with the inverted subnet mask (~).

    Host Range:
        First host: network_address + 1
        Last host: broadcast_address - 1

Output :
--- IPv4 Calculator Result ---
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.63
Subnet Mask: 255.255.255.192/26
Host Range: 192.168.1.1 - 192.168.1.62

"""
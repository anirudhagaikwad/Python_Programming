import math
import ipaddress

def calculate_subnet_mask(host_count):
    """Calculate subnet mask based on the number of hosts."""
    bits_needed = math.ceil(math.log2(host_count + 2))  # Include network and broadcast addresses
    subnet_bits = 32 - bits_needed
    subnet_mask = (1 << 32) - (1 << bits_needed)
    return ipaddress.IPv4Address(subnet_mask), subnet_bits

def get_ip_range(network):
    """Get the range of usable IPs in the network."""
    hosts = list(network.hosts())
    return hosts[0], hosts[-1]

def ipv4_calculator():
    """Main function for IPv4 calculator."""
    # Input the base IP address and number of hosts required
    base_ip = input("Enter the base IP address (e.g., 192.168.0.0): ")
    host_count = int(input("Enter the number of hosts required: "))
    
    # Calculate subnet mask
    subnet_mask, subnet_bits = calculate_subnet_mask(host_count)
    
    # Define the network
    network = ipaddress.IPv4Network(f"{base_ip}/{subnet_bits}", strict=False)
    
    # Get the host range
    start_ip, end_ip = get_ip_range(network)
    
    # Print the details
    print("\n--- IPv4 Calculator Result ---")
    print(f"Network Address: {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Subnet Mask: {subnet_mask}/{subnet_bits}")
    print(f"Host Range: {start_ip} - {end_ip}")

# Run the calculator
ipv4_calculator()

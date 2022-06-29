from ipaddress import IPv4Network


def print_network_information(ipv4network: IPv4Network) -> None:
    """Prints the network address, broadcast address and number
    of addresses on the given IPv4 network.
    """

    print('Network IP:', ipv4network.network_address)
    print('Broadcast address:', ipv4network.broadcast_address)
    print('Number of hosts:', ipv4network.num_addresses)


def main() -> None:
    print_network_information(IPv4Network('192.168.0.0/255.255.255.0'))


if __name__ == '__main__':
    main()

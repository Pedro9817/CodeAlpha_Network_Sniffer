import socket


def parse_packet(packet):
    if len(packet) < 20:
        return

    source = socket.inet_ntoa(packet[12:16])
    destination = socket.inet_ntoa(packet[16:20])
    protocol = packet[9]

    names = {1: "ICMP", 6: "TCP", 17: "UDP"}
    protocol_name = names.get(protocol, f"Other ({protocol})")

    print("\n" + "=" * 50)
    print(f"Source IP      : {source}")
    print(f"Destination IP : {destination}")
    print(f"Protocol       : {protocol_name}")
    print(f"Packet Size    : {len(packet)} bytes")

    payload = packet[20:52]

    if payload:
        print(f"Payload Preview: {payload.hex(' ')}")
    else:
        print("Payload Preview: None")


def main():
    print("=" * 50)
    print("CodeAlpha Basic Network Sniffer")
    print("Press Ctrl+C to stop.")
    print("=" * 50)

    try:
        temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp.connect(("8.8.8.8", 80))
        local_ip = temp.getsockname()[0]
        temp.close()

        print(f"Local IP: {local_ip}")

        sniffer = socket.socket(
            socket.AF_INET,
            socket.SOCK_RAW,
            socket.IPPROTO_IP
        )

        sniffer.bind((local_ip, 0))

        sniffer.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_HDRINCL,
            1
        )

        sniffer.ioctl(
            socket.SIO_RCVALL,
            socket.RCVALL_ON
        )

        print("Packet capture started...\n")

        while True:
            packet, address = sniffer.recvfrom(65535)
            parse_packet(packet)

    except PermissionError:
        print("Administrator privileges are required.")

    except OSError as error:
        print(f"Network capture error: {error}")

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")

    finally:
        try:
            sniffer.ioctl(
                socket.SIO_RCVALL,
                socket.RCVALL_OFF
            )
            sniffer.close()
        except:
            pass


if __name__ == "__main__":
    main()
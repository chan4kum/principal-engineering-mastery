"""Local example for A02.13. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

client_seq, server_seq = 10, 50
syn_ack = client_seq if broken else client_seq + 1
final_ack = server_seq + 1
print("handshake accepted in model:", syn_ack == 11 and final_ack == 51)

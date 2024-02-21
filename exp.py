import struct
# Format string: '<' for little-endian, 'I' for unsigned int (4 bytes)
packed_data = struct.pack('<I', 123)
print(packed_data)

# How to convert a byte array to a String? (solution)
def byte_array_to_string(byte_array, encoding="utf-8"):
    return byte_array.decode(encoding)

byte_array = b'hello'
print("Byte array:", byte_array)
print("String:", byte_array_to_string(byte_array))

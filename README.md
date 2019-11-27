# basestego
Steganography with base64

## Install
```
pip install basestego
```

## Usage:
```python
import basestego

# Fast encoding (uses base64 module)
# 2 is a number you want to hide
basestego.b64encode(b"bijereg", 2)  # Returns "YmlqZXJlZy=="

# Slow encoding (uses own implementation of base64)
basestego.b64encode(b"bijereg", 2, slow_mode=True)  # Returns "YmlqZXJlZy=="

# You can't write all you want.
# If you'll try to write more than allowed,
# ValueError will be raised.
basestego.b64encode(b"bijereg", 42)  # ValueError: Can't write 6 bits in the string.

# How much you can write?
basestego.get_allowed_bits(b"bijereg")  # Returns 4 (bits)

# Decoding
basestego.b64decode("YmlqZXJlZy==")  # Returns 2
```

## More examples
```python
import basestego


for i in range(4):
    encoded = basestego.b64encode(b"bijereg", i)
    decoded = basestego.b64decode(encoded)
    
    print(encoded)
    print(decoded, i, decoded == i)
    print()
```
Output:
```
YmlqZXJlZw==
0 0 True

YmlqZXJlZx==
1 1 True

YmlqZXJlZy==
2 2 True

YmlqZXJlZz==
3 3 True
```

## Credits
Sergey Belousov (bijereg@gmail.com)

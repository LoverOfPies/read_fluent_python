symbols = '$¢£¥€¤'

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(codes)

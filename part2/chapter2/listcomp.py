symbols = '$¢£¥€¤'

# обычный for
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# listcompl
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

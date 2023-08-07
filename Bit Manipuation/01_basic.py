def bitAnd():
    a = 0b1010
    b= 0b1100
    c= a& b
    print(bin(c))

def bitOr():
    a = 0b1010
    b = 0b1100
    c = a | b
    print(bin(c))

def bitXor():
    a = 0b1010
    b = 0b1100
    c = a ^ b
    print(bin(c))

def bitNot():
    a = 0b1010
    c = ~a
    print(bin(c))

def bitLeftShift():
    a = 0b1010
    c = a<<2
    print(bin(c))

def bitShiftRight():
    a = 0b1010
    c = a>>1
    print(bin(c))

print("bit and operation...")
bitAnd()
print("bit wise or operation..")
bitOr()
print("bit wise NOt operation...")
bitNot()
print("Bit wise Left Shift operation...")
bitLeftShift()
print("bit wise Right shift opearation...")
bitShiftRight()


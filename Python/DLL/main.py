import ctypes

libc = ctypes.CDLL('./cpp/MathLibrary/x64/Debug/MathLibrary.dll')

libc.fibonacci_init(int(1),int(1))

# while(True):
#     if libc.fibonacci_next() <= 0:
#         break
#     print(f'{libc.fibonacci_index()} : {libc.fibonacci_next()}')
# print(f'{libc.fibonacci_index() + 1} Fibonacci Sequence values fit in an unsinged 64-bit integer.')
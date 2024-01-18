import ctypes
NULL = 0
MB_OK = 0
MessageBoxA = ctypes.windll.user32.MessageBoxA
var = ctypes.c_bool(True)

MessageBoxA(NULL, ctypes.c_char_p(b"Hello from python."), ctypes.c_char_p(b"Alert"), MB_OK)
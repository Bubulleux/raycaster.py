from ctypes import *
import math

py_daxa = CDLL("./py_daxa.dll")
py_daxa.init.restype = POINTER(c_void_p)
py_daxa.update.restype = c_bool
py_daxa_ctx = py_daxa.init()
frame_i = 0
c = (0, 0, 0)
palette = ((95, 0, 95, 255), (128, 0, 128, 255), (135, 0, 135, 255), (135, 95, 135, 255), (175, 0, 175, 255), (175, 95, 175, 255), (175, 135, 175, 255), (215, 0, 215, 255), (215, 95, 215, 255), (215, 135, 215, 255), (215, 175, 215, 255), (255, 0, 255, 255), (255, 95, 255, 255), (255, 135, 255, 255), (255, 175, 255, 255), (255, 215, 255, 255), (255, 0, 215, 255), (215, 0, 175, 255), (175, 0, 135, 255), (255, 95, 215, 255), (135, 0, 95, 255), (255, 0, 175, 255), (215, 95, 175, 255), (255, 135, 215, 255), (215, 0, 135, 255), (175, 0, 95, 255), (255, 0, 135, 255), (175, 95, 135, 255), (255, 95, 175, 255), (215, 135, 175, 255), (255, 175, 215, 255), (215, 0, 95, 255), (255, 0, 95, 255), (215, 95, 135, 255), (255, 135, 175, 255), (255, 95, 135, 255), (0, 0, 0, 255), (95, 0, 0, 255), (128, 0, 0, 255), (135, 0, 0, 255), (175, 0, 0, 255), (215, 0, 0, 255), (255, 0, 0, 255), (8, 8, 8, 255), (18, 18, 18, 255), (28, 28, 28, 255), (38, 38, 38, 255), (48, 48, 48, 255), (58, 58, 58, 255), (68, 68, 68, 255), (78, 78, 78, 255), (88, 88, 88, 255), (95, 95, 95, 255), (135, 95, 95, 255), (175, 95, 95, 255), (215, 95, 95, 255), (255, 95, 95, 255), (96, 96, 96, 255), (102, 102, 102, 255), (118, 118, 118, 255), (128, 128, 128, 255), (135, 135, 135, 255), (175, 135, 135, 255), (215, 135, 135, 255), (255, 135, 135, 255), (138, 138, 138, 255), (148, 148, 148, 255), (158, 158, 158, 255), (168, 168, 168, 255), (175, 175, 175, 255), (215, 175, 175, 255), (255, 175, 175, 255), (178, 178, 178, 255), (188, 188, 188, 255), (192, 192, 192, 255), (198, 198, 198, 255), (208, 208, 208, 255), (215, 215, 215, 255), (255, 215, 215, 255), (218, 218, 218, 255), (228, 228, 228, 255), (238, 238, 238, 255), (255, 255, 255, 255), (255, 135, 95, 255), (215, 135, 95, 255), (255, 175, 135, 255), (255, 95, 0, 255), (215, 95, 0, 255), (175, 135, 95, 255), (255, 175, 95, 255), (215, 175, 135, 255), (255, 215, 175, 255), (255, 135, 0, 255), (175, 95, 0, 255), (215, 135, 0, 255), (215, 175, 95, 255), (255, 215, 135, 255), (255, 175, 0, 255), (135, 95, 0, 255), (255, 215, 95, 255), (175, 135, 0, 255), (215, 175, 0, 255), (255, 215, 0, 255), (95, 95, 0, 255), (128, 128, 0, 255), (135, 135, 0, 255), (175, 175, 0, 255), (215, 215, 0, 255), (255, 255, 0, 255), (135, 135, 95, 255), (175, 175, 95, 255), (215, 215, 95, 255), (255, 255, 95, 255), (175, 175, 135, 255), (215, 215, 135, 255), (255, 255, 135, 255), (215, 215, 175, 255), (255, 255, 175, 255), (255, 255, 215, 255), (215, 255, 0, 255), (175, 215, 0, 255), (135, 175, 0, 255), (215, 255, 95, 255), (95, 135, 0, 255), (175, 255, 0, 255), (175, 215, 95, 255), (215, 255, 135, 255), (135, 215, 0, 255), (95, 175, 0, 255), (135, 255, 0, 255), (135, 175, 95, 255), (175, 255, 95, 255), (175, 215, 135, 255), (215, 255, 175, 255), (95, 215, 0, 255), (95, 255, 0, 255), (135, 215, 95, 255), (175, 255, 135, 255), (135, 255, 95, 255), (0, 95, 0, 255), (0, 128, 0, 255), (0, 135, 0, 255), (0, 175, 0, 255), (0, 215, 0, 255), (0, 255, 0, 255), (95, 135, 95, 255), (95, 175, 95, 255), (95, 215, 95, 255), (95, 255, 95, 255), (135, 175, 135, 255), (135, 215, 135, 255), (135, 255, 135, 255), (175, 215, 175, 255), (175, 255, 175, 255), (215, 255, 215, 255), (95, 255, 135, 255), (95, 215, 135, 255), (135, 255, 175, 255), (0, 255, 95, 255), (0, 215, 95, 255), (95, 175, 135, 255), (135, 215, 175, 255), (95, 255, 175, 255), (175, 255, 215, 255), (0, 255, 135, 255), (0, 175, 95, 255), (0, 215, 135, 255), (95, 215, 175, 255), (135, 255, 215, 255), (0, 255, 175, 255), (0, 135, 95, 255), (95, 255, 215, 255), (0, 175, 135, 255), (0, 215, 175, 255), (0, 255, 215, 255), (0, 95, 95, 255), (0, 128, 128, 255), (0, 135, 135, 255), (95, 135, 135, 255), (0, 175, 175, 255), (95, 175, 175, 255), (135, 175, 175, 255), (0, 215, 215, 255), (95, 215, 215, 255), (135, 215, 215, 255), (175, 215, 215, 255), (0, 255, 255, 255), (95, 255, 255, 255), (135, 255, 255, 255), (175, 255, 255, 255), (215, 255, 255, 255), (0, 215, 255, 255), (0, 175, 215, 255), (0, 135, 175, 255), (95, 215, 255, 255), (0, 95, 135, 255), (0, 175, 255, 255), (95, 175, 215, 255), (135, 215, 255, 255), (0, 135, 215, 255), (0, 95, 175, 255), (0, 135, 255, 255), (95, 135, 175, 255), (135, 175, 215, 255), (95, 175, 255, 255), (175, 215, 255, 255), (0, 95, 215, 255), (0, 95, 255, 255), (95, 135, 215, 255), (135, 175, 255, 255), (95, 135, 255, 255), (0, 0, 95, 255), (0, 0, 128, 255), (0, 0, 135, 255), (95, 95, 135, 255), (0, 0, 175, 255), (95, 95, 175, 255), (135, 135, 175, 255), (0, 0, 215, 255), (95, 95, 215, 255), (135, 135, 215, 255), (175, 175, 215, 255), (0, 0, 255, 255), (95, 95, 255, 255), (135, 135, 255, 255), (175, 175, 255, 255), (215, 215, 255, 255), (135, 95, 255, 255), (135, 95, 215, 255), (175, 135, 255, 255), (95, 0, 255, 255), (95, 0, 215, 255), (135, 95, 175, 255), (175, 135, 215, 255), (175, 95, 255, 255), (215, 175, 255, 255), (135, 0, 255, 255), (95, 0, 175, 255), (135, 0, 215, 255), (175, 95, 215, 255), (215, 135, 255, 255), (175, 0, 255, 255), (95, 0, 135, 255), (215, 95, 255, 255), (135, 0, 175, 255), (175, 0, 215, 255), (215, 0, 255, 255))
l_pal = len(palette)

def calc_pixel(xi, yi):
    global py_daxa
    global frame_i
    global c
    global l_pal
    c = palette[(frame_i + xi + yi)%l_pal]
    py_daxa.set_pixel(py_daxa_ctx, xi, yi, PyDaxaColor(c[0], c[1], c[2]))


CALLBACK_TYPE = CFUNCTYPE(None, c_int, c_int)
callback = CALLBACK_TYPE(calc_pixel)


class PyDaxaColor(Structure):
    _fields_ = [("r", c_byte), ("g", c_byte), ("b", c_byte)]


while 1:
    is_closed = py_daxa.update(py_daxa_ctx)
    if is_closed:
        break

    frame_i = frame_i + 1

    py_daxa.fill(py_daxa_ctx, callback)

    py_daxa.draw(py_daxa_ctx)


py_daxa.deinit(py_daxa_ctx)
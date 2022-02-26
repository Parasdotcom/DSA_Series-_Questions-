import ctypes
null_ptr = ctypes.c_void_p()
pa_stream_peek(stream, null_ptr, ctypes.c_ulong(length))
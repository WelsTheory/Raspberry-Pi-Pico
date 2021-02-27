import machine
import utime
import _thread

rojo = machine.Pin(13, machine.Pin.OUT)
verde = machine.Pin(11, machine.Pin.OUT)

sinc = _thread.allocate_lock()

def ledVerde():
    while True:
        sinc.acquire()
        verde.value(1)
        utime.sleep(0.1)
        verde.value(0)
        utime.sleep(0.1)
        sinc.release()

_thread.start_new_thread(ledVerde,())

while True:
    sinc.acquire()
    rojo.value(1)
    utime.sleep(0.5)
    rojo.value(0)
    utime.sleep(0.5)
    sinc.release()
    
    
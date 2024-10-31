from pymem import *
from pymem.process import *
from pymem.exception import *
from settings import *

pm = Pymem("FarCry6.exe")
module = module_from_name(pm.process_handle,process).lpBaseOfDll

def getPointer(base, offsets):
    addr = pm.read_ulonglong(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = pm.read_ulonglong(addr + offset)
    addr += offsets[-1]
    return addr


while True:
    try:
        pm.write_float(getPointer(module + endereco,offset),1000.0)
        print("\r[*] injetado!")
    except Exception as e:
        print(f"Erro de execução: {e}")
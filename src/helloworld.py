import os, sys
import platform
from ssl import OPENSSL_VERSION
import struct

from cryptography.hazmat.backends.openssl import backend

if os.environ.get('STATICX_PROG_PATH', False):
    execution_type = 'staticx'
elif getattr(sys, 'frozen', False):
    execution_type = 'pyinstaller'
else:
    execution_type = 'pythonsource'

proc = platform.processor()
machine = platform.machine()
bitness = struct.calcsize("P") * 8

print(f'Python: {platform.python_version()}')
print(f'OpenSSL: {OPENSSL_VERSION}')
print(f'Execution type: {execution_type}')
print(f'Platform: {platform.platform()}')
print(f'Processor: {proc}')
print(f'Machine: {machine}')
print(f'Python Bits: {bitness}')
print(f'Cryptography Backend: {backend.openssl_version_text()}')

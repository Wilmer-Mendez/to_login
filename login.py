from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

if hasattr(__builtins__, 'raw_input'):
  input = raw_input

import fileinput
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--hide', action='store_true')
args = parser.parse_args()


ML_USERNAME = '80b95090-a78f-4e74-8c7d-52d63a360e7c'
ML_PASSWORD = '9b20f8cf-90b4-4547-9965-0ad6d3a401bb'
ML_INSTANCE = 'c2087c96-0276-4fd3-b74a-9888481c6017'
ACCESS_KEY_ID = '335db1dc8d2543d3b01aa4e79d5dcd44'
SECRET_ACCESS_KEY = 'a3cb74305e610f04dbfcd531cb04a43c80f1a408a901bf6c'

CREDENTIALS = '.credentials_wml'

with open(CREDENTIALS, 'w') as file:
  file.write('ML_USERNAME={}\n'.format(ML_USERNAME))
  file.write('ML_PASSWORD={}\n'.format(ML_PASSWORD))
  file.write('ML_INSTANCE={}\n'.format(ML_INSTANCE))
  file.write('ACCESS_KEY_ID={}\n'.format(ACCESS_KEY_ID))
  file.write('SECRET_ACCESS_KEY={}\n'.format(SECRET_ACCESS_KEY))

print("\033[92mSuccessfully set credentials!\033[0m")

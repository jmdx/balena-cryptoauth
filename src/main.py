from time import sleep

from cryptoauthlib import *

ATCA_SUCCESS = 0x00
load_cryptoauthlib()
cfg = cfg_ateccx08a_i2c_default()
cfg.cfg.atcai2c.bus = 1
init_success = atcab_init(cfg) == ATCA_SUCCESS
info = bytearray(4)
init_success = init_success and atcab_info(info) == ATCA_SUCCESS
print('init sucess?', init_success)
if init_success:
    dev_name = get_device_name(info)
    dev_type = get_device_type_id(dev_name)

    print('success, device name:', dev_name, ', device type:', dev_type)
atcab_release()

while True:
    sleep(1)
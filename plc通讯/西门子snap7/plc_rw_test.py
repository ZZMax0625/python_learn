# -*- coding: utf-8 -*-
from numpy import byte

from app.adapter import plc_access
import time
import snap7
from snap7.exceptions import Snap7Exception
from app import current_app
from app.model.base_models import Device
from setting import DevelopConfig, ProductConfig
import json
from struct import pack, unpack

if __name__ == "__main__":

    current_app.config_from_class(ProductConfig)
    current_app.init_app(app_name="zzmax01")
    current_app.init_db()

    _device = current_app.db_session.query(Device).all()

    print(type(_device))

    data = []

    for item in _device:
        _dict = {
            "device_id": item.device_id,
            "connect_info": json.loads(item.connect_info)
        }
        data.append(_dict)

    print(data[0].get("device_id"))
    print(data[0].get("connect_info"))
    print(data[0].get("connect_info").get("ip_address"))

    print("plc连接demo")

    # 从数据库中读取ip，连接plc
    plc_access.connect(data[0].get("connect_info").get("ip_address"), 0, 0, False)

    snap7_client = plc_access.client.get("192.168.0.1/0/0")

    # 查看plc是否连接成功
    print(plc_access.is_connected(data[0].get("connect_info").get("ip_address"), 0, 0, False))

    # print(plc_access.read_data("192.168.1.20", 0, 0, "DB1", 70, 1, 100, False))

    str_data = bytearray([254, len("hello world")] + [ord(letter) for letter in "hello world"])

    count = snap7.util.get_int(snap7_client.db_read(1, 0, 2), 0)
    temperature = snap7.util.get_real(snap7_client.db_read(1, 2, 4), 0)
    comm_status = snap7.util.get_bool(snap7_client.db_read(1, 6, 1), 0, 0)
    # desc = snap7.util.get_string(snap7_client.db_read(1, 8, 12), 0)
    desc = snap7.util.get_string(snap7_client.read_area(snap7.types.Areas.DB, 1, 8, 254), 0)

    # print("从plc中读取的字符串")
    # print(snap7_client.db_read(1, 8, 254))
    # print(snap7_client.db_read(1, 8, 254)[1])
    # print(chr(snap7_client.db_read(1, 8, 254)[1]))
    # for item in snap7_client.db_read(1, 8, 254)[2:]:
    #     print(item)
    #     print(str(item) + "转义后")
    #     print(chr(item))
    #     # for i in str(item):
    #     #     print(i + "转义后")
    #     #     print(chr(i))
    # print(desc)
    # data = snap7_client.read_area(snap7.types.Areas.DB, 1, 8, 254)
    # print(data)
    # print(data[1:].decode("utf-8"))

    current_app.logger.info("plc数据读取")

    print("==========plc数据读取==========")
    print("计数器：" + str(count))
    print("温度：" + str(round(temperature, 2)))
    print("状态：" + str(comm_status))
    print("描述：" + str(desc))

    print("==========plc数据写入==========")

    # plc数据修改
    count = 65
    temperature = 36.87
    comm_status = False
    desc = 'Hello World2222222'

    # # 更改int
    # snap7_client.db_write(1, 0, count.to_bytes(2, "big"))
    #
    # # 更改float
    # snap7_client.db_write(1, 2, snap7.util.set_real(bytearray(4), 0, temperature))
    #
    # # 更改bool值
    # snap7_client.db_write(1, 6, bytearray(False))

    # 更改字符串
    # data1 = bytearray(254)
    # data1[0] = 254
    # data1[1] = 9
    # data1[2] = 48
    # data1[3] = 49
    # data1[4] = 50
    # data1[5] = 207
    # data1[6] = 200
    # data1[7] = 72
    # data1[8] = 73
    # data1[9] = 189
    # data1[10] = 248
    # # data1[0] = 254
    # print(data1)
    # snap7_client.write_area(snap7.types.Areas.DB, 1, 8, data1)


    # print(type(buffer))
    # print(type(buffer[0]))
    #
    # buffer[0] = 254
    # print(buffer.decode("utf-16"))
    # snap7_client.write_area(snap7.types.Areas.DB, 1, 8, buffer)



    # print("A 经过utf-16编码后")
    # test = "A"
    # data = bytearray(test, encoding='utf-16')
    # print(data)
    # data[0] = 254
    # print(data)
    #
    # snap7_client.write_area(snap7.types.Areas.DB, 1, 8, data)

    # buffer = bytearray("\xfe\03".join("qzk"))
    # snap7_client.write_area(snap7.types.Areas.DB,1,8,buffer)

    # print(type(snap7_client.db_read(1, 8, 6)))
    # print(snap7_client.db_read(1, 9, 6))
    # # snap7_client.db_write(1,8,snap7_client.db_read(1, 8, 11))
    # #
    # data = bytearray(20)
    # snap7.util.set_string(data, 0, "test", 255)
    # print(data)
    # # snap7_client.db_write(1, 264, data)

    # data = bytearray(20)
    # snap7.util.set_string(data, 0, desc, 255)
    # print(data)
    # # snap7.util.set_string(data, 0, desc, 255)
    # # print(data)
    # # snap7_client.db_write(1,8,data)
    # # print(type(snap7.types.Areas.DB))
    # # print(type(snap7.client.Areas.DB))
    # snap7_client.write_area(snap7.types.Areas.DB,1,8,data)

    #
    # plcObj = snap7.client.Client();
    #
    # plcObj.connect('192.168.1.21',0,0);
    #
    # print(plcObj.get_connected())
    #
    # data = plcObj.db_read(12,0,255)
    #
    # print(data)
    #
    # print(data.decode('utf-16'))
    #
    #
    # plcObj.disconnect();
    #
    # print(plcObj.get_connected())

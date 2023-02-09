#-*-coding:utf-8-*-

# from modbus_tk import modbus_tcp
# import modbus_tk.defines as cst
#
# from numpy import byte
#
# from app.adapter import plc_access
# import time
# import snap7
# from snap7.exceptions import Snap7Exception
# from app import current_app
# from app.model.base_models import Device
# from setting import DevelopConfig, ProductConfig
# import json
# from struct import pack, unpack
#
# if __name__ == "__main__":
#
#     current_app.config_from_class(ProductConfig)
#     current_app.init_app(app_name="zzmax01")
#     current_app.init_db()
#
#     _device = current_app.db_session.query(Device).all()
#
#     print(type(_device))
#
#     data = []
#
#     for item in _device:
#         _dict = {
#             "device_id": item.device_id,
#             "connect_info": json.loads(item.connect_info)
#         }
#         data.append(_dict)
#
#     print(data[1].get("device_id"))
#     print(data[1].get("connect_info"))
#     print(data[1].get("connect_info").get("ip_address"))
#
#     print("logo连接demo")
#
#     server = modbus_tcp.TcpMaster(data[1].get("connect_info").get("ip_address"), 502)
#     server.set_timeout(1.0)
#
#     # 读保持寄存器 03H 1站号 地址0 长度0-10
#     res1 = server.execute(1, cst.READ_COILS, 8193, 10)
#
#     print(res1)
#
#


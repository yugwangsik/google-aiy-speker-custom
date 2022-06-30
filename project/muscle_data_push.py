import asyncio
import struct
import time
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import requests


#address = "E4:27:42:CA:AA:E5"
address = "C2:6B:78:BB:76:90"
#address = "CC:AE:7F:D3:7D:08"
read_data = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"


def notify_callback(sender: int, data: bytearray):
    cnt = len(data)
    t = data
    t = t.decode('utf-8')
    t = t.replace(" ", "")

    print('plus value')
    print(t)
    print('===============================================================================================')
    plus_data = t
    url = "http://hangyu.pe.kr:9876/auth_m/keyword"
    datas = {'plus':plus_data}
    requests.post(url, json=datas)

#async def run(address, uuid, status):
async def run(address):
    async with BleakClient(address) as client:
        print('connected')
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                #if characteristic.uuid == uuid:
                if characteristic.uuid == read_data:
                    if 'notify' in characteristic.properties:
                        #while status == True:
                        while True:
                            await client.start_notify(characteristic, notify_callback)




    print('disconnect')

#def main(address, uuid, status):
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(run(address))
#    print('done')

#def main(address, uuid, status):
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')

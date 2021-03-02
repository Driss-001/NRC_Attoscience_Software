import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

for p in ports:
    if "Silicon Labs" in p.description:
        print (p.name)
from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
temperatura= sensor.get_obj_temp()
print ("Tu temperatura actual es :", temperatura)
bus.close()

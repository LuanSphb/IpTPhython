import serial
import time

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Aguarda o Arduino resetar
time.sleep(2)

def read_soil_moisture():
    if arduino.in_waiting > 0:
        try:
            moisture_value = int(arduino.readline().decode().strip())
            return moisture_value
        except ValueError:
            return None

def control_leds(moisture_value):
    if moisture_value is not None:
        if moisture_value < 50:
            arduino.write(b'2H')  # Liga LED no pino 2
            arduino.write(b'3L')  # Desliga LED no pino 3
        else:
            arduino.write(b'2L')  # Desliga LED no pino 2
            arduino.write(b'3H')  # Liga LED no pino 3

try:
    while True:
        soil_moisture = read_soil_moisture()
        if soil_moisture is not None:
            print(f'Soil Moisture: {soil_moisture}')
        control_leds(soil_moisture)
        time.sleep(0.01)  # Delay para simular a mesma performance

except KeyboardInterrupt:
    print("Programa interrompido")
finally:
    arduino.close()
import serial
import time

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Aguarda o Arduino resetar
time.sleep(2)

def read_temperature():
    if arduino.in_waiting > 0:
        try:
            data = arduino.readline().decode().strip()
            if "degrees C" in data:
                temperature_value = float(data.split()[0])
                return temperature_value
        except ValueError:
            return None

try:
    while True:
        temperatureC = read_temperature()
        if temperatureC is not None:
            print(f'Temperature: {temperatureC} degrees C')
        time.sleep(0.1)  # Delay para simular a mesma performance

except KeyboardInterrupt:
    print("Programa interrompido")
finally:
    arduino.close()
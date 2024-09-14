import serial
import time

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Aguarda o Arduino resetar
time.sleep(2)

def read_force_value():
    if arduino.in_waiting > 0:
        try:
            force_val = int(arduino.readline().decode().strip())
            return force_val
        except ValueError:
            return None

def control_led(force_val):
    if force_val is not None:
        if force_val > 400:
            arduino.write(b'H')  # Envia comando para acender o LED
        else:
            arduino.write(b'L')  # Envia comando para apagar o LED

try:
    while True:
        force_value = read_force_value()
        if force_value is not None:
            print(f'Force Sensor Value: {force_value}')
        control_led(force_value)
        time.sleep(0.01)  # Pequeno delay para melhorar a performance

except KeyboardInterrupt:
    print("Programa interrompido")
finally:
    arduino.close()
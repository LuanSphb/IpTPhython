import serial
import time

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Aguarda o Arduino resetar
time.sleep(2)

def read_ultrasonic_distance():
    if arduino.in_waiting > 0:
        try:
            distance = float(arduino.readline().decode().strip())
            return distance
        except ValueError:
            return None

def control_leds(distance):
    if distance is not None:
        if distance <= 50:
            arduino.write(b'8H')  # Liga LED no pino 8
        else:
            arduino.write(b'8L')  # Desliga LED no pino 8

        if distance <= 75:
            arduino.write(b'9H')  # Liga LED no pino 9
        else:
            arduino.write(b'9L')  # Desliga LED no pino 9

        if distance <= 100:
            arduino.write(b'10H')  # Liga LED no pino 10
        else:
            arduino.write(b'10L')  # Desliga LED no pino 10

try:
    while True:
        distance_value = read_ultrasonic_distance()
        if distance_value is not None:
            print(f'Distance: {distance_value} cm')
        control_leds(distance_value)
        time.sleep(0.01)  # Delay para simular a mesma performance

except KeyboardInterrupt:
    print("Programa interrompido")
finally:
    arduino.close()
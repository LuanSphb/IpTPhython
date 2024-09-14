import serial
import time

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

# Aguarda o Arduino resetar
time.sleep(2)

def read_sensor_value():
    if arduino.in_waiting > 0:
        try:
            sensor_val = int(arduino.readline().decode().strip())
            return sensor_val
        except ValueError:
            return None

def control_pwm(sensor_val):
    if sensor_val is not None:
        pwm_value = int(sensor_val / 1023 * 255)  # Mapeia o valor do sensor para 0-255
        arduino.write(f'{pwm_value}\n'.encode())  # Envia o valor do PWM para o Arduino

try:
    while True:
        sensor_value = read_sensor_value()
        if sensor_value is not None:
            print(f'Sensor Value: {sensor_value}')
        control_pwm(sensor_value)
        time.sleep(0.1)  # Delay para simular a mesma performance

except KeyboardInterrupt:
    print("Programa interrompido")
finally:
    arduino.close()
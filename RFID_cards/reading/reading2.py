import serial

ser = serial.Serial(
    port='COM15',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

card_store = open('card_store.txt', 'r').read().split('\n')

ser.flush()

if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()

            # print(f"Line: {line} \n")

            if line.startswith('[checking]: '):
                line = line.replace('[checking]: ', '')
                id = line.rstrip().lstrip()
                
                print(f"Id: {id}\n")
                resp = "granted" if id in card_store else "denied"
                ser.write(resp.encode())
                print(f"Access: {resp}\n")
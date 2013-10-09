import serial
import sqlite3
import time

con = sqlite3.connect('site.db')

# ser = serial.Serial('COM1', 9600)
ser = serial.Serial('/dev/tty.Bluetooth-Serial-1', 9600)


def update_content(con, line_value):
    vagas = line_value.split(',')
    for i in vagas:
        vaga = i[:2]
        status = i[-1]
        con.execute('UPDATE vagas set status=? where vaga=?', (status, vaga))
    con.commit()


while True:
    message = ser.readline()
    if message:
        update_content(con, message)
        time.sleep(30)
    print(message)

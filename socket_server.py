# coding=utf-8
import serial
import sqlite3

# carrega o banco de dados SQLite
con = sqlite3.connect('site.db')



def update_content(con, line_value):
    # remove Linhas 1 do texto da serial
    vagas = line_value.replace('Linha 1: ', '').strip()
    # remove Linhas 2 do texto da serial
    vagas = vagas.replace('Linha 2: ', '').strip()
    vagas = vagas.replace(' \r\n', '').strip()
    # remove ultima virgula do texto se ouver
    vagas = vagas.rstrip(',')
    # transforma o texto em uma lista de vagas
    vagas = vagas.split(',')
    # mostra a lista que vai ser alterada
    print vagas

    for i in vagas:
        if not i:
            # caso i seja nulo ir para o próximo valor
            continue
        # pega uma vaga
        vaga = i[:2]
        # pega um status de uma vaga
        status = i[-1]
        # altera a tabela do banco de dados
        con.execute('UPDATE vagas set status=? where vaga=?', (status, vaga))
        # salva as modificações
        con.commit()


# loop infinito
while True:

    # conecta com a serial
    ser = serial.Serial('COM10', 9600)

    # le uma linha da serial
    message = ser.read(69)

    # se exister mensagem altera a tabela de status
    if message:
        # mostra a mensagem recebida pela serial
        print message
        # altera o status da tabela
        update_content(con, message)

    ser.close()



# coding=utf-8
from bottle import route, run, install, template, error, static_file
from bottle_sqlite import SQLitePlugin

# carrega o banco de dados pelo plugin do Bottle
install(SQLitePlugin(dbfile='site.db'))


@error(404)
def error404(error):
    # pagina de erros
    return 'Nothing here, sorry'


@route('/static/<filename:path>')
def send_static(filename):
    # pagina de arquivos staticos: css, img ...
    return static_file(filename, root='./static/')


@route('/')
def home(db, vaga=None):
    if not vaga:
        # mostra todas as vagas
        query = db.execute('SELECT * FROM vagas')
    else:
        # mostra apenas uma vaga em especial
        query = db.execute('SELECT * FROM vagas WHERE vaga = ?', (vaga,))

    # transforma o conteudo SQL em uma lista de dados
    rows = query.fetchall()

    # conta quantas vagas estão livres
    query = db.execute('SELECT count(id) FROM vagas where status=0')
    vagas_ocupadas = query.fetchone()

    # conta o total de vagas
    query = db.execute('SELECT count(id) FROM vagas')
    vagas_total = query.fetchone()

    # monta mesagem padrão para ser exibida no template
    mensagem = "{0} vagas livres de {1} vagas".format(vagas_ocupadas[0], vagas_total[0])

    # envia os dados para o template
    return template('vagas_bo', vagas=rows, vagas_mensagem=mensagem)

# inicia o webserver do bottle com debug na porta 8080
run(host='0.0.0.0', port=8080, debug=False, server='paste')

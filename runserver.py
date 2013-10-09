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
        c = db.execute('SELECT * FROM vagas')
    else:
        # mostra apenas uma vaga em especial
        c = db.execute('SELECT * FROM vagas WHERE vaga = ?', (vaga,))

    # transforma o conteudo SQL em uma lista de dados
    rows = c.fetchall()

    # envia os dados para o template
    return template('vagas', vagas=rows)

run(host='0.0.0.0', port=8080, debug=True)


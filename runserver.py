from bottle import route, run, install, template, error, static_file
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='site.db'))


@error(404)
def error404(error):
    return 'Nothing here, sorry'


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')


@route('/')
def home(db, post_id=None):
    if not post_id:
        c = db.execute('SELECT * FROM vagas')
    else:
        c = db.execute('SELECT * FROM vagas WHERE id = ?', (post_id,))

    rows = c.fetchall()

    return template('vagas', vagas=rows)

run(host='0.0.0.0', port=8080, debug=True)


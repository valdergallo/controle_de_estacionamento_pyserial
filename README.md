Vagas
=====

Controle de vagas de estacionamento com saída para website.


Requerimentos
=============

* Python 2.7 (http://www.python.org/download/releases/2.7.5/)
* SetupTools (https://pypi.python.org/pypi/setuptools)
* Pyserial (http://pyserial.sourceforge.net/)
* Bottle (http://bottlepy.org/)
* Bottle SQLite (http://bottlepy.org/docs/dev/plugins/sqlite.html)


Instalar Python no Windows
==========================

Download do Python 32bits 2.7

* Python on Windows (http://docs.python.org/2/using/windows.html)

Após a instalação do Python é preciso adicionar o diretório do Python e o dos Scripts no Path do Windows.

* Abrir o "Painel de Controle" do Windows
* Entrar em "Sistema" e clicar na opção "Configurações avançadas do sistema"
* Na aba "Avançado", clicar no botão "Variáveis de Ambiente"
* Selecionar a variável do sistema "Path" e clicar no botão "Editar..."
* Adicionar o diretório de instalação do Python na caixa de texto

Normalmente o diretório do Python é:

```
C:\Python;C:\Python\Scripts;
```

Instalar o Setuptools
=====================

Download do Setuptools versão 32bits do Python 2.7 para Windows.

* SetupTools (https://pypi.python.org/pypi/setuptools)


Instalar pacotes
================

```
easy_install pip
```

Você precisa ir até o diretório onde está o projeto e executar o comando:

```
pip install -r requirements.txt
```


Executar WebServer
=============

```
python runserver.py
```

Executar SocketServer
================

```
python socket_server.py
```

Listar portas
=============

```
python -m serial.tools.list_ports
```

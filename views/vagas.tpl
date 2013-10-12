<html>
<head>
  <title>Vagas</title>
  <link rel="stylesheet" href="static/base.css" type="text/css">
  <meta http-equiv="refresh" content="1" />
</head>
<body>

<h1>Lista de Vagas</h1>

<ul>
  % for vaga in vagas:
    <li class=''><span> {{vaga[1]}} </span> |
    % if vaga[2] == 1:
        <span class='ocupado'>Ocupada</span>
    % end
    % if vaga[2] == 0:
        <span class='livre'>Livre</span>
    % end
    | {{vaga[3]}} </li>
  % end
</ul>

</body>
</html>

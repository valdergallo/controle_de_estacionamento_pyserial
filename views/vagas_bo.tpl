<html>
<head>
  <title>Vagas</title>
  <link rel="stylesheet" href="static/base.css" type="text/css">
  <script type="text/JavaScript">
    <!--
    function timedRefresh(timeoutPeriod) {
        setTimeout("location.reload(true);",timeoutPeriod);
    }
    //   -->
</script>
</head>
<body onload="JavaScript:timedRefresh(2000);">

<h1>Lista de Vagas</h1>


<div class='content'>
% for vaga in vagas:

<div class='box
    % if vaga[2] == 1:
        ocupado'>
        {{vaga[1]}} </br>
        Ocupada
    % end
    % if vaga[2] == 0:
        livre'>
        {{vaga[1]}} </br>
        Livre
    % end
</div>

% if vaga[0] % 6 == 0:
</div>

% if vaga[0] != 12:
<div class='content-min'>
<h4>{{ vagas_mensagem }}</h4>
</div>
% end

<div class='content'>

%end

% end

</body>
</html>

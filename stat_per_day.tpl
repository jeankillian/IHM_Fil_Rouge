<!doctype html>
<html lang="fr">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <link rel="stylesheet" href="..\media\Css.v2.css">

    <title>Gameserver</title>
</head>
<body>
    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">Machine</th>
          <th scope="col">date</th>
          <th scope="col">nb parties</th>
          <th scope="col">moyenne temps partie</th>
          <th scope="col">win P1</th>
          <th scope="col">win P2</th>
          <th scope="col">Draw</th>
        </tr>
      </thead>
      <tbody>
      % for item in liste:
        <tr>
          <th scope="row">{{item}}</th>
          <td>{{item.date}}</td>
          <td>{{item.nb_partie}}</td>
          <td>{{item.moyenne_partie}}</td>
          <td>{{item.win_count_joueur1}}</td>
          <td>{{item.win_count_joueur2}}</td>
          <td>{{item.draw_count}}</td>
        </tr>
       %end
      </tbody>
    </table>
    </body>
</html>
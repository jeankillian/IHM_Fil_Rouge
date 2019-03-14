
<body>
<table class="table table-striped table-dark">
  <thead>
  <h1>{{machine}}</h1>
    <tr>
      <th scope="col">Heure de départ</th>
      <th scope="col">Temps de partie</th>
      <th scope="col">Winner</th>
    </tr>
  </thead>
  <tbody>
  % for item in liste:
    <tr>
      <th scope="row">{{item.start_time}}</th>
      <td>{{item.game_time}}</td>
      <td>{{item.winner}}</td>
    </tr>
   %end
  </tbody>
</table>
</body>
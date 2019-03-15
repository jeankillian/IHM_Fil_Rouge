<body>
<table class="table table-striped table-dark">
  <thead>
  <h1>Last Game Result</h1>
    <tr>
      <th scope="col">msg_id</th>
      <th scope="col">Message</th>
      <th scope="col">Date</th>
      <th scope="col">Duration</th>
      <th scope="col">Winner</th>
    </tr>
  </thead>
  <tbody>
  %
    <tr>
      <th scope="row">{{last_game.msg_id}}</th>
      <td>{{last_game.jeu}}</td>
      <td>{{last_game.start_time}}</td>
      <td>{{last_game.get_game_duration()}}</td>
      <td>{{last_game.winner}}</td>
    </tr>
   %end
  </tbody>
</table>
</body>
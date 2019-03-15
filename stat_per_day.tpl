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
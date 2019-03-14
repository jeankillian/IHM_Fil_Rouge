
<body>
<table class="table table-striped table-dark">
  <thead>
    <tr>
      <th scope="col">Machine</th>
      <th scope="col">Adresse IP</th>
      <th scope="col">Jeu</th>
    </tr>
  </thead>
  <tbody>
  % for item in liste:
    <tr>
      <th scope="row">{{item}}</th>
      <td>{{item.adresse_ip}}</td>
      <td>{{item.jeu}}</td>
    </tr>
   %end

  </tbody>
</table>
</body>
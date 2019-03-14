
<body>
<table class="table table-striped table-dark">
  <thead>
  <h1>{{machine}}</h1>
    <tr>
      <th scope="col">msg_id</th>
      <th scope="col">Message</th>
      <th scope="col">Date</th>
    </tr>
  </thead>
  <tbody>
  % for item in liste:
    <tr>
      <th scope="row">{{item.msg_id}}</th>
      <td>{{item.message}}</td>
      <td>{{item.created_date}}</td>
    </tr>
   %end
  </tbody>
</table>
</body>
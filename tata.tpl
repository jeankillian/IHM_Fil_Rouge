<table>
    <tbody>
        <td>
            % for item in liste:
                <li>{{item}}</li>
            % end
        </td>
        <td>
            % for item in liste:
                <li>{{item.adresse_ip}}</li>
            % end
        </td>
        <td>
            % for item in liste:
                <li>{{item.jeu}}</li>
            % end
        </td>
     </tboy>
</table>

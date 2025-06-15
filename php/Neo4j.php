<?php
// Neo4j login and endpoint
$url = 'http://neo4j:7474/db/neo4j/tx/commit';
$username = 'neo4j';
$password = 'password';

// Cypher query: Vehicle goes FROM Point A TO Point B
$query = array(
    'statements' => array(
        array(
            'statement' => 'MATCH (a:Point)<-[:FROM]-(v:Vehicle)-[:TO]->(b:Point) RETURN v.car_id, a.name, b.name'
        )
    )
);

// Send request to Neo4j REST API
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_USERPWD, $username . ":" . $password);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($query));

$response = curl_exec($ch);
curl_close($ch);

// Decode JSON response
$data = json_decode($response, true);
$rows = $data['results'][0]['data'];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Car Routes</title>
</head>
<body>
    <h2>Car Routes (Neo4j)</h2>
    <table>
        <tr><th>Car ID</th><th>Point A</th><th>Point B</th></tr>
        <?php
        foreach ($rows as $row) {
            $car     = $row['row'][0];
            $point_a = $row['row'][1];
            $point_b = $row['row'][2];
            echo "<tr><td>$car</td><td>$point_a</td><td>$point_b</td></tr>";
        }
        ?>
    </table>
</body>
</html>

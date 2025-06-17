<?php

$manager = new MongoDB\Driver\Manager("mongodb://mongodb:27017");
$query = new MongoDB\Driver\Query([]);
$cursor = $manager->executeQuery("fleet_data.car_locations", $query);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Car GPS Locations</title>
</head>
<body>
    <table>
        <tr><th>Car ID</th><th>Latitude</th><th>Longitude</th></tr>
        <?php
        foreach ($cursor as $doc) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($doc->car_id ?? '') . "</td>";
            echo "<td>" . htmlspecialchars($doc->latitude ?? '') . "</td>";
            echo "<td>" . htmlspecialchars($doc->longitude ?? '') . "</td>";
            echo "</tr>";
        }
        ?>
    </table>
</body>
</html>

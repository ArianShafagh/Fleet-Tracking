<?php
// Connect to MongoDB (default Docker host and port)
$manager = new MongoDB\Driver\Manager("mongodb://mongodb:27017");

// Query everything from fleet_data.car_locations collection
$query = new MongoDB\Driver\Query([]);
$cursor = $manager->executeQuery("fleet_data.car_locations", $query);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Car GPS Locations</title>
    <style>
        table { border-collapse: collapse; width: 80%; margin: 20px auto; }
        th, td { border: 1px solid gray; padding: 8px; text-align: center; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Car Locations (MongoDB)</h2>
    <table>
        <tr><th>Car ID</th><th>Latitude</th><th>Longitude</th><th>Timestamp</th></tr>
        <?php
        foreach ($cursor as $doc) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($doc->car_id ?? '') . "</td>";
            echo "<td>" . htmlspecialchars($doc->latitude ?? '') . "</td>";
            echo "<td>" . htmlspecialchars($doc->longitude ?? '') . "</td>";
            echo "<td>" . htmlspecialchars($doc->timestamp ?? '') . "</td>";
            echo "</tr>";
        }
        ?>
    </table>
</body>
</html>

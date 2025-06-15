<?php
$host = 'mysql';
$port = 3306;
$user = 'root';
$pass = 'root';
$db   = 'fleet_data';

$conn = new mysqli($host, $user, $pass, $db, $port);

$sql = "SELECT * FROM fleet_tracking ORDER BY timestamp DESC";
$result =mysqli_query($conn,$sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Fleet Speed Dashboard</title>
</head>
<body>
    <h1>Fleet Tracking - Speed Logs</h1>
    <table>
        <tr>
            <th>Car ID</th>
            <th>Speed (km/h)</th>
            <th>Status</th>
            <th>Timestamp</th>
        </tr>
        <?php if ($result && $result->num_rows > 0): ?>
            <?php while($row = $result->fetch_assoc()): ?>
                <tr>
                    <td><?= htmlspecialchars($row['car_id']) ?></td>
                    <td><?= htmlspecialchars($row['speed']) ?></td>
                    <td><?= htmlspecialchars($row['status']) ?></td>
                    <td><?= htmlspecialchars($row['timestamp']) ?></td>
                </tr>
            <?php endwhile; ?>
        <?php else: ?>
            <tr><td colspan="5">No data available</td></tr>
        <?php endif; ?>
    </table>

</body>
</html>

<?php mysqli_close($conn); ?>

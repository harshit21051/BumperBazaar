<!DOCTYPE html>
<html>
<head>
    <title>Address Table</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
</head>
<body>
    <h2>Address</h2>
    <table>
        <tr>
            <th>CustID</th>
            <th>House</th>
            <th>Street</th>
            <th>City</th>
        </tr>

        <?php
            $servername = "localhost";
            $username = "root";
            $password = "root";
            $dbname = "bumper_bazaar";

            // Create connection
            $conn = new mysqli($servername, $username, $password, $dbname);

            // Check connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Retrieve data from address table
            $sql = "SELECT * FROM address";
            $result = $conn->query($sql);

            // Loop through each row of data
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>".$row['CustID']."</td>";
                echo "<td>".$row['House']."</td>";
                echo "<td>".$row['Street']."</td>";
                echo "<td>".$row['City']."</td>";
                echo "</tr>";
            }

            // Close the connection
            $conn->close();
        ?>

    </table>
</body>
</html>
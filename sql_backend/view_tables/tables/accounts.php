<!DOCTYPE html>
<html>
<head>
    <title>Accounts Table</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
</head>
<body>
    <h2>Accounts</h2>
    <table>
        <tr>
            <th>CustID</th>
            <th>Username</th>
            <th>Password</th>
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

            // Retrieve data from accounts table
            $sql = "SELECT * FROM accounts";
            $result = $conn->query($sql);

            // Loop through each row of data
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>".$row['CustID']."</td>";
                echo "<td>".$row['Username']."</td>";
                echo "<td>".$row['Password']."</td>";
                echo "</tr>";
            }

            // Close the connection
            $conn->close();
        ?>

    </table>
</body>
</html>
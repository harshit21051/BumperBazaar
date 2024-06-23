<!DOCTYPE html>
<html>
<head>
    <title>Orders Table</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
</head>
<body>
    <h2>Orders</h2>
    <table>
        <tr>
            <th>OrderID</th>
            <th>CustID</th>
            <th>PayMode</th>
            <th>Amount</th>
            <th>Status</th>
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

            // Retrieve data from orders table
            $sql = "SELECT * FROM orders";
            $result = $conn->query($sql);

            // Loop through each row of data
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>".$row['OrderID']."</td>";
                echo "<td>".$row['CustID']."</td>";
                echo "<td>".$row['PayMode']."</td>";
                echo "<td>".$row['Amount']."</td>";
                echo "<td>".$row['Status']."</td>";
                echo "</tr>";
            }

            // Close the connection
            $conn->close();
        ?>

    </table>
</body>
</html>
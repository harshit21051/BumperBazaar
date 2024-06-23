<!DOCTYPE html>
<html>
<head>
    <title>Inventory Table</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
</head>
<body>
    <h2>Inventory</h2>
    <table>
        <tr>
            <th>ProdID</th>
            <th>ProdName</th>
            <th>Price</th>
            <th>StockQty</th>
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

            // Retrieve data from inventory table
            $sql = "SELECT * FROM inventory";
            $result = $conn->query($sql);

            // Loop through each row of data
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>".$row['ProdID']."</td>";
                echo "<td>".$row['ProdName']."</td>";
                echo "<td>".$row['Price']."</td>";
                echo "<td>".$row['StockQty']."</td>";
                echo "</tr>";
            }

            // Close the connection
            $conn->close();
        ?>

    </table>
</body>
</html>
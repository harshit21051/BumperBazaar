<!DOCTYPE html>
<html>
<head>
    <title>Customers Table</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
</head>
<body>
    <h2>Customers</h2>
    <table>
        <tr>
            <th>CustID</th>
            <th>Name</th>
            <th>Gender</th>
            <th>Category</th>
            <th>Email</th>
            <th>Phone</th>
            <th>WalletBalance</th>
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

            // Retrieve data from customers table
            $sql = "SELECT * FROM customers";
            $result = $conn->query($sql);

            // Loop through each row of data
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>".$row['CustID']."</td>";
                echo "<td>".$row['Name']."</td>";
                echo "<td>".$row['Gender']."</td>";
                echo "<td>".$row['Category']."</td>";
                echo "<td>".$row['Email']."</td>";
                echo "<td>".$row['Phone']."</td>";
                echo "<td>".$row['WalletBalance']."</td>";
                echo "</tr>";
            }

            // Close the connection
            $conn->close();
        ?>

    </table>
</body>
</html>
# BumperBazaar

Welcome to BumperBazaar, an online shopping platform built using Python and MySQL. BumperBazaar provides a command-line interface (CLI) for shopping functionality and utilizes a SQL database as its backend. Additionally, a website has been developed to display tables fetched from the database using PHP and the XAMPP web server.

## Tech Stack

BumperBazaar is built using the following technologies:

  - Python
  - MySQL
  - MySQL Python Connector library
  - HTML
  - CSS
  - PHP
  - XAMPP web server
  - Mockaroo : used to populate database with dummy data

## Prerequisites

To ensure proper functioning of the BumperBazaar website, please follow these steps:

  - Install XAMPP from their official website: https://www.apachefriends.org/download.html.
  - Configure XAMPP properly by referring to this video tutorial: https://www.youtube.com/watch?v=at19OmH2Bg4&list=PLu0W_9lII9aikXkRE0WxDt1vozo3hnmtR&index=1&t=7s.
  - Clone the BumperBazaar repository and extract the zip file in the following directory: C:\xampp\htdocs.
  - Import the schema.sql file into MySQL Workbench and execute it. Then, import the dataset.sql file. This will create the necessary database and populate it with data.
  - To run the Python program:
      - Navigate to the python_files directory and run index.py.
      - While the Python program is running, any modifications made to the database will be reflected in real-time.
  - To view the tables online:
      - First open XAMPP control panel and start Apache and MySQL.
      - Open the following link: http://localhost/BumperBazaar-main/html_files/.
      - To access the database portal (phpMyAdmin), visit: http://localhost/phpmyadmin/index.php?route=/database/structure&db=bumper_bazaar.

Enjoy using BumperBazaar for your online shopping needs! Should you have any questions or encounter any issues, please don't hesitate to contact us at harshit21051@iiitd.ac.in.

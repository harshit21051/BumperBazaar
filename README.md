# BumperBazaar

 Tech stack:
 - Python
 - MySQL
 - MySQL python connector library
 - HTML
 - CSS
 - PHP
 - XAMPP web-server

 It is a CLI based online shopping program written in python which uses SQL database as the backend.
 Also, a website is created where we can see the tables fetched from the database using PHP and XAMPP server.
 For proper functioning of the website, you need to:
   - Installl XAMPP from their site: https://www.apachefriends.org/download.html
   - Configure it properly, watch video for reference: https://www.youtube.com/watch?v=at19OmH2Bg4&list=PLu0W_9lII9aikXkRE0WxDt1vozo3hnmtR&index=1&t=7s
   - Clone this repo and store it in the following directory: C:\xampp\htdocs
   - First run the schema.sql into MySQL Workbench and then run dataset.sql. Your database is now created in your system.
   - To run python program:
        - Run index.py in python_files directory
        - While running the python program, any modification done to the database gets reflected in the website.
   - To view tables in HTML:
        - Open following link: http://localhost/BumperBazaar/html_files/
        - To open database portal (phpMyAdmin): http://localhost/phpmyadmin/index.php?route=/database/structure&db=bumper_bazaar

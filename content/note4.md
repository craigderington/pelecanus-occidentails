Title: MySQL - Create a New Database User Account
Date: 2025-07-13 23:55
Modified: 2025-07-13 23:55
Category: MySQL
Tags: linux, command line, useful commands, mysql, mysql-server, mysql-workbench
Slug: create-a-new-user-in-mysql-database
Authors: Craig Derington
Summary: Create a new MySQL User and Assign Privileges.

#### MySQL Users

##### Create a NEW User
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON database_name.* TO 'newuser'@'localhost';
```

##### Update ROOT User to login from any host

```
sudo mysql -u root
Check your accounts present in your db

SELECT User,Host FROM mysql.user;
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| admin            | localhost |
| debian-sys-maint | localhost |
| magento_user     | localhost |
| mysql.sys        | localhost |
| root             | localhost |
Delete current root@localhost account

mysql> DROP USER 'root'@'localhost';
Query OK, 0 rows affected (0,00 sec)
Recreate your user

mysql> CREATE USER 'root'@'%' IDENTIFIED BY '';
Query OK, 0 rows affected (0,00 sec)
Give permissions to your user (don't forget to flush privileges)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0,00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0,01 sec)

```

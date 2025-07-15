Title: MySQL - Event Scheduler
Date: 2025-07-13 23:30
Modified: 2025-07-13 23:30
Category: MySQL
Tags: linux, command line, useful commands, mysql, mysql-server, mysql-workbench
Slug: mysql-database-event-scheduler
Authors: Craig Derington
Summary: Create Events with the MySQL Event Scheduler

##### MYSQL EVENT SCHEDULER
MySQL Event Scheduler


View Scheduler Settings


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
select @@global.event_scheduler;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Set Event Scheduler to ON


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
set @@global.event_scheduler = 1;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Check MySQL for Event Last Run Time


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
select * from information_schema.events\G;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Event


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
delimiter |

CREATE EVENT update_customers
    ON SCHEDULE
      EVERY 1 DAY
      STARTS '2017-04-20 06:00:00' ON COMPLETION PRESERVE ENABLE
    COMMENT 'Overwrites OWL Customer Names from Temp Table'
    DO
      BEGIN
        UPDATE frontend_customer t1, temp_customers t2
           SET t1.customer_name = t2.customer_name
        WHERE t1.id = t2.id;
      END |

delimiter ;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Drop Event


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DROP EVENT [IF EXISTS] event_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Edit Event


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ALTER event _insert 
   ON SCHEDULE AT '2012-10-08 17:09' + INTERVAL 1 MINUTE -- or new date 
   DO INSERT INTO event_test VALUES(now());
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Describe Table


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mysql> describe temp_customers;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id             | int(11)     | NO   | PRI | NULL    | auto_increment |
| customer_name  | varchar(50) | YES  |     | NULL    |                |
| street_address | varchar(50) | YES  |     | NULL    |                |
| city           | varchar(50) | YES  |     | NULL    |                |
| state          | varchar(50) | YES  |     | NULL    |                |
| postal_code    | varchar(50) | YES  |     | NULL    |                |
| latitude       | varchar(50) | YES  |     | NULL    |                |
| longitude      | varchar(50) | YES  |     | NULL    |                |
| email          | varchar(50) | YES  |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

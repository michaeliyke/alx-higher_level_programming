# 0x0E. SQL - More queries

> This project was on ...
**Databases**

## Background Context

> [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)

### Creating a New User

Upon installation, MySQL creates a root user account which you can use to manage your database. This user has full privileges over the MySQL server, meaning it has complete control over every database, table, user, and so on. Because of this, it’s best to avoid using this account outside of administrative functions. This step outlines how to use the root MySQL user to create a new user account and grant it privileges.

In Ubuntu systems running MySQL 5.7 (and later versions), the root MySQL user is set to authenticate using the auth_socket plugin by default rather than with a password. This plugin requires that the name of the operating system user that invokes the MySQL client matches the name of the MySQL user specified in the command. This means that you need to precede the mysql command with sudo to invoke it with the privileges of the root Ubuntu user in order to gain access to the root MySQL user:

```sql
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
```

```sql
``GRANT`` privilege [,privilege],..
ON privilege_level
TO account_name;
```

```sql
GRANT SELECT
ON *.*
TO bob@localhost;
```

**Column privileges** apply to individual columns within a table. You must specify the column or columns for each privilege. For example:

```sql
GRANT
   SELECT (employeeNumner,lastName, firstName,email),
   UPDATE(lastName)
ON employees
TO bob@localhost;
```

```sql
GRANT EXECUTE
ON PROCEDURE CheckCredit
TO bob@localhost;
```

### EXAMPLES

```sql
CREATE USER super@localhost
IDENTIFIED BY 'Secure1Pass!';
```

```sql
SHOW GRANTS FOR super@localhost;
```

```sql
GRANT ALL
ON classicmodels.*
TO super@localhost;
```

```sql
SHOW GRANTS FOR super@localhost;
```

```sql
CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
```

```sql
ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

```sql
GRANT PRIVILEGE ON database.table TO 'username'@'host';
```

The PRIVILEGE value in this example syntax defines what actions the user is allowed to perform on the specified database and table. You can grant multiple privileges to the same user in one command by separating each with a comma. You can also grant a user privileges globally by entering asterisks (*) in place of the database and table names. In SQL, asterisks are special characters used to represent “all” databases or tables.

To illustrate, the following command grants a user global privileges to CREATE, ALTER, and DROP databases, tables, and users, as well as the power to INSERT, UPDATE, and DELETE data from any table on the server. It also grants the user the ability to query data with SELECT, create foreign keys with the REFERENCES keyword, and perform FLUSH operations with the RELOAD privilege. However, you should only grant users the permissions they need, so feel free to adjust your own user’s privileges as necessary.

```sql
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

Warning: Some users may want to grant their MySQL user the ALL PRIVILEGES privilege, which will provide them with broad superuser privileges akin to the root user’s privileges, like so:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

Such broad privileges should not be granted lightly, as anyone with access to this MySQL user will have complete control over every database on the server.

Many guides suggest running the FLUSH PRIVILEGES command immediately after a CREATE USER or GRANT statement in order to reload the grant tables to ensure that the new privileges are put into effect:

```sql
FLUSH PRIVILEGES;
```

```sql
REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';
```

You can review a user’s current permissions by running the SHOW GRANTS command:

```sql
SHOW GRANTS FOR 'username'@'host';
```

```sql
DROP USER 'username'@'localhost';
```



#### I learnt about

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a ``PRIMARY KEY``
- What’s a ``FOREIGN KEY``
- How to use ``NOT NULL`` and ``UNIQUE`` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are ``JOIN`` and ``UNION``

## Requirements

### General

- Allowed editors: ``vi``, ``vim``, ``emacs``
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT, WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### More Info

#### Comments for your SQL file

```\
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

#### Install MySQL 8.0 on Ubuntu 20.04 LTS

```\
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:

```\
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

#### Use “container-on-demand” to run MySQL

**In the container, credentials are `root/root`**

- Ask for container `Ubuntu 20.04`
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

```\
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database

information_schema
mysql
performance_schema
sys
$
```

**In the container, credentials are `root/root`**

#### How to import a SQL dump

```\
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

![Different forms SQL join](./sql.png)

### Environment

- Language: SQL
- OS: Ubuntu 20.04 LTS
- Interpreter: MySQL 8.0

### Files

> Each file contains the solution to a task in the project.

- 0-list_databases.sql
- 1-create_database_if_missing.sql
- 2-remove_database.sql
- 3-list_tables.sql
- 4-first_table.sql
- 5-full_table.sql
- 6-list_values.sql
- 7-insert_value.sql
- 8-count_89.sql
- 9-full_creation.sql
- 10-top_score.sql
- 11-best_score.sql
- 12-no_cheating.sql
- 13-change_class.sql
- 14-average.sql
- 15-groups.sql
- 16-no_link.sql

#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

#### Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

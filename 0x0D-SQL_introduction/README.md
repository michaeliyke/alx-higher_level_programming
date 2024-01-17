# 0x0D. SQL - Introduction

> This project was on ...
**Databases**

## Background Context

> What are databases?
First, what are databases for?

Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

Then, why not store your data in flat files, as you did in the “Relational databases, done wrong” project? A solid database is expected to be acid, which means it guarantees:

- **A**tomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.

- **C**onsistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.

- **I**solation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.

- **D**urability: unplug your server at any time, boot it back up, and it didn’t lose any data.

Also, a solid database will provide strong performance (because I/O is your bottleneck and databases are I/O, so their performance makes a whole lot more of a difference than the performance of your application’s code) and scalability (inserting one user in a collection of 5 users should take about the same time as inserting one user in a collection of 5 billion users).

### **ACID** is a cool acronym! **CRUD** is another cool one

You will definitely run into the concept of “CRUD” operations. It’s just a fancy way to refer to the 4 operations that can be performed on the data itself:

- **C**reate some data;
- **R**ead some data;
- **U**pdate some data;
- **D**estroy some data.

#### I learnt about

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are subqueries
- How to use MySQL functions

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

``` \
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

# 0x0E. SQL - More queries

```sql
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
```

```sql
GRANT privilege [,privilege],..
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

```sql
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

Warning: Some users may want to grant their MySQL user the ALL PRIVILEGES privilege, which will provide them with broad superuser privileges akin to the root user’s privileges, like so:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

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

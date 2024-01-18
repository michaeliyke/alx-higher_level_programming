
# 0x0E. SQL - More queries

&nbsp; <!-- blank line -->

## SQL technique: subqueries

SQL technique: subqueries
Sometimes you don’t have enough information available when you design a query to determine which rows you want. In this case, you’ll have to find the required information with a subquery.

```sql
  SELECT cFirstName, cLastName
        FROM customers
        WHERE cZipCode = ???
```

```sql
        SELECT cZipCode
        FROM Customers
        WHERE cFirstName = 'Wayne' AND cLastName = 'Dick';
```

```sql
 SELECT cFirstName, cLastName, cZipCode
        FROM customers
        WHERE cZipCode =
          (SELECT cZipCode
           FROM customers
           WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');
```

A subquery that returns only one column and one row can be used any time that we need a single value.

Another example would be to find the product name and sale price of all products whose unit sale price is greater than the average of all products

We can see that the DISTINCT keyword is needed, since the SELECT attributes are not a super key of the result set:

```sql
 SELECT DISTINCT prodName, unitSalePrice
        FROM Products NATURAL JOIN OrderLines
        WHERE unitSalePrice > the average unit sale price
```

Again, we already know how to write another query that finds the average:

```sql
        SELECT AVG(unitSalePrice)
        FROM OrderLines;
```

```sql
 SELECT DISTINCT prodName, unitSalePrice
        FROM Products NATURAL JOIN OrderLines
        WHERE unitSalePrice >
          (SELECT AVG(unitSalePrice)
           FROM OrderLines);
```

<!-- markdownlint-disable-next-line -->
#### References

[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

#### Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

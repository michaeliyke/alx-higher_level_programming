
# 0x0E. SQL - More queries

&nbsp; <!-- blank line -->

## SQL technique: join types

&nbsp;

### Inner join

All of the joins that you have seen so far have used the `natural join` syntax—for example, to produce a list of customers and dates on which they placed orders. Remember that if this syntax is available, it will automatically pick the join attributes as those with the same name in both tables (intersection of the schemes). It will also produce only one copy of those attributes in the result table.

```sql
SELECT cFirstName, cLastName, orderDate
        FROM customers NATURAL JOIN orders;
```

- The join does not consider the pk and fk attributes you have specified. If there are any non-pk/fk attributes that have the same names in the tables to be joined, they will also be included in the intersection of the schemes, and used as join attributes in the natural join. The results will certainly not be correct! This problem might be especially difficult to detect in cases where many natural joins are performed in the same query. Fortunately, you can always specify the join attributes yourself, as we describe next.

- Another keyword that produces the same results (without the potential attribute name problem) is the `inner join`. With this syntax, you may specify the join attributes in a `USING` clause. (Multiple join attributes in the `USING` clause are separated by commas.) This also produces only one copy of the join attributes in the result table. Like the `NATURAL JOIN` syntax, the `USING` clause is not supported by all systems.

```sql
  SELECT cFirstName, cLastName, orderDate
        FROM customers INNER JOIN orders
          USING (custID);
```

- The most widely-used (and most portable) syntax for the inner join substitutes an ON clause for the USING clause. This requires you to explicitly specify not only the join attribute names, but the join condition (normally equality). It also requires you to preface (qualify) the join attribute names with their table name, since both columns will be included in the result table. This is the only syntax that will let you use join attributes that have different names in the tables to be joined. Unfortunately, it also allows you to join tables on attributes other than the pk/fk pairs, which was a pre-1992 way to answer queries that can be written in better ways today.

```sql
  SELECT cFirstName, cLastName, orderDate
        FROM customers INNER JOIN orders
          ON customers.custID = orders.custID;
```

- You can save a bit of typing by specifying an alias for each table name (such as c and o in this example), then using the alias instead of the full name when you refer to the attributes. This is the only syntax that will let you join a table to itself, as we will see when we discuss recursive relationships.

```sql
 SELECT cFirstName, cLastName, orderDate
        FROM customers c INNER JOIN orders o
          ON c.custID = o.custID;
```

### Outer join

One important effect of all natural and inner joins is that any unmatched PK value simply drops out of the result. In our example, this means that any customer who didn’t place an order isn’t shown. Suppose that we want a list of all customers, along with order date(s) for those who did place orders. To include the customers who did not place orders, we will use an outer join, which may take either the USING or the ON clause syntax.

```sql
SELECT cFirstName, cLastName, orderDate
        FROM customers c LEFT OUTER JOIN orders o
          ON c.custID = o.custID
```

- Notice that for customers who placed no orders, any attributes from the Orders table are simply filled with NULL values.

- The word “left” refers to the order of the tables in the FROM clause (customers on the left, orders on the right). The left table here is the one that might have unmatched join attributes—the one from which we want all rows. We could have gotten exactly the same results if the table names and outer join direction were reversed:

```sql
  SELECT cFirstName, cLastName, orderDate
        FROM orders o RIGHT OUTER JOIN customers c
          ON o.custID = c.custID;
```

- An outer join makes sense only if one side of the relationship has a minimum cardinality of zero (as Orders does in this example). Otherwise, the outer join will produce exactly the same result as an inner join (for example, between Orders and OrderLines).

- The SQL standard also allows a FULL outer join, in which unmatched join attributes from either side are paired with null values on the other side. You will probably not have to use this with most well-designed databases.

### Evaluation order

Multiple joins in a query are evaluated left-to-right in the order that you write them, unless you use parentheses to force a different evaluation order. (Some database systems require parentheses in any case.) The schemes of the joins are also cumulative in the order that they are evaluated; in RA, this means that

r1 ⨝ r2 ⨝ r3 = (r1 ⨝ r2) ⨝ r3.

- It is especially important to remember this rule when outer joins are mixed with other joins in a query. For example, if you write:

```sql
SELECT cFirstName, cLastName, orderDate, UPC, quantity
        FROM customers LEFT OUTER JOIN orders
          USING (custID)
          NATURAL JOIN orderlines;
```

you will lose the customers who haven’t placed orders. They will be retained if you force the second join to be executed first:

```sql
SELECT cFirstName, cLastName, orderDate, UPC, quantity
        FROM customers LEFT OUTER JOIN
          (orders NATURAL JOIN orderlines)
          USING (custID);
```

### Other join types

For sake of completeness, you should also know that if you try to join two tables with no join condition, the result will be that every row from one side is paired with every row from the other side. Mathematically, this is a Cartesian product of the two tables, as you have seen before. It is almost never what you want. In pre-1992 syntax, it is easy to do this accidently, by forgetting to put the join condition in the WHERE clause:

```sql
SELECT cFirstName, cLastName, orderDate
        FROM customers, orders;
```

- If your system is backward-compatible (most are), you might actually try this just to prove to yourself that the result is pure nonsense. However, if you ever have an occasion to really need a Cartesian product of two tables, use the new `cross join` syntax to prove that you really mean it. Notice that this example still produces nonsense.

```sql
SELECT cFirstName, cLastName, orderDate
        FROM customers CROSS JOIN orders;
```

- It is possible, but confusing, to specify a join condition other than equality of two attributes; this is called a `non-equi-join`. If you see such a thing in older code, it probably represents a WHERE clause or subquery in disguise.

- You may also hear the term `self join`, which is nothing but an inner or outer join between two attributes in the same table. We’ll look at these when we discuss recursive relationships.

<!-- markdownlint-disable-next-line -->
#### References

[SQL technique: unions and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

#### Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

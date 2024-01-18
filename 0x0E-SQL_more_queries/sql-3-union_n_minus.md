
# 0x0E. SQL - More queries

&nbsp; <!-- blank line -->

## SQL technique: union and minus

Some students initially think of the join as being a sort of union between two tables. It’s not (except for the schemes). The join pairs up data from two very different tables. In RA and SQL, union can operate only on two identical tables. Remember the Venn-diagram representation of the union and minus operations on sets. Union includes members of either or both sets (with no duplicates). Minus includes only those members of the set on the left side of the expression that are not contained in the set on the right side of the expression

### Union

For this example, we will add a Suppliers table to our sales data entry model. “A supplier is a company from which we purchase products that we will re-sell.” Each supplier suppliers zero to many products; each product is supplied by one and only one supplier. The supplier class attributes include the company name and address, plus the name and phone number of the representative from whom we make our purchases

We can create an extra column in the query output for the Customers table by simply giving it a name and filling it with a constant value. Here, we’ll use the value 'Customer' to distinguish these rows from supplier representatives. SQL uses the column names of the first part of the union query as the column names for the output, so we will give each of them aliases that are appropriate for the entire set of data.

Build and test each component of the union query individually, then put them together. The ORDER BY clause has to come at the end.

```sql
SELECT cLastName AS "Last Name", cFirstName AS "First Name",
          cPhone as "Phone", 'Customer' AS "Company"
        FROM customers
        UNION
        SELECT repLName, repFName, repPhone, sCompanyName
        FROM suppliers
        ORDER BY "Last Name";
```

### Minus

Sometimes you have to think about both what you do want and what you don’t want in the results of a query. If there is a WHERE clause predicate that completely partitions all rows of interest (the result set) into those you want and those you don’t want, then you have a simple query with a test for inequality.

The multiplicity of an association can help you determine how to build the query. Since each product has one and only one supplier, we can partition the Products table into those that are supplied by a given company and those that are not.

```sql
   SELECT prodName, sCompanyName
        FROM Products NATURAL JOIN Suppliers
        WHERE sCompanyName <> 'Industrial Tool Supply';
```

Contrast this to finding customers who did not make purchases in 2002. Because of the optional one-to-many association between Customers and Orders, there are actually four possibilities:

1. A customer made purchases in 2002 (only).
2. A customer made purchases in other years, but not in 2002.
3. A customer made purchases both in other years and in 2002.
4. A customer made no purchases in any year.

If you try to write this as a simple test for inequality,

```sql
 SELECT DISTINCT cLastName, cFirstName, cStreet, cZipCode
        FROM Customers NATURAL JOIN Orders
        WHERE TO_CHAR(orderDate, 'YYYY') <> '2002';
```

you will correctly exclude group 1 and include group 2, but falsely include group 3 and falsely exclude group 4. Please take time to re-read this statement and convince yourself why it is true!

<!-- markdownlint-disable-next-line -->
#### what we need to do:

{customers who did not make purchases in 2002} = {all customers} − {those who did}

The easiest syntax in this case is to compare only the customer IDs. We’ll use the NOT IN set operator in the WHERE clause, along with a subquery to find the customer ID of those who did made purchases in 2002.

```sql
SELECT cLastName, cFirstName, cStreet, cZipCode
        FROM Customers
        WHERE custID NOT IN
          (SELECT custID
          FROM Orders
          WHERE TO_CHAR(orderDate, 'YYYY') = '2002');
```

We can also use the MINUS operator to subtract rows we don’t want from all rows in Customers. (Some versions of SQL use the keyword `EXCEPT` instead of `MINUS`.) Like the `UNION`, this requires the schemes of the two tables to match exactly in number and type of attributes.

```sql
SELECT cLastName, cFirstName, cStreet, cZipCode
        FROM Customers
        MINUS
        SELECT cLastName, cFirstName, cStreet, cZipCode
        FROM Customers NATURAL JOIN Orders
        WHERE TO_CHAR(orderDate, 'YYYY') = '2002';
```

#### Other set operations

SQL has two additional set operators. UNION ALL works like UNION, except it keeps duplicate rows in the result. INTERSECT operates just like you would expect from set theory; again, the schemes of the two tables must match exactly.

<!-- markdownlint-disable-next-line -->
#### References

[SQL technique: unions and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

#### Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

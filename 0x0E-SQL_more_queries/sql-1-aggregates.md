
# 0x0E. SQL - More queries

&nbsp; <!-- blank line -->

## Aggregates

Aggregate functions in SQL are used to perform calculations on sets of values and return a single result. They're crucial for summarizing and analyzing data within a database. Here are explanations of AVG, COUNT, and SUM, along with examples:

### AVG

Calculates the average of a numeric column. Goes from top to bottom between all the rows.
Below query returns the average price of all products in the products table.

```sql
SELECT AVG(price) AS average_price FROM products;
```

### COUNT

Counts the number of rows in a table or the number of non-null values in a specific column.
Just like `AVG` `COUNT` goes top to bottom between the rows counting each record occurence.

```sql
SELECT COUNT(*) AS total_products FROM products;  -- Counts all rows
SELECT COUNT(price) AS products_with_price FROM products;  -- Counts rows with non-null price
```

The first query counts the total number of products, while the second counts only those with a non-null price.

### SUM

Calculates the sum of values in a numeric column. And Just like the others, `SUM` goes top to bottom
between the rows summing in each record the named column's values.

```sql
SELECT SUM(sales) AS total_sales FROM orders;
```

<!-- markdownlint-disable-next-line -->
### Other common aggregate functions:

- **`MIN`**: Finds the minimum value in a column.
- **`MAX`**: Finds the maximum value in a column.
- **`VAR`**: Calculates the variance of a column.
- **`STDDEV`**: Calculates the standard deviation of a column.

<!-- markdownlint-disable-next-line -->
### Key facts:

- Aggregate functions typically ignore null values.
- They can be used with the GROUP BY clause to perform calculations on groups of data.
- You can apply multiple aggregate functions in a single query.
- Different SQL database platforms may have additional aggregate functions available

#### References

[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

#### Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

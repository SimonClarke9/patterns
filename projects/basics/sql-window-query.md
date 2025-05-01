# 1 ROW_NUMBER()
<details>
<summary> What it does: Assigns a sequential integer to each row within the partition.</summary>

How to apply:
ROW_NUMBER() OVER (PARTITION BY category ORDER BY price)
Use Case: Assigning sequence numbers to sales transactions within each store.
</details>

# 2 RANK()
What it does: Assigns ranks with gaps in case of ties.
How to apply:
RANK() OVER (PARTITION BY category ORDER BY price)
Use Case: Ranking employees or products in a region based on sales.

# 3 DENSE_RANK()
What it does: Same as RANK(), but no gaps in ranking.
How to apply:
DENSE_RANK() OVER (PARTITION BY category ORDER BY price)
Use Case: Ranking products by price without skipping tied values.

# 4 NTILE(n)
What it does: Distributes rows into n buckets.
How to apply:
NTILE(4) OVER (PARTITION BY category ORDER BY price)
Use Case: Splitting customers into quartiles for marketing segmentation.

# 5 PERCENT_RANK()
What it does: Computes the rank as a percentage of total rows.
How to apply:
PERCENT_RANK() OVER (PARTITION BY category ORDER BY price)
Use Case: Analyzing how a product ranks in pricing within a category.

# 6 FIRST_VALUE()
What it does: Returns the first value in the ordered set.
How to apply:
FIRST_VALUE(price) OVER (PARTITION BY category ORDER BY price)
Use Case: Finding the lowest price per product category.

# 7 LAST_VALUE()
What it does: Returns the last value in the ordered set.
How to apply:
LAST_VALUE(price) OVER (PARTITION BY category ORDER BY price)
Use Case: Identifying the latest value for audit or time-based checks.

# 8 LAG()
What it does: Accesses value from previous row (offset optional).
How to apply:
LAG(price, 1, 0) OVER (PARTITION BY category ORDER BY price)
Use Case: Comparing day-over-day prices for trend analysis.

# 9 LEAD()
What it does: Accesses value from next row (offset optional).
How to apply:
LEAD(price, 1, 0) OVER (PARTITION BY category ORDER BY price)
Use Case: Forecasting future values based on current row.

# 10 SUM()
What it does: Calculates the sum over a window.
How to apply:
SUM(price) OVER (PARTITION BY category ORDER BY price)
Use Case: Calculating rolling sales totals by category.

# 11 AVG()
What it does: Calculates the average over a window.
How to apply:
AVG(price) OVER (PARTITION BY category ORDER BY price)
Use Case: 7-day rolling average for smoother trends.

# 12  COUNT()
What it does: Counts non-null rows in a partition.
How to apply:
COUNT() OVER (PARTITION BY category)
Use Case: Count of orders per user in a dataset.
Check the 1st comment for the last 3 ↓

# 13 MIN()
What it does: Returns the minimum value in the window.
How to apply:
MIN(price) OVER (PARTITION BY category)
Use Case: Finding the cheapest product per group.
How to apply:
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
Use Case: 7-day moving sums or averages.
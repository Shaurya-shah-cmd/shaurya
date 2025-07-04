CREATE SCHEMA dannys_diner;
SET search_path = dannys_diner;
CREATE TABLE sales (
  "customer_id" VARCHAR(1),
  "order_date" DATE,
  "product_id" INTEGER
);

INSERT INTO sales ("customer_id", "order_date", "product_id") VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
CREATE TABLE menu (
  "product_id" INTEGER,
  "product_name" VARCHAR(5),
  "price" INTEGER
);

INSERT INTO menu ("product_id", "product_name", "price") VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
CREATE TABLE members (
  "customer_id" VARCHAR(1),
  "join_date" DATE
);

INSERT INTO members ("customer_id", "join_date") VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
SELECT
  s.customer_id,
  SUM(m.price) AS total_spent
FROM
  sales s
  JOIN menu m ON s.product_id = m.product_id
GROUP BY
  s.customer_id;
SELECT
  customer_id,
  COUNT(DISTINCT order_date) AS visit_days
FROM
  sales
GROUP BY
  customer_id;
SELECT
  first_purchases.customer_id,
  first_purchases.order_date,
  m.product_name
FROM (
  SELECT
    s.customer_id,
    s.order_date,
    s.product_id,
    ROW_NUMBER() OVER (PARTITION BY s.customer_id ORDER BY s.order_date, s.product_id) AS rn
  FROM
    sales s
) first_purchases
JOIN menu m ON first_purchases.product_id = m.product_id
WHERE
  first_purchases.rn = 1;
SELECT
  m.product_name,
  COUNT(*) AS total_orders
FROM
  sales s
  JOIN menu m ON s.product_id = m.product_id
GROUP BY
  m.product_name
ORDER BY
  total_orders DESC
LIMIT 1;
WITH item_counts AS (
  SELECT
    s.customer_id,
    s.product_id,
    COUNT(*) AS order_count
  FROM
    sales s
  GROUP BY
    s.customer_id, s.product_id
),
ranked_items AS (
  SELECT
    ic.customer_id,
    ic.product_id,
    ic.order_count,
    RANK() OVER (PARTITION BY ic.customer_id ORDER BY ic.order_count DESC) AS rnk
  FROM
    item_counts ic
)
SELECT
  r.customer_id,
  m.product_name,
  r.order_count
FROM
  ranked_items r
  JOIN menu m ON r.product_id = m.product_id
WHERE
  r.rnk = 1;
WITH after_join AS (
  SELECT
    s.customer_id,
    s.order_date,
    s.product_id,
    m.join_date,
    ROW_NUMBER() OVER (
      PARTITION BY s.customer_id
      ORDER BY s.order_date, s.product_id
    ) AS rn
  FROM
    sales s
    JOIN members m ON s.customer_id = m.customer_id
  WHERE
    s.order_date >= m.join_date
)
SELECT
  a.customer_id,
  a.order_date,
  menu.product_name
FROM
  after_join a
  JOIN menu ON a.product_id = menu.product_id
WHERE
  a.rn = 1;
WITH before_join AS (
  SELECT
    s.customer_id,
    s.order_date,
    s.product_id,
    m.join_date,
    ROW_NUMBER() OVER (
      PARTITION BY s.customer_id
      ORDER BY s.order_date DESC, s.product_id DESC
    ) AS rn
  FROM
    sales s
    JOIN members m ON s.customer_id = m.customer_id
  WHERE
    s.order_date < m.join_date
)
SELECT
  b.customer_id,
  b.order_date,
  menu.product_name
FROM
  before_join b
  JOIN menu ON b.product_id = menu.product_id
WHERE
  b.rn = 1;
SELECT
  s.customer_id,
  COUNT(*) AS total_items,
  SUM(mn.price) AS total_spent
FROM
  sales s
  JOIN members mb ON s.customer_id = mb.customer_id
  JOIN menu mn ON s.product_id = mn.product_id
WHERE
  s.order_date < mb.join_date
GROUP BY
  s.customer_id;
SELECT
  s.customer_id,
  SUM(
    CASE
      WHEN m.product_name = 'sushi' THEN m.price * 10 * 2
      ELSE m.price * 10
    END
  ) AS total_points
FROM
  sales s
  JOIN menu m ON s.product_id = m.product_id
GROUP BY
  s.customer_id;

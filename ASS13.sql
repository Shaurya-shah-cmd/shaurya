CREATE TABLE clique_bait.event_identifier (
  "event_type" INTEGER,
  "event_name" VARCHAR(13)
);

CREATE TABLE clique_bait.campaign_identifier (
  "campaign_id" INTEGER,
  "products" VARCHAR(3),
  "campaign_name" VARCHAR(33),
  "start_date" TIMESTAMP,
  "end_date" TIMESTAMP
);

CREATE TABLE clique_bait.page_hierarchy (
  "page_id" INTEGER,
  "page_name" VARCHAR(14),
  "product_category" VARCHAR(9),
  "product_id" INTEGER
);

CREATE TABLE clique_bait.users (
  "user_id" INTEGER,
  "cookie_id" VARCHAR(6),
  "start_date" TIMESTAMP
);

CREATE TABLE clique_bait.events (
  "visit_id" VARCHAR(6),
  "cookie_id" VARCHAR(6),
  "page_id" INTEGER,
  "event_type" INTEGER,
  "sequence_number" INTEGER,
  "event_time" TIMESTAMP
);
SELECT COUNT(*) AS total_users
FROM clique_bait.users;
SELECT COUNT(DISTINCT cookie_id)::DECIMAL / COUNT(DISTINCT user_id) AS avg_cookies_per_user
FROM clique_bait.users;
SELECT 
  DATE_TRUNC('month', event_time) AS month,
  COUNT(DISTINCT visit_id) AS unique_visits
FROM clique_bait.events
GROUP BY 1
ORDER BY 1;

SELECT 
  ei.event_name,
  COUNT(*) AS WITH visit_events AS (
  SELECT 
    visit_id,
    MAX(CASE WHEN page_id = 12 THEN 1 ELSE 0 END) AS viewed_checkout,
    MAX(CASE WHEN event_type = 3 THEN 1 ELSE 0 END) AS made_purchase
  FROM clique_bait.events
  GROUP BY visit_id
)
SELECT 
  ROUND(
    100.0 * COUNT(*) FILTER (WHERE viewed_checkout = 1 AND made_purchase = 0)
    / NULLIF(COUNT(*), 0), 2
  ) AS pct_checkout_no_purchase
FROM visit_events;
SELECT 
  ph.page_name,
  COUNT(*) AS view_count
FROM clique_bait.events e
JOIN clique_bait.page_hierarchy ph
  ON e.page_id = ph.page_id
WHERE e.event_type = 1 -- Page View
GROUP BY ph.page_name
ORDER BY view_count DESC
LIMIT 3;
FROM clique_bait.events e
JOIN clique_bait.event_identifier ei
  ON e.event_type = ei.event_type
GROUP BY ei.event_name
ORDER BY event_count DESC;
SELECT 
  ROUND(
    100.0 * COUNT(DISTINCT CASE WHEN e.event_type = 3 THEN visit_id END)
    / COUNT(DISTINCT visit_id), 2
  ) AS pct_visits_with_purchase
FROM clique_bait.events e;
SELECT 
  ph.page_name,
  COUNT(*) AS view_count
FROM clique_bait.events e
JOIN clique_bait.page_hierarchy ph
  ON e.page_id = ph.page_id
WHERE e.event_type = 1 -- Page View
GROUP BY ph.page_name
ORDER BY view_count DESC
LIMIT 3;
SELECT 
  ph.product_category,
  COUNT(*) FILTER (WHERE e.event_type = 1) AS view_count,
  COUNT(*) FILTER (WHERE e.event_type = 2) AS cart_add_count
FROM clique_bait.events e
JOIN clique_bait.page_hierarchy ph
  ON e.page_id = ph.page_id
WHERE ph.product_category IS NOT NULL
GROUP BY ph.product_category
ORDER BY product_category;
SELECT 
  ph.page_name AS product_name,
  COUNT(*) AS purchase_count
FROM clique_bait.events e
JOIN clique_bait.page_hierarchy ph
  ON e.page_id = ph.page_id
WHERE e.event_type = 3 -- Purchase
GROUP BY ph.page_name
ORDER BY purchase_count DESC
LIMIT 3;


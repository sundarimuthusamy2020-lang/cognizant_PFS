--Display Products with Stock Less Than 20
SELECT product_id,
       product_name,
       stock
FROM product
WHERE stock <= 20;
--Display Products Ordered by Price (Highest to Lowest)
SELECT product_id,
       product_name,
       price
FROM product
ORDER BY price DESC;
--Display Customer Orders (Using JOIN)
SELECT
    t.transaction_id,
    m.full_name,
    p.product_name,
    t.quantity,
    t.transaction_date,
    t.approved_status
FROM transactions t
JOIN member m
ON t.member_id = m.member_id
JOIN product p
ON t.product_id = p.product_id;
--Calculate Total Sales of Each Product
SELECT
    p.product_name,
    SUM(t.quantity) AS total_quantity_sold
FROM product p
JOIN transactions t
ON p.product_id = t.product_id
GROUP BY p.product_name;
--Count Number of Orders by Each Customer
SELECT
    m.member_id,
    m.full_name,
    COUNT(t.transaction_id) AS total_orders
FROM member m
LEFT JOIN transactions t
ON m.member_id = t.member_id
GROUP BY
    m.member_id,
    m.full_name;
--Calculate Total Revenue of Each Product
SELECT
    p.product_name,
    SUM(p.price * t.quantity) AS total_revenue
FROM product p
JOIN transactions t
ON p.product_id = t.product_id
GROUP BY p.product_name;
--Find Top-Selling Product
SELECT
    p.product_name,
    SUM(t.quantity) AS quantity_sold
FROM product p
JOIN transactions t
ON p.product_id = t.product_id
GROUP BY p.product_name
ORDER BY quantity_sold DESC
LIMIT 1;
--Calculate Average Product Rating
SELECT
    p.product_name,
    ROUND(AVG(r.value), 2) AS average_rating
FROM product p
JOIN rating r
ON p.product_id = r.product_id
GROUP BY p.product_name;
--Display Products in Customer Cart
SELECT
    c.cart_id,
    m.full_name,
    p.product_name,
    c.quantity
FROM cart c
JOIN member m
ON c.member_id = m.member_id
JOIN product p
ON c.product_id = p.product_id;

--Find Products That Have Never Been Purchased
SELECT
    p.product_name
FROM product p
LEFT JOIN transactions t
ON p.product_id = t.product_id
WHERE t.transaction_id IS NULL;

INSERT INTO product
(product_name, product_type, price, stock, description,
 created_by, creation_date, last_updated_by, last_updated_date, last_updated_login)
VALUES
('Laptop', 'Electronics', 55000.00, 20, 'Dell Inspiron 15 Laptop',
 1, CURRENT_DATE, 1, CURRENT_DATE, 101),

('Smartphone', 'Electronics', 25000.00, 50, 'Samsung Galaxy Smartphone',
 1, CURRENT_DATE, 1, CURRENT_DATE, 102),

('Headphones', 'Accessories', 3000.00, 100, 'Wireless Bluetooth Headphones',
 1, CURRENT_DATE, 1, CURRENT_DATE, 103);


INSERT INTO member
(user_name, password, full_name, phone, email_id, gender,
 created_by, creation_date, last_updated_by, last_updated_date, last_updated_login)
VALUES
('arun01', 'pass123', 'Arun Kumar', '9876543210',
 'arun@gmail.com', 'Male',
 1, CURRENT_DATE, 1, CURRENT_DATE, 101),

('priya02', 'pass456', 'Priya Sharma', '9876543211',
 'priya@gmail.com', 'Female',
 1, CURRENT_DATE, 1, CURRENT_DATE, 102),

('rahul03', 'pass789', 'Rahul Singh', '9876543212',
 'rahul@gmail.com', 'Male',
 1, CURRENT_DATE, 1, CURRENT_DATE, 103);


INSERT INTO transactions
(product_id, member_id, quantity, transaction_date,
 approved_status, created_by, creation_date,
 last_updated_by, last_updated_date, last_updated_login)
VALUES
(1, 1, 1, CURRENT_DATE, 'Approved',
 1, CURRENT_DATE, 1, CURRENT_DATE, 101),

(1, 2, 2, CURRENT_DATE, 'Pending',
 2, CURRENT_DATE, 2, CURRENT_DATE, 102),

(1, 3, 1, CURRENT_DATE, 'Approved',
 3, CURRENT_DATE, 3, CURRENT_DATE, 103);

INSERT INTO cart
(product_id, member_id, quantity,
 created_by, creation_date,
 last_updated_by, last_updated_date, last_updated_login)
VALUES
(1, 2, 1,
 1, CURRENT_DATE, 1, CURRENT_DATE, 101),

(2, 3, 2,
 2, CURRENT_DATE, 2, CURRENT_DATE, 102),

(3, 1, 1,
 3, CURRENT_DATE, 3, CURRENT_DATE, 103);


INSERT INTO rating
(product_id, member_id, value,
 created_by, creation_date,
 last_updated_by, last_updated_date, last_updated_login)
VALUES
(1, 1, 5,
 1, CURRENT_DATE, 1, CURRENT_DATE, 101),

(2, 2, 4,
 2, CURRENT_DATE, 2, CURRENT_DATE, 102),

(3, 3, 5,
 3, CURRENT_DATE, 3, CURRENT_DATE, 103);
SELECT product_id, product_name FROM product;

SELECT * FROM product;
SELECT * FROM member;
SELECT * FROM transactions;
SELECT * FROM cart;
SELECT * FROM rating;

-- Необходимо спроектировать таблицы: 
-- ●  users 
-- ●  products 
-- ●  orders 
-- ●  order_items 
-- и реализовать: 
-- ●  первичные и внешние ключи; 
-- ●  UNIQUE; 
-- ●  добавление данных;
-- ●  получение данных;
-- ●  фильтрацию; 
-- ●  сортировку; 
-- ●  изменение;
-- ●  удаление;
-- ●  JOIN; 
-- ●  агрегатные функции; 
-- ●  GROUP BY; 
-- ●  индексы для часто используемых запросов. 
-- Все запросы должны находится в .sql файлах.

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

INSERT INTO users (id,name,email)
VALUES
(1, 'Nastya', 'nas21@gmail.com'),
(2, 'Nikita', 'nfew@mail.ru'),
(3, 'Nadya', 'jogh4e@yandex.ru'),
(4, 'Nikita', 'j1r4e@yandex.ru'),
(5, 'Masha', 'jor4e@yandex.ru');

SELECT * FROM users
WHERE name='Nikita'
ORDER BY id DESC;

DELETE FROM users   
WHERE name='Nikita' AND id=4

UPDATE users
SET name='Natasha',
    email='43gwe@mail.ru'
WHERE id=2;

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    price INTEGER
);

INSERT INTO products (id,product_name,price)
VALUES
(1, 'cola', 5),
(2, 'chips', 6),
(3, 'bread', 2);

SELECT product_name AS 'Товар',
       MAX(price) AS 'Максимальная цена'
FROM products

CREATE TABLE orders (
    id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    
    PRIMARY KEY (id, user_id)

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);

INSERT INTO orders (id,user_id)
VALUES
    (1,1),
    (2,3),
    (3,3),
    (4,3);

CREATE TABLE orders_items (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES users(id)
    
    FOREIGN KEY (product_id)
        REFERENCES products(id)
);

INSERT INTO orders_items (order_id,product_id)
VALUES
(1, 1),
(1, 2),
(1, 2),
(2, 3),
(2, 2),
(3, 2),
(3, 1),
(4, 2),
(4, 1),
(4, 3);

CREATE INDEX user_name
ON users(name);

SELECT order_id as 'Номер заказа',
       COUNT(*) as 'Кол-во продуктов'
FROM orders_items
GROUP BY order_id
HAVING COUNT(*) >= 3

SELECT users.name AS 'Имя',
       COUNT(*) AS 'Кол-во заказов'
FROM users RIGHT JOIN orders ON users.id == orders.user_id
GROUP BY users.name

SELECT orders.id AS 'Номер заказа',
       products.product_name AS 'Название товара'
FROM products
JOIN orders_items
ON products.id == orders_items.product_id
JOIN orders
ON orders_items.order_id == orders.id

-- DROP TABLE 
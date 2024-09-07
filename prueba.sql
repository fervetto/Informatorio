CREATE DATABASE IF NOT EXISTS Tienda;
USE Tienda;


CREATE TABLE IF NOT EXISTS Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    ciudad VARCHAR(100),
    telefono VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS Productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);


CREATE TABLE IF NOT EXISTS Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
);


INSERT INTO Clientes (nombre, email, ciudad, telefono) VALUES
('Juan Pérez', 'juan.perez@example.com', 'Buenos Aires', '1111-1111'),
('María Gómez', 'maria.gomez@example.com', 'Córdoba', '2222-2222'),
('Carlos Ruiz', 'carlos.ruiz@example.com', 'Rosario', '3333-3333'),
('Ana López', 'ana.lopez@example.com', 'Mendoza', '4444-4444'),
('Luis Fernández', 'luis.fernandez@example.com', 'La Plata', '5555-5555');


INSERT INTO Productos (nombre, precio, stock) VALUES
('Notebook', 75000.00, 10),
('Smartphone', 45000.00, 20),
('Tablet', 30000.00, 15),
('Auriculares', 5000.00, 50),
('Monitor', 20000.00, 8);


INSERT INTO Pedidos (cliente_id, producto_id, cantidad, fecha) VALUES
(1, 1, 1, '2024-08-01'),
(2, 2, 2, '2024-08-02'),
(3, 3, 1, '2024-08-03'),
(1, 4, 3, '2024-08-04'),
(4, 5, 1, '2024-08-05'),
(2, 1, 1, '2024-08-06'),
(5, 3, 2, '2024-08-07');

SELECT * FROM clientes
SELECT nombre, ciudad FROM clientes WHERE ciudad = 'Buenos Aires' 

SELECT nombre, precio FROM productos WHERE precio > '40000';
SELECT * FROM productos ORDER BY precio DESC;

SELECT COUNT(*) FROM clientes AS total_clientes;
SELECT SUM(stock) AS total_unidades FROM productos;
SELECT AVG(precio) AS promedio_productos FROM productos;

SELECT * FROM productos WHERE precio BETWEEN'30000' AND '50000';

-- Muestra el nombre de cada cliente junto con la cantidad total de productos que ha comprado.

SELECT clientes.nombre AS Cliente, SUM(pedidos.cantidad) AS Total_comprado
FROM Pedidos JOIN Clientes
ON pedidos.cliente_id = clientes.cliente_id
GROUP BY clientes.nombre;


-- Muestra el nombre de los productos que han sido pedidos por el cliente "María Gómez".
SELECT nombre FROM productos JOIN pedidos ON pedido_id WHERE 'María Gómez' = nombre FROM cliente;

SELECT productos.nombre AS producto
FROM Pedidos JOIN Productos ON Pedidos.producto_id



SELECT clientes.nombre
FROM productos
JOIN pedidos ON producto_id = producto_id
JOIN clientes ON cliente_id = cliente_id
WHERE nombre = 'María Gómez';


-- Muestra la cantidad de pedidos realizados por cada cliente.
SELECT COUNT(cliente_id) FROM pedidos AS total_pedidos;

-- Muestra el nombre de los productos junto con la cantidad total vendida, ordenados de mayor a menor cantidad.

SELECT clientes.nombre AS Cliente, SUM(pedidos.cantidad) AS Total_comprado
FROM Pedidos JOIN Clientes
ON pedidos.cliente_id = clientes.cliente_id
GROUP BY clientes.nombre;

SELECT productos.nombre AS Producto
FROM Pedidos JOIN Productos ON Pedidos.producto_id = Productos.producto_id
JOIN Clientes ON Pedidos.cliente_id = Clientes.cliente_id
WHERE Clientes.nombre = 'María Gómez';


SELECT CLientes.nombre AS Cliente, COUNT(Pedidos.producto_id) AS Total_pedidos
FROM Pedidos JOIN Clientes ON Pedidos.cliente_id = Clientes.cliente_id
GROUP BY Clientes.nombre;


















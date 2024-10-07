-- ข้อมูลสำหรับตาราง Position (ตำแหน่งของพนักงาน)
INSERT INTO rent_position (name, description) VALUES 
('Manager', 'Manages the overall operations'),
('Sales', 'Handles sales and customer inquiries'),
('Technician', 'Maintains and repairs vehicles');

-- ข้อมูลสำหรับตาราง Employee (พนักงาน)
INSERT INTO rent_employee (first_name, last_name, phone_number, email, position_id) VALUES
('John', 'Doe', '0812345678', 'john@example.com', 1),
('Jane', 'Smith', '0823456789', 'jane@example.com', 2),
('Mark', 'Taylor', '0834567890', 'mark@example.com', 3);

-- ข้อมูลสำหรับตาราง Customer (ลูกค้า)
INSERT INTO rent_customer (first_name, last_name, phone_number, email) VALUES
('Alice', 'Johnson', '0845678901', 'alice@example.com'),
('Bob', 'Brown', '0856789012', 'bob@example.com'),
('Charlie', 'Davis', '0867890123', 'charlie@example.com');

-- ข้อมูลสำหรับตาราง VehicleType (ประเภทของรถ)
INSERT INTO rent_vehicleType (name, description, image) VALUES
('Sedan', '4-door family car', 'sedan.jpg'),
('SUV', 'Sport Utility Vehicle', 'suv.jpg'),
('Truck', 'Large vehicle for transporting goods', 'truck.jpg');

-- ข้อมูลสำหรับตาราง Vehicle (รถยนต์)
INSERT INTO rent_vehicle (type_id, name, image, insurance, price_per_hour, price_per_day, seat, description, employee_id, vehicle_status, number) VALUES
(1, 'Toyota Camry', 'camry.jpg', 'Full Coverage', 200, 1500, 5, 'Comfortable sedan', 1, TRUE, '1123a'),
(2, 'Ford Explorer', 'explorer.jpg', 'Full Coverage', 300, 2000, 7, 'Spacious SUV', 2, TRUE, '1123b'),
(3, 'Isuzu D-Max', 'dmax.jpg', 'Third-Party Only', 150, 1000, 2, 'Powerful truck for transport', 3, FALSE, '1123c');

-- ข้อมูลสำหรับตาราง Payment (การชำระเงิน)
INSERT INTO rent_payment (total_cost, created_at, pay_at, pay_status) VALUES
(5000, NOW(), '2024-10-05 10:00:00', TRUE),
(3000, NOW(), '2024-10-06 14:00:00', FALSE),
(7000, NOW(), '2024-10-07 12:00:00', TRUE);

-- ข้อมูลสำหรับตาราง Rent (การเช่ารถ)
INSERT INTO rent_rent (customer_id, vehicle_id, payment_id, start_time, end_time, return_status) VALUES
(1, 1, 1, '2024-10-01 09:00:00', '2024-10-01 17:00:00', FALSE),
(2, 2, 2, '2024-10-02 08:00:00', '2024-10-02 18:00:00', TRUE),
(3, 3, 3, '2024-10-03 09:00:00', '2024-10-03 17:00:00', FALSE);

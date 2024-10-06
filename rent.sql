-- เพิ่มข้อมูลใน rent_position
INSERT INTO rent_position (name, description)
VALUES
('Manager', 'Oversees operations'),
('Staff', 'Handles daily tasks');


-- เพิ่มข้อมูลใน rent_employee
INSERT INTO rent_employee (first_name, last_name, phone_number, email, position_id)
VALUES
('Alice', 'Brown', '0831234567', 'alice.brown@example.com', 1),
('Bob', 'Wilson', '0839876543', 'bob.wilson@example.com', 2);

-- เพิ่มข้อมูลใน rent_detail
INSERT INTO rent_detail (insurance, price_per_hour, price_per_day, seat, description)
VALUES
('Full Coverage', 500, 4000, 5, 'blah blah'),
('Basic Coverage', 300, 2500, 4, 'blah blah');


-- เพิ่มข้อมูลใน rent_vehicletype
INSERT INTO rent_vehicletype (name, description)
VALUES
('Sedan', 'Comfortable and small size vehicle'),
('SUV', 'Spacious vehicle for families');


-- เพิ่มข้อมูลใน rent_vehicle
INSERT INTO rent_vehicle (type_id, vehicle_number, vehicle_status, employee_id, detail_id, name)
VALUES
(1, '1234ABC', TRUE, 1, 1, 'test'),  -- ใช้ type_id = 1 (Sedan), employee_id = 1, detail_id = 1
(2, '5678XYZ', FALSE, 2, 2, 'test');  -- ใช้ type_id = 2 (SUV), employee_id = 2, detail_id = 2

-- เพิ่มข้อมูลใน rent_customer
INSERT INTO rent_customer (first_name, last_name, phone_number, email)
VALUES
('John', 'Doe', '0801234567', 'john.doe@example.com'),
('Jane', 'Smith', '0809876543', 'jane.smith@example.com');

-- เพิ่มข้อมูลใน rent_rent
INSERT INTO rent_rent (customer_id, vehicle_id, payment_id, start_time, end_time, return_status)
VALUES
(1, 1, 1, '2023-10-01 09:00:00', '2023-10-01 17:00:00', TRUE),  -- ใช้ customer_id = 1, vehicle_id = 1, payment_id = 1
(2, 2, 2, '2023-10-02 08:00:00', '2023-10-02 18:00:00', FALSE);  -- ใช้ customer_id = 2, vehicle_id = 2, payment_id = 2

-- เพิ่มข้อมูลใน rent_payment
INSERT INTO rent_payment (total_cost, created_at, pay_at, pay_status)
VALUES
(2500, '2023-10-02 09:00:00', NULL, FALSE),
(4000, '2023-10-02 10:00:00', '2023-10-02 10:30:00', TRUE);
-- Create the database
CREATE DATABASE momo_db;
USE momo_db;

-- Table for users/customers
CREATE TABLE customers (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    masked_phone VARCHAR(20),
    account_number VARCHAR(50),
    role VARCHAR(20),
    created_at DATETIME,
    last_seen DATETIME,
    source_notes VARCHAR(255)
);

-- Table for transaction categories
CREATE TABLE transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20),
    name VARCHAR(50),
    description VARCHAR(255),
    default_fee DECIMAL(10,2),
    direction VARCHAR(20)
);

-- Table for transactions
CREATE TABLE transactions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    tx_id VARCHAR(50),
    financial_tx_id VARCHAR(50),
    external_tx_id VARCHAR(50),
    amount DECIMAL(15,2),
    currency CHAR(3),
    transaction_datetime DATETIME,
    sms_date_epoch BIGINT,
    date_sent DATETIME,
    readable_date VARCHAR(50),
    fee DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    transaction_type_id INT,
    from_user_id INT,
    to_user_id INT,
    from_account VARCHAR(50),
    to_account VARCHAR(50),
    raw_body TEXT,
    sms_address VARCHAR(50),
    service_center VARCHAR(100),
    sms_protocol VARCHAR(20),
    sms_status VARCHAR(20),
    sms_read BOOLEAN,
    sms_locked BOOLEAN,
    contact_name VARCHAR(100)
);

-- Table for system logs
CREATE TABLE system_logs (
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_time DATETIME,
    level VARCHAR(20),
    source VARCHAR(50),
    message VARCHAR(255),
    transaction_id BIGINT,
    sms_sample_id VARCHAR(50),
    parsed BOOLEAN,
    error_details VARCHAR(255),
    processed_by VARCHAR(50)
);

-- Inserting sample data in each table

INSERT INTO customers (name, phone_number, masked_phone, account_number, role)
VALUES 
('Patrick Tuyizere', '+250780000000', '*********000', '0071001', 'sender'),
('Jane Smith', '+250781111111', '*********111', '0071002', 'receiver'),
('Robert Brown', '+250782222222', '*********222', '0071003', 'sender'),
('John Doe', '+250783333333', NULL, '0091004', 'agent'),
('Kivu Belt LTD', '+250782222222', NULL, '0041003', 'merchant');


INSERT INTO transactions (tx_id, financial_tx_id, external_tx_id, amount, currency, transaction_datetime, fee, balance_after, transaction_type_id, from_user_id, to_user_id, from_account, raw_body)
VALUES 
('73214484437', '76662021700', '47842929', 500.00, 'RWF', '2025-09-18 08:30:00', 10.00, 10590.00, 1, 1, 2, '0071001', '0071002', 'Transfer of 500 RWF...'),
('80573369999', '15462874800', '76952901', 10000.00, 'RWF', '2025-09-18 10:00:00', 10.00, 120560.00, 1, 1, 3, '0071056', '0071009', 'Transfer of 10000 RWF...'),
('93018486767', '78712021900', '47842930', 2000.00, 'RWF', '2025-09-18 11:30:00', 0.00, 638.00, 2, 1, 5, '0071003', '0041305', 'Payment of 2000 RWF...'),
('90233480001', '58922021111', '90854948', 8000.00, 'RWF', '2025-09-18 12:00:00', 10.00, 2580.00, 3, 4, 1, '0071001', '0071004', 'Transfer of 8000 RWF...'),
('90233480005', '67711122222', '10894766', 5000.00, 'RWF', '2025-09-18 14:00:00', 0.00, 1500.00, 5, 1, NULL, '0071001', NULL, 'Payment of 5000 RWF...');

INSERT INTO transaction_categories (code, name, description, default_fee, direction)
VALUES 
('*182*1*1', 'Transfer', 'Money transfer', 1000.00, 'debit'),
('*182*8*1', 'Payment', 'Goods payment', 1500.00, 'debit'),
('*182*', 'Withdraw', 'Bank withdraw', 10000.00, 'credit'),
('*860#', 'Payment', 'CanalBox payment', 25000.00, 'debit'),
('*182*1*1', 'Transfer', 'Money transfer', 1000.00, 'debit');

INSERT INTO system_logs (level, source, message, transaction_id, parsed, processed_by)
VALUES 
('INFO', 'parser', 'Transaction parsed successfully', 1, TRUE, 'system'),
('INFO', 'parser', 'Transaction parsed successfully', 2, TRUE, 'system'),
('ERROR', 'parser', 'Missing recepient id', 3, FALSE, 'system'),
('INFO', 'validator', 'Search inputs validated successfully', 4, TRUE, 'system'),
('ERROR', 'validator', 'Search inputs failed validation.', 5, FALSE, 'system');
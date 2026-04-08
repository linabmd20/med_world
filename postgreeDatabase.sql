-- USER TABLE
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ACCOUNT TABLE
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(12,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id)
);

-- DATA
INSERT INTO users (full_name,email) VALUES
('Alice Smith','alice@email.com'),
('Bob Johnson','bob@email.com'),
('Charlie Brown','charlie@email.com');

INSERT INTO accounts (user_id,account_type,balance) VALUES
(1,'Checking',1500),
(1,'Savings',5000),
(2,'Checking',2200),
(3,'Savings',10000);
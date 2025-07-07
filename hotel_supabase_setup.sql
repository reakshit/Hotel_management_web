-- Drop tables if they already exist to ensure a clean start
-- Order matters due to foreign key constraints
DROP TABLE IF EXISTS "TRANSACTION";
DROP TABLE IF EXISTS "CUSTOMERS";
DROP TABLE IF EXISTS "ROOMS";

-- Create the ROOMS table
CREATE TABLE "ROOMS" (
    "Roomno" VARCHAR(50) PRIMARY KEY,
    "RoomType" VARCHAR(50) NOT NULL,
    "RoomPrice" DECIMAL(10, 2) NOT NULL
);

-- Create the CUSTOMERS table
CREATE TABLE "CUSTOMERS" (
    "CustomerID" VARCHAR(50) PRIMARY KEY,
    "Name" VARCHAR(100) NOT NULL,
    "Room" VARCHAR(50) DEFAULT '000' -- '000' indicates no room assigned
);

-- Create the TRANSACTION table
-- Use SERIAL for auto-incrementing primary key in PostgreSQL
CREATE TABLE "TRANSACTION" (
    "TransactionID" SERIAL PRIMARY KEY,
    "CustomerID" VARCHAR(50) NOT NULL,
    "Roomno" VARCHAR(50) NOT NULL,
    "isOccupied" VARCHAR(10) NOT NULL,
    "price" DECIMAL(10, 2),
    FOREIGN KEY ("CustomerID") REFERENCES "CUSTOMERS"("CustomerID"),
    FOREIGN KEY ("Roomno") REFERENCES "ROOMS"("Roomno")
);

-- Insert sample data into ROOMS table
INSERT INTO "ROOMS" ("Roomno", "RoomType", "RoomPrice") VALUES
('101', 'Standard', 100.00),
('102', 'Standard', 100.00),
('201', 'Deluxe', 150.00),
('202', 'Deluxe', 150.00),
('301', 'Suite', 250.00);

-- Insert sample data into CUSTOMERS table
INSERT INTO "CUSTOMERS" ("CustomerID", "Name", "Room") VALUES
('C001', 'Alice Smith', '000'),
('C002', 'Bob Johnson', '000'),
('C003', 'Charlie Brown', '000');

-- Insert sample data into TRANSACTION table
-- Note: For transactions, you might want to simulate check-ins by updating the CUSTOMERS.Room field
-- and then inserting into TRANSACTION.
-- Here's an example of a customer checked into a room:

-- Simulate C001 checking into Room 101
UPDATE "CUSTOMERS" SET "Room" = '101' WHERE "CustomerID" = 'C001';
INSERT INTO "TRANSACTION" ("CustomerID", "Roomno", "isOccupied", "price") VALUES
('C001', '101', 'yes', NULL); -- Price is NULL on check-in, calculated on check-out

-- Simulate C002 checking into Room 201
UPDATE "CUSTOMERS" SET "Room" = '201' WHERE "CustomerID" = 'C002';
INSERT INTO "TRANSACTION" ("CustomerID", "Roomno", "isOccupied", "price") VALUES
('C002', '201', 'yes', NULL);

-- Example of a past transaction (customer checked out)
-- This assumes C003 was in Room 102 and checked out for a price of 200.00
-- Note: The CUSTOMERS.Room for C003 would be '000' if they are checked out.
INSERT INTO "TRANSACTION" ("CustomerID", "Roomno", "isOccupied", "price") VALUES
('C003', '102', 'no', 200.00);
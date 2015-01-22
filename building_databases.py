import sqlite3
db_name = "pharmacy_database.db"
with sqlite3.connect(db_name)as db:
    cursor = db.cursor()
    sql = """ create table Customer
    (CustomerID integer,
    FirstName text,
    LastName text,
    Street text,
    Town text,
    Postcode real,
    TelephoneNum integer,
    EmailAddress text,
    Primary Key(CustomerID))"""
    
    cursor.execute(sql)

    sql = """ create table Prescription
    (PrescriptionCode integer,
    PharmacistID real,
    CustomerID real,
    QuantityOfMed real,
    Primary Key(PrescriptionCode),
    FOREIGN KEY (PharmacistID) REFERENCES Persons(PharmacistID),
    FOREIGN KEY (CustomerID) REFERENCES Persons(CustomerID))"""
    
    cursor.execute(sql)
        
    sql = """ create table Orders
    (OrderNum integer,
    OrderDate real,
    OrderSize real,
    Primary Key(OrderNum))"""
    
    cursor.execute(sql)

    sql = """ create table product
    (ProductID integer,
    ProductName text,
    ProductWeight real,
    ProductCode real,
    Price real,
    Primary Key(ProductID))"""

    cursor.execute(sql)
    
    sql = """ create table Pharmacist
    (PharmacistID integer, 
    PharmacistName text, 
    PharmacistEmail text, 
    PharmacistTown text, 
    PharmacistStreet text, 
    PharmacistPostcode real, 
    Primary Key(PharmacistID))"""

    cursor.execute(sql)
    
    sql = """ create table Warehouse
    (WarehouseNum integer,
    WarehouseTown text,
    WarehouseStreet text,
    WarehousePostcode real,
    Primary Key(WarehouseNum))"""

    cursor.execute(sql)
    
    sql = """ create table Manufacturer
    (Manufacturer text,
    Product text,
    ManufacturerTown text,
    ManufacturerStreet text,
    ManufacturerPostcode real,
    Primary Key(Manufacturer),
    FOREIGN KEY (Product) REFERENCES Persons(Product))"""

    cursor.execute(sql)
        
    sql = """ create table PrescriptionProduct
    (PrescriptionProduct text,
    Product text,
    Prescription text,
    Primary Key(PrescriptionProduct),
    FOREIGN KEY (Product) REFERENCES Persons(Product),
    FOREIGN KEY (Prescription) REFERENCES Persons(Prescription))"""

    cursor.execute(sql)
        
    sql = """ create table ProductWarehouse
    (ProductWarehouse text,
    Product text,
    Warehouse text,
    Primary Key(ProductWarehouse),
    FOREIGN KEY (Product) REFERENCES Persons(Product),
    FOREIGN KEY (Warehouse) REFERENCES Persons(Warehouse))"""

    cursor.execute(sql)
            
    sql = """ create table OrderProduct
    (OrderProduct text,
    Product text,
    Orders text,
    Primary Key(OrderProduct),
    FOREIGN KEY (Product) REFERENCES Persons(Product),
    FOREIGN KEY (Orders) REFERENCES Persons(Orders))"""

    cursor.execute(sql)
    
    db.commit()   



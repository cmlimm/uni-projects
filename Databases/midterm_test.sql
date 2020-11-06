CREATE TABLE material (IDmat INT PRIMARY KEY, NameMat CHAR(15), price INT);
CREATE TABLE product (IDproduct INT PRIMARY KEY, NameProd CHAR(15));
CREATE TABLE composition (IDproduct INT, IDmat INT, quantityMQ INT, PRIMARY KEY (IDproduct, IDmat),
CONSTRAINT Fk10 FOREIGN KEY (IDproduct) REFERENCES product(IDproduct),
CONSTRAINT Fk20 FOREIGN KEY (IDmat) REFERENCES material(IDmat));
CREATE TABLE productionHall (IDproductionHall INT PRIMARY KEY, NameproductionHall CHAR(15));
CREATE TABLE release1 (Nrelease INT PRIMARY KEY, DateRel date, IDproductionHall INT,
CONSTRAINT Fk11 FOREIGN KEY (IDproductionHall) REFERENCES productionHall(IDproductionHall));
CREATE TABLE releaseSP (Nrelease INT, IDmat INT, quantityRel INT, PRIMARY KEY (Nrelease, IDmat),
CONSTRAINT Fk12 FOREIGN KEY (Nrelease) REFERENCES release1(Nrelease),
CONSTRAINT Fk13 FOREIGN KEY (IDmat) REFERENCES material(IDmat));
CREATE TABLE transfer (IDtransfer INT, IDproductionHall INT, DateTr date, PRIMARY KEY (IDtransfer, IDproductionHall),
CONSTRAINT FK14 FOREIGN KEY (IDproductionHall) REFERENCES productionHall(IDproductionHall));
CREATE TABLE specTransfer (IDtransfer INT, IDproductionHall INT, IDproduct INT, QuantityTr INT,
CONSTRAINT FK15 FOREIGN KEY (IDproductionHall, IDtransfer) REFERENCES transfer(IDproductionHall, IDtransfer),
CONSTRAINT FK16 FOREIGN KEY (IDproduct) REFERENCES product(IDproduct));
CREATE TABLE partner (IDpartner INT PRIMARY KEY, NameP CHAR(15), attributes TEXT);
CREATE TABLE order1 (IDorder INT PRIMARY KEY, DateOr date, IDpartner INT, total INT,
CONSTRAINT FK17 FOREIGN KEY (IDpartner) REFERENCES partner(IDpartner));
CREATE TABLE orderSpec (IDorder INT, IDproduct INT, DateShipment date, quantityOr INT,
PRIMARY KEY (IDorder, IDproduct, DateShipment),
CONSTRAINT FK18 FOREIGN KEY (IDorder) REFERENCES order1(IDorder),
CONSTRAINT FK19 FOREIGN KEY (IDproduct) REFERENCES product(IDproduct));
CREATE TABLE supply (IDsupply INT, IDpartner INT, DateSup date, PRIMARY KEY (IDsupply, IDpartner),
CONSTRAINT FK21 FOREIGN KEY (IDpartner) REFERENCES partner(IDpartner));
CREATE TABLE supplySpec (IDsupply INT, IDpartner INT, IDmat INT, PriceSup INT, QuantitySup INT,
PRIMARY KEY (IDsupply, IDpartner, IDmat),
CONSTRAINT FK22 FOREIGN KEY (IDsupply, IDpartner) REFERENCES supply(IDsupply, IDpartner),
CONSTRAINT FK23 FOREIGN KEY (IDmat) REFERENCES material(IDmat));
LOAD DATA INFILE '/Users/cmlimm/Downloads/Uploads'
INTO TABLE material
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY 'n'
IGNORE 1 ROWS;

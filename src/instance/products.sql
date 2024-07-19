BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "products" (
	"id"	INTEGER NOT NULL,
	"product_name"	VARCHAR(100) NOT NULL,
	"price"	INTEGER NOT NULL,
	"color"	VARCHAR(100) NOT NULL,
	"dimensions"	VARCHAR(100),
	"category"	VARCHAR(100) NOT NULL,
	"image_path"	VARCHAR(100) NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "products" VALUES (1,'Backpack',60,'French Blue & White w/ Adjustable Straps','D = 7 3/4" H = 9" W = 10"','Bags','../css/images/products/Backpack Navy-White/Backpack-7.png');
INSERT INTO "products" VALUES (2,'Bucket Bag',50,'Mint Green & White w/ Detachable Straps','D = 7 1/4" H = 10 1/2" W = 11 1/2"','Bags','../css/images/products/Bucket Bag Blue-White/Bucket Bag-1.png');
INSERT INTO "products" VALUES (3,'Bucket Bag',50,'Dark & Lt Grey','D = 7 1/4" H = 9" W = 11"','Bags','../css/images/products/Bucket Bag Grey/Bucket Bag-10.png');
INSERT INTO "products" VALUES (4,'Bucket Bag',40,'Peach','D = 8" H = 7" W = 10"','Bags','../css/images/products/Bucket Bag Pink/Bucket Bag-3.png');
INSERT INTO "products" VALUES (5,'Bucket Bag',50,'Pink & White','D = 8 3/4" H = 9" W = 10 1/2"','Bags','../css/images/products/Bucket Bag Pink-White/Bucket Bag-2.png');
INSERT INTO "products" VALUES (6,'Bucket Bag',50,'Tan & Brown w/ Detachable Straps','D = 8 1/2" H = 10 1/4" W = 12"','Bags','../css/images/products/Bucket Bag Tan-Brown/Bucket Bag-8.png');
INSERT INTO "products" VALUES (7,'Bucket Bag',40,'Forest Green & White','D = 10" H = 9" W = 11 1/2"','Bags','../css/images/products/Bucket Bag White-Green/Bucket Bag-11.png');
INSERT INTO "products" VALUES (8,'Bucket Bag',40,'Grey & White','D = 10" H = 8 1/2" W = 11"','Bags','../css/images/products/Bucket Bag White-Grey/Bucket Bag-14.png');
INSERT INTO "products" VALUES (9,'Bucket Bag',45,'White & Purple w/ Adjustable and Detachable Straps','D = 7" H = 8 1/2" W = 9"','Bags','../css/images/products/Bucket Bag White-Purple/Bucket Bag-12.png');
INSERT INTO "products" VALUES (10,'Bucket Bag',50,'Peach & White w/ Detachable Straps','D = 8" H = 9 1/2" W = 11"','Bags','../css/images/products/Bucket Bag White-Salmon/Bucket Bag-5.png');
INSERT INTO "products" VALUES (11,'Bucket Bag',45,'White & Mint Green','D = 8" H = 9" W = 11"','Bags','../css/images/products/Bucket Bag White-Teal/Bucket Bag-13.png');
INSERT INTO "products" VALUES (12,'Bucket Bag',40,'Yellow & White w/ Detachable Straps',NULL,'Bags','../css/images/products/Bucket Bag White-Yellow/Bucket Bag-9.png');
INSERT INTO "products" VALUES (13,'Kids Bag',10,'Mint Green w/ White Ribbon',NULL,'Other Bags','../css/images/products/Kid Bag Teal-White/Kid Bag-6.png');
INSERT INTO "products" VALUES (14,'Mini Bucket Bag',30,'Coral',NULL,'Other Bags','../css/images/products/Mini Bucket Bag Pink/D1E158A2-77C3-422A-BD1D-19A6F4B35194_1_105_c.jpeg');
INSERT INTO "products" VALUES (15,'Small Tote Bag',35,'Peach & Ecru',NULL,'Other Bags','../css/images/products/Mini Bucket Bag Pink-White/Bucket Bag-16.png');
INSERT INTO "products" VALUES (16,'Large Tote Bag',65,'Ecru w/ Polka Dots',NULL,'Other Bags','../css/images/products/Tote Bag Polka/Tote Bag-18.png');
INSERT INTO "products" VALUES (17,'Wristlet',35,'Grey w/ Key Charm',NULL,'Other Bags','../css/images/products/Wristlet Grey/Wristlet-17.png');
INSERT INTO "products" VALUES (18,'Wristlet',30,'Lime Green',NULL,'Other Bags','../css/images/products/Wristlet Lime/Wristlet-4.png');
INSERT INTO "products" VALUES (19,'Wristlet',40,'Watermelon w/ Key Charm',NULL,'Other Bags','../css/images/products/Wristlet Watermelon/04D8C30D-8500-4C98-B485-E0000AB9C585_1_105_c.jpeg');
INSERT INTO "products" VALUES (20,'Bucket Hat',40,'Brown w/ Tan Designs',NULL,'Hats','../css/images/products/Bucket Hat Brown-Tan/Screenshot 2023-10-04 at 11.24.42 AM.png');
INSERT INTO "products" VALUES (21,'Bucket Hat',40,'Grey w/ Designs',NULL,'Hats','../css/images/products/Bucket Hat Grey/Screenshot 2023-10-04 at 11.23.42 AM.png');
INSERT INTO "products" VALUES (22,'Bucket Hat',50,'Grey w/ Pink Flowers',NULL,'Hats','../css/images/products/Bucket Hat Grey-Pink/Screenshot 2023-10-04 at 11.16.21 AM.png');
INSERT INTO "products" VALUES (23,'Bucket Hat',30,'Grey & White',NULL,'Hats','../css/images/products/Bucket Hat Grey-White/Screenshot 2023-10-04 at 11.15.38 AM.png');
INSERT INTO "products" VALUES (24,'Bucket Hat',30,'Navy Blue',NULL,'Hats','../css/images/products/Bucket Hat Navy/Screenshot 2023-10-04 at 11.18.58 AM.png');
INSERT INTO "products" VALUES (25,'Bucket Hat',35,'Purple & White',NULL,'Hats','../css/images/products/Bucket Hat Purple-White/Screenshot 2023-10-04 at 11.22.34 AM.png');
INSERT INTO "products" VALUES (26,'Bucket Hat',40,'Red & White Flowers',NULL,'Hats','../css/images/products/Bucket Hat Red-White/Screenshot 2023-10-04 at 11.19.51 AM.png');
COMMIT;

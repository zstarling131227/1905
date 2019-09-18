-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: db2
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bank1`
--

DROP TABLE IF EXISTS `bank1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bank1` (
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank1`
--

LOCK TABLES `bank1` WRITE;
/*!40000 ALTER TABLE `bank1` DISABLE KEYS */;
INSERT INTO `bank1` VALUES ('vip1',17000.00),('vip2',2000.00);
/*!40000 ALTER TABLE `bank1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cla`
--

DROP TABLE IF EXISTS `cla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cla` (
  `class` enum('a','b','c') DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10017 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cla`
--

LOCK TABLES `cla` WRITE;
/*!40000 ALTER TABLE `cla` DISABLE KEYS */;
INSERT INTO `cla` VALUES ('a','andy',10011,85),('b','eason',10012,98),('c','mike',10013,82),('a','tony',10014,63),('b','jack',10015,92),('a','ruby',10016,85);
/*!40000 ALTER TABLE `cla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master`
--

DROP TABLE IF EXISTS `master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `class` varchar(30) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master`
--

LOCK TABLES `master` WRITE;
/*!40000 ALTER TABLE `master` DISABLE KEYS */;
INSERT INTO `master` VALUES (1,'唐伯虎','AID1905',300.00),(3,'祝枝山','AID1905',300.00),(10,'秋菊','AID1905',300.00),(11,'腊梅','AID1905',300.00),(12,'秋菊','AID1905',300.00);
/*!40000 ALTER TABLE `master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scoretab`
--

DROP TABLE IF EXISTS `scoretab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scoretab` (
  `rank` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `score` float(5,2) DEFAULT NULL,
  `phone` char(11) DEFAULT NULL,
  `class` char(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scoretab`
--

LOCK TABLES `scoretab` WRITE;
/*!40000 ALTER TABLE `scoretab` DISABLE KEYS */;
INSERT INTO `scoretab` VALUES (1,'å¤§ç©ºç¿¼',98.50,'13016880001','AID1903'),(2,'æ¾äºº',98.00,'13016880002','AID1903'),(3,'æ°´å†°æœˆ',98.00,'13016880003','AID1903'),(4,'æ˜ŸçŸ¢',97.50,'13016880004','AID1903'),(5,'ç´«é¾™',96.50,'13016880005','AID1903'),(6,'å¼ é£ž',96.00,'13016880006','AID1903'),(7,'å…³ç¾½',94.50,'13016880007','AID1903'),(8,'åˆ˜å¤‡',94.50,'13016880008','AID1903'),(9,'é‡‘èŠ±å©†å©†',94.00,'13016880009','AID1903'),(10,'ç´«è¡«é¾™çŽ‹',93.00,'13016880010','AID1903'),(11,'é’ç¿¼è çŽ‹',92.50,'13016880011','AID1903'),(12,'ç™½çœ‰é¹°çŽ‹',92.50,'13016880012','AID1903'),(13,'é‡‘æ¯›ç‹®çŽ‹',92.50,'13016880013','AID1903'),(14,'å¼ ä¸‰ä¸°',92.00,'13016880014','AID1903'),(15,'å¼ æ— å¿Œ',92.00,'13016880015','AID1903'),(16,'èµµæ•',91.50,'13016880016','AID1903'),(17,'å°æ˜­',91.50,'13016880017','AID1903'),(18,'å‘¨èŠ·è‹¥',91.50,'13016880018','AID1903'),(19,'è¶³çƒå°å°†',91.00,'13016880019','AID1903'),(20,'åœ£æ–—å£«',90.50,'13016880020','AID1903'),(21,'é»„é‡‘åœ£è¡£',90.00,'13016880021','AID1903'),(22,'èƒ¡äº¥',90.00,'13016880022','AID1903'),(23,'æ¨è´µå¦ƒ',89.00,'13016880023','AID1903'),(24,'å®å½“çŒ«',88.50,'13016880024','AID1903'),(25,'å»åˆ«',88.50,'13016880025','AID1903'),(26,'æŠ–éŸ³',87.50,'13016880026','AID1903'),(27,'ç«å±±',87.50,'13016880027','AID1903'),(28,'ç«ç®­',87.00,'13016880028','AID1903'),(29,'éª‘å£«',86.00,'13016880029','AID1903'),(30,'å°å¯ä¹',85.00,'13016880030','AID1903'),(31,'å°é›ªç¢§',83.50,'13016880031','AID1903'),(32,'ç¾Žå¹´è¾¾',82.50,'13016880032','AID1903'),(33,'å°ç”œç”œ',81.00,'13016880033','AID1903'),(34,'æ¬¢æ¬¢',81.00,'13016880034','AID1903'),(35,'ä¹ä¹',81.00,'13016880035','AID1903'),(36,'ç§‹ç§‹',80.00,'13016880036','AID1903'),(37,'è¾‰è¾‰',79.50,'13016880037','AID1903'),(38,'å†›å†›',77.00,'13016880038','AID1903'),(39,'é˜³é˜³',74.50,'13016880039','AID1903'),(40,'ç™½çœ‰å¤§ä¾ ',73.00,'13016880040','AID1903'),(41,'æ¨è¿‡',68.00,'13016880041','AID1903'),(42,'å°é¾™å¥³',66.00,'13016880042','AID1903'),(43,'éƒ­è¥„',64.50,'13016880043','AID1903'),(44,'å‘¨èŠ·è‹¥',60.00,'13016880044','AID1903'),(45,'ç¥žé›•',60.00,'13016880045','AID1903'),(46,'æˆ˜ç¥ž',60.00,'13016880046','AID1903'),(47,'åªæ‰‹é®å¤©',60.00,'13016880047','AID1903'),(48,'çŽ‹è€…è£è€€',60.00,'13016880048','AID1903');
/*!40000 ALTER TABLE `scoretab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slave`
--

DROP TABLE IF EXISTS `slave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slave` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `slave_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slave`
--

LOCK TABLES `slave` WRITE;
/*!40000 ALTER TABLE `slave` DISABLE KEYS */;
INSERT INTO `slave` VALUES (1,'唐伯虎',300.00),(3,'祝枝山',300.00),(10,'秋菊',300.00),(1,'腊梅',300.00);
/*!40000 ALTER TABLE `slave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slave1`
--

DROP TABLE IF EXISTS `slave1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slave1` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slave1`
--

LOCK TABLES `slave1` WRITE;
/*!40000 ALTER TABLE `slave1` DISABLE KEYS */;
/*!40000 ALTER TABLE `slave1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slave2`
--

DROP TABLE IF EXISTS `slave2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slave2` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `slave2_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slave2`
--

LOCK TABLES `slave2` WRITE;
/*!40000 ALTER TABLE `slave2` DISABLE KEYS */;
/*!40000 ALTER TABLE `slave2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slave3`
--

DROP TABLE IF EXISTS `slave3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slave3` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` decimal(6,2) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `slave3_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `master` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slave3`
--

LOCK TABLES `slave3` WRITE;
/*!40000 ALTER TABLE `slave3` DISABLE KEYS */;
INSERT INTO `slave3` VALUES (NULL,'点秋香',300.00),(3,'祝枝山',300.00);
/*!40000 ALTER TABLE `slave3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test1`
--

DROP TABLE IF EXISTS `test1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test1` (
  `id` int(3) unsigned zerofill DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test1`
--

LOCK TABLES `test1` WRITE;
/*!40000 ALTER TABLE `test1` DISABLE KEYS */;
INSERT INTO `test1` VALUES (001);
/*!40000 ALTER TABLE `test1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_int`
--

DROP TABLE IF EXISTS `test_int`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_int` (
  `id` int(3) unsigned zerofill DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_int`
--

LOCK TABLES `test_int` WRITE;
/*!40000 ALTER TABLE `test_int` DISABLE KEYS */;
INSERT INTO `test_int` VALUES (001);
/*!40000 ALTER TABLE `test_int` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-10 19:56:46

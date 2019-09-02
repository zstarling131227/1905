-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: mysite4_db
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add author',7,'add_author'),(20,'Can change author',7,'change_author'),(21,'Can delete author',7,'delete_author'),(22,'Can add book',8,'add_book'),(23,'Can change book',8,'change_book'),(24,'Can delete book',8,'delete_book'),(25,'Can add wife',9,'add_wife'),(26,'Can change wife',9,'change_wife'),(27,'Can delete wife',9,'delete_wife'),(28,'Can add publisher',10,'add_publisher'),(29,'Can change publisher',10,'change_publisher'),(30,'Can delete publisher',10,'delete_publisher'),(31,'Can add book2',11,'add_book2'),(32,'Can change book2',11,'change_book2'),(33,'Can delete book2',11,'delete_book2'),(34,'Can add author3',12,'add_author3'),(35,'Can change author3',12,'change_author3'),(36,'Can delete author3',12,'delete_author3'),(37,'Can add book3',13,'add_book3'),(38,'Can change book3',13,'change_book3'),(39,'Can delete book3',13,'delete_book3'),(40,'Can add user',14,'add_user'),(41,'Can change user',14,'change_user'),(42,'Can delete user',14,'delete_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$pxLVawIMNmst$G1MYUO0ZL8Ap1siV4Ro1yZIo7dCUXLgTcDdFJWH9FkU=','2019-08-17 07:59:32.493359',1,'zstarling','','','xxx@tedu.cn',1,1,'2019-08-16 01:50:10.187539'),(2,'pbkdf2_sha256$36000$LacL59swqwiL$Qlv3FmkpngMBEsltST44MlqZrvjVRfqgrObUO7OBrsc=','2019-08-16 02:16:00.000000',1,'zstarling1','','','123456789@tedu.cn',1,1,'2019-08-16 02:13:00.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore2_author3`
--

DROP TABLE IF EXISTS `bookstore2_author3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore2_author3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore2_author3`
--

LOCK TABLES `bookstore2_author3` WRITE;
/*!40000 ALTER TABLE `bookstore2_author3` DISABLE KEYS */;
INSERT INTO `bookstore2_author3` VALUES (1,'吕泽'),(2,'魏老师'),(3,'wang'),(4,'zhang'),(5,'xixi');
/*!40000 ALTER TABLE `bookstore2_author3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore2_book2`
--

DROP TABLE IF EXISTS `bookstore2_book2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore2_book2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bookstore2_book2_publisher_id_e33a068c_fk_bookstore` (`publisher_id`),
  CONSTRAINT `bookstore2_book2_publisher_id_e33a068c_fk_bookstore` FOREIGN KEY (`publisher_id`) REFERENCES `bookstore2_publisher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore2_book2`
--

LOCK TABLES `bookstore2_book2` WRITE;
/*!40000 ALTER TABLE `bookstore2_book2` DISABLE KEYS */;
INSERT INTO `bookstore2_book2` VALUES (1,'C++',1),(2,'Java',1),(3,'Python',1),(4,'西游记',2),(5,'水浒',2);
/*!40000 ALTER TABLE `bookstore2_book2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore2_book3`
--

DROP TABLE IF EXISTS `bookstore2_book3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore2_book3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore2_book3`
--

LOCK TABLES `bookstore2_book3` WRITE;
/*!40000 ALTER TABLE `bookstore2_book3` DISABLE KEYS */;
INSERT INTO `bookstore2_book3` VALUES (1,'Python'),(2,'C++'),(3,'C'),(4,'Java'),(5,'Linux'),(6,'C'),(7,'C++'),(8,'Java'),(9,'Linux'),(10,'windows');
/*!40000 ALTER TABLE `bookstore2_book3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore2_book3_authors`
--

DROP TABLE IF EXISTS `bookstore2_book3_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore2_book3_authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book3_id` int(11) NOT NULL,
  `author3_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bookstore2_book3_authors_book3_id_author3_id_50ddf582_uniq` (`book3_id`,`author3_id`),
  KEY `bookstore2_book3_aut_author3_id_edfa6891_fk_bookstore` (`author3_id`),
  CONSTRAINT `bookstore2_book3_aut_author3_id_edfa6891_fk_bookstore` FOREIGN KEY (`author3_id`) REFERENCES `bookstore2_author3` (`id`),
  CONSTRAINT `bookstore2_book3_aut_book3_id_26f745b8_fk_bookstore` FOREIGN KEY (`book3_id`) REFERENCES `bookstore2_book3` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore2_book3_authors`
--

LOCK TABLES `bookstore2_book3_authors` WRITE;
/*!40000 ALTER TABLE `bookstore2_book3_authors` DISABLE KEYS */;
INSERT INTO `bookstore2_book3_authors` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(6,5,2),(7,6,3),(8,7,3),(11,8,1),(12,8,2),(13,8,3),(9,8,4),(10,9,4),(15,10,4),(14,10,5);
/*!40000 ALTER TABLE `bookstore2_book3_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore2_publisher`
--

DROP TABLE IF EXISTS `bookstore2_publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore2_publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore2_publisher`
--

LOCK TABLES `bookstore2_publisher` WRITE;
/*!40000 ALTER TABLE `bookstore2_publisher` DISABLE KEYS */;
INSERT INTO `bookstore2_publisher` VALUES (2,'北京大学出版社'),(1,'清华大学出版社');
/*!40000 ALTER TABLE `bookstore2_publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore_author`
--

DROP TABLE IF EXISTS `bookstore_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(254),
  PRIMARY KEY (`id`),
  KEY `bookstore_author_name_f0a34c06` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore_author`
--

LOCK TABLES `bookstore_author` WRITE;
/*!40000 ALTER TABLE `bookstore_author` DISABLE KEYS */;
INSERT INTO `bookstore_author` VALUES (1,'王老师',28,'wangweichao@tedu.cn'),(2,'吕老师',31,'lvze@tedu.cn'),(3,'祁老师',30,'qitx@tedu.cn'),(5,'嘻嘻',24,'123456789@tedu.cn'),(6,'钥玥',23,'123456789@tedu.cn'),(7,'王老师',1,'xxx@tedu.cn');
/*!40000 ALTER TABLE `bookstore_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookstore_wife`
--

DROP TABLE IF EXISTS `bookstore_wife`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookstore_wife` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `author_id` (`author_id`),
  CONSTRAINT `bookstore_wife_author_id_85e6a2ee_fk_bookstore_author_id` FOREIGN KEY (`author_id`) REFERENCES `bookstore_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookstore_wife`
--

LOCK TABLES `bookstore_wife` WRITE;
/*!40000 ALTER TABLE `bookstore_wife` DISABLE KEYS */;
INSERT INTO `bookstore_wife` VALUES (1,'zhang',23,5),(2,'wang',24,6);
/*!40000 ALTER TABLE `bookstore_wife` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-08-16 02:13:40.588257','2','zstarling1',1,'[{\"added\": {}}]',4,1),(2,'2019-08-16 02:16:03.296259','2','zstarling1',2,'[{\"changed\": {\"fields\": [\"email\", \"is_staff\", \"is_superuser\"]}}]',4,1),(3,'2019-08-16 02:52:33.639367','2','zstarling1',2,'[{\"changed\": {\"fields\": [\"last_login\"]}}]',4,2),(4,'2019-08-16 03:28:06.747299','21','书名：java',2,'[{\"changed\": {\"fields\": [\"market_price\"]}}]',8,2),(5,'2019-08-16 03:28:06.888198','19','书名：Rstudio',2,'[{\"changed\": {\"fields\": [\"market_price\"]}}]',8,2),(6,'2019-08-16 06:42:52.384494','1','Wife object',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,2),(7,'2019-08-16 06:43:14.583189','1','Wife object',2,'[{\"changed\": {\"fields\": [\"author\"]}}]',9,2),(8,'2019-08-16 06:45:07.981458','1','Wife object',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,2),(9,'2019-08-16 06:48:50.328019','1','妻子：zhang',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,2),(10,'2019-08-16 07:52:28.791255','1','出版社：清华大学出版社',1,'[{\"added\": {}}]',10,2),(11,'2019-08-16 07:52:42.215362','2','出版社：北京大学出版社',1,'[{\"added\": {}}]',10,2),(12,'2019-08-16 08:53:26.210792','5','书名：Linux',2,'[{\"changed\": {\"fields\": [\"authors\"]}}]',13,2),(13,'2019-08-16 09:14:39.668004','8','书名：Java',2,'[{\"changed\": {\"fields\": [\"authors\"]}}]',13,2),(14,'2019-08-17 08:00:03.020026','6','用户wangweichao',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'bookstore','author'),(8,'bookstore','book'),(9,'bookstore','wife'),(12,'bookstore2','author3'),(11,'bookstore2','book2'),(13,'bookstore2','book3'),(10,'bookstore2','publisher'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(14,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-15 01:40:40.729121'),(2,'auth','0001_initial','2019-08-15 01:40:50.524606'),(3,'admin','0001_initial','2019-08-15 01:40:52.640697'),(4,'admin','0002_logentry_remove_auto_add','2019-08-15 01:40:52.782989'),(5,'contenttypes','0002_remove_content_type_name','2019-08-15 01:40:53.954826'),(6,'auth','0002_alter_permission_name_max_length','2019-08-15 01:40:54.865885'),(7,'auth','0003_alter_user_email_max_length','2019-08-15 01:40:55.776783'),(8,'auth','0004_alter_user_username_opts','2019-08-15 01:40:55.823749'),(9,'auth','0005_alter_user_last_login_null','2019-08-15 01:40:56.439600'),(10,'auth','0006_require_contenttypes_0002','2019-08-15 01:40:56.489177'),(11,'auth','0007_alter_validators_add_error_messages','2019-08-15 01:40:56.549218'),(12,'auth','0008_alter_user_username_max_length','2019-08-15 01:40:58.502566'),(13,'sessions','0001_initial','2019-08-15 01:40:59.096169'),(14,'bookstore','0001_initial','2019-08-15 01:58:34.233216'),(15,'bookstore','0002_auto_20190815_0201','2019-08-15 02:01:42.596211'),(16,'bookstore','0003_auto_20190816_1139','2019-08-16 03:39:39.883904'),(17,'bookstore','0004_auto_20190816_1424','2019-08-16 06:24:08.487352'),(18,'bookstore2','0001_initial','2019-08-16 07:43:16.657723'),(19,'bookstore2','0002_author3_book3','2019-08-16 08:23:00.160437'),(20,'user','0001_initial','2019-08-17 06:45:09.174765');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('erfotgai922rp1wuklijdy1nghcvw765','NDk3ZTA0NWI5M2FmZjY5OWRlNmFiNWViYTllOTE0NmU3ODE5NmZhOTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxN2VjNzk3MDRiNTQ2MTNhYmYzMDU4MmIzNTI0N2Y4MTQ3ODM1OGQ4In0=','2019-08-30 02:16:52.447699'),('hxaycp3uls5ow9iwuy34xkx3sezv4c6e','YTRhNDc1NTY2NjgzMWZiMDExMDFhMWFiNGE4MmViZGQwMmRlODdhNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDRkZTljNmJjNGJmZTY5ZjBhNjY5ZDI3YjYzMDE4NzQxZmM0ZjE2In0=','2019-08-31 07:59:32.547601');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mybook`
--

DROP TABLE IF EXISTS `mybook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mybook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `market_price` decimal(7,2) NOT NULL,
  `pub` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mybook`
--

LOCK TABLES `mybook` WRITE;
/*!40000 ALTER TABLE `mybook` DISABLE KEYS */;
INSERT INTO `mybook` VALUES (1,'Python',20.00,34.00,'清华大学出版社'),(2,'Python3',60.00,56.00,'清华大学出版社'),(3,'Django',70.00,75.00,'清华大学出版社'),(4,'JQuery',90.00,85.00,'机械工业出版社'),(5,'Linux',80.00,65.00,'机械工业出版社'),(6,'Windows',50.00,35.00,'机械工业出版社'),(7,'HTML5',90.00,105.00,'清华大学出版社'),(19,'Rstudio',56.00,21.00,'北京大学出版社'),(21,'java',60.00,56.00,'北京大学出版社');
/*!40000 ALTER TABLE `mybook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES (1,'wang','123'),(5,'yao','123'),(6,'wangweichao','123456'),(13,'xixi','123'),(14,'wan','123'),(15,'ang','123'),(16,'a','123');
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-17 16:58:34

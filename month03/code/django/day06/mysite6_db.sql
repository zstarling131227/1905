-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: mysite6_db
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add note',8,'add_note'),(23,'Can change note',8,'change_note'),(24,'Can delete note',8,'delete_note');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$FtOfYgZiKN9Y$YNqZzjNC+c2QN4b0/eLreDx4ltIPBG8K3MyjMzqs8NI=','2019-08-19 07:52:20.610684',1,'tedu','','','xxx@tedu.cn',1,1,'2019-08-19 07:51:24.298596');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-08-19 08:09:18.197848','1','Note object',1,'[{\"added\": {}}]',8,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'note','note'),(6,'sessions','session'),(7,'user','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-19 01:59:07.312099'),(2,'auth','0001_initial','2019-08-19 01:59:16.805377'),(3,'admin','0001_initial','2019-08-19 01:59:18.968687'),(4,'admin','0002_logentry_remove_auto_add','2019-08-19 01:59:19.093575'),(5,'contenttypes','0002_remove_content_type_name','2019-08-19 01:59:20.265527'),(6,'auth','0002_alter_permission_name_max_length','2019-08-19 01:59:21.168065'),(7,'auth','0003_alter_user_email_max_length','2019-08-19 01:59:21.957625'),(8,'auth','0004_alter_user_username_opts','2019-08-19 01:59:22.032850'),(9,'auth','0005_alter_user_last_login_null','2019-08-19 01:59:22.657510'),(10,'auth','0006_require_contenttypes_0002','2019-08-19 01:59:22.707462'),(11,'auth','0007_alter_validators_add_error_messages','2019-08-19 01:59:22.762685'),(12,'auth','0008_alter_user_username_max_length','2019-08-19 01:59:24.614639'),(13,'sessions','0001_initial','2019-08-19 01:59:25.258163'),(14,'user','0001_initial','2019-08-19 01:59:25.661144'),(15,'note','0001_initial','2019-08-19 07:45:14.963202');
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
INSERT INTO `django_session` VALUES ('0bqt1h6kh816ze8phq0fxk9amm6d0wwu','OGNiZjU4ZGUzNGNiZDMyNzA3ZjI4NGJjYmRlYjc3ZDhkMGZmNjgwZjp7InVzZXIiOnsidXNlcm5hbWUiOiJ3YW5nYmFkYW4iLCJpZCI6MX19','2019-09-03 08:19:00.388438');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `note_note`
--

DROP TABLE IF EXISTS `note_note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `note_note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `mod_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `note_note_user_id_14a49a72_fk_user_user_id` (`user_id`),
  CONSTRAINT `note_note_user_id_14a49a72_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `note_note`
--

LOCK TABLES `note_note` WRITE;
/*!40000 ALTER TABLE `note_note` DISABLE KEYS */;
INSERT INTO `note_note` VALUES (1,'HY','从你的全世界路过\r\n烂人','2019-08-19 08:09:18.195836','2019-08-20 03:05:59.793917',1),(4,'Rstudio','从你的全世界路过','2019-08-20 07:45:53.951010','2019-08-20 07:45:53.951043',1),(5,'bz','waiting for you','2019-08-20 08:19:30.013820','2019-08-20 08:19:30.013919',1),(6,'lanren','是谁的心啊，孤单的留下\r\n他还好吗。我多想爱他','2019-08-20 08:21:56.384477','2019-08-20 08:21:56.384507',1),(7,'xixi','我愿变成童话里你爱的那个天使\r\n张开双手，变成翅膀守护你','2019-08-20 08:24:32.755611','2019-08-20 08:24:32.755656',1),(8,'嘻嘻','怎敌他晚来风急','2019-08-20 08:25:57.959267','2019-08-20 08:25:57.959348',1),(9,'钥玥','你是人间四月天\r\n也无风雨也无晴','2019-08-20 08:27:34.332107','2019-08-20 08:27:34.332197',1),(10,'霰雪鸟','感受停在我发端的指尖\r\n如何瞬间冻结时间\r\n记住望着我坚定的双眼\r\n也许已经没有明天\r\n面对浩瀚的星海\r\n我们微小得像尘埃\r\n漂浮在一片无奈\r\n缘分让我们相遇乱世以外\r\n命运却要我们危难中相爱\r\n也许未来遥远在光年之外\r\n我愿守候未知里为你等待\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n一双围在我胸口的臂弯\r\n足够抵挡天旋地转\r\n一种执迷不放手的倔强\r\n足以点燃所有希望\r\n宇宙磅礴而冷漠\r\n我们的爱微小却闪烁\r\n颠簸却如此忘我\r\n\r\n缘分让我们相遇乱世以外\r\n命运却要我们危难中相爱\r\n也许未来遥远在光年之外\r\n我愿守候未知里为你等待\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n也许航道以外是醒不来的梦\r\n乱世以外是纯粹的相拥\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n相遇乱世以外危难中相爱\r\n相遇乱世以外危难中相爱\r\n我没想到','2019-08-20 08:35:49.810738','2019-08-20 08:35:49.810769',1),(11,'霰雪鸟','感受停在我发端的指尖\r\n如何瞬间冻结时间\r\n记住望着我坚定的双眼\r\n也许已经没有明天\r\n面对浩瀚的星海\r\n我们微小得像尘埃\r\n漂浮在一片无奈\r\n缘分让我们相遇乱世以外\r\n命运却要我们危难中相爱\r\n也许未来遥远在光年之外\r\n我愿守候未知里为你等待\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n一双围在我胸口的臂弯\r\n足够抵挡天旋地转\r\n一种执迷不放手的倔强\r\n足以点燃所有希望\r\n宇宙磅礴而冷漠\r\n我们的爱微小却闪烁\r\n颠簸却如此忘我\r\n\r\n缘分让我们相遇乱世以外\r\n命运却要我们危难中相爱\r\n也许未来遥远在光年之外\r\n我愿守候未知里为你等待\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n也许航道以外是醒不来的梦\r\n乱世以外是纯粹的相拥\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n相遇乱世以外危难中相爱\r\n相遇乱世以外危难中相爱\r\n我没想到','2019-08-20 08:36:17.597679','2019-08-20 08:36:17.597752',1),(12,'霰雪鸟','感受停在我发端的指尖\r\n如何瞬间冻结时间\r\n记住望着我坚定的双眼\r\n也许已经没有明天\r\n面对浩瀚的星海\r\n我们微小得像尘埃\r\n漂浮在一片无奈\r\n缘分让我们相遇乱世以外\r\n命运却要我们危难中相爱\r\n也许未来遥远在光年之外\r\n我愿守候未知里为你等待\r\n我没想到为了你我能疯狂到\r\n山崩海啸没有你根本不想逃\r\n我的大脑为了你已经疯狂到\r\n脉搏心跳没有你根本不重要\r\n一双围在我胸口的臂弯\r\n足够抵挡天旋地转\r\n一种执迷不放手的倔强\r\n足以点燃所有希望\r\n宇宙磅礴而冷漠\r\n我们的爱微小却闪烁\r\n颠簸却如此忘我','2019-08-20 08:39:58.341053','2019-08-20 08:39:58.341083',1),(13,'王八蛋','忘了有多久\r\n再没听到你\r\n对我说你 最爱的故事\r\n我想了很久\r\n我开始慌了\r\n是不是我又做错了什么\r\n你哭着对我说\r\n童话里都是骗人的\r\n我不可能 是你的王子\r\n也许你不会懂\r\n从你说爱我以后\r\n我的天空 星星都亮了\r\n我愿变成童话里\r\n你爱的那个天使\r\n张开双手\r\n变成翅膀守护你\r\n你要相信\r\n相信我们会像童话故事里\r\n幸福和快乐是结局\r\n你哭着对我说\r\n童话里都是骗人的\r\n我不可能 是你的王子\r\n也许你不会懂\r\n从你说爱我以后\r\n我的天空 星星都亮了\r\n我愿变成童话里\r\n你爱的那个天使\r\n张开双手\r\n变成翅膀守护你\r\n你要相信\r\n相信我们会像童话故事里\r\n幸福和快乐是结局\r\n我要变成童话里\r\n你爱的那个天使\r\n张开双手\r\n变成翅膀守护你\r\n你要相信\r\n相信我们会像童话故事里\r\n幸福和快乐是结局\r\n我会变成童话里\r\n你爱的那个天使\r\n张开双手\r\n变成翅膀守护你\r\n你要相信\r\n相信我们会像童话故事里\r\n幸福和快乐是结局\r\n一起写 我们的结局','2019-08-20 08:47:58.405841','2019-08-20 08:47:58.405873',1),(14,'王八蛋','翻开随身携带的记事本\r\n写着许多事都是关於你\r\n你讨厌被冷落\r\n习惯被守候\r\n寂寞才找我\r\n我看见自己写下的心情\r\n把自己放在卑微的后头\r\n等你等太久\r\n想你泪会流\r\n而幸福快乐是什么\r\n爱的痛了\r\n痛的哭了\r\n哭的累了\r\n日记本里页页执着\r\n记载着你的好\r\n像上瘾的毒药\r\n它反复骗着我\r\n爱的痛了\r\n痛的哭了\r\n哭的累了\r\n矛盾心里总是强求\r\n劝自己要放手\r\n闭上眼让你走\r\n烧掉日记重新来过\r\n我看见自己写下的心情\r\n把自己放在卑微的后头\r\n等你等太久\r\n想你泪会流\r\n而幸福快乐是什么\r\n爱的痛了\r\n陈慧琳\r\n陈慧琳\r\n痛的哭了\r\n哭的累了\r\n日记本里页页执着\r\n记载着你的好\r\n像上瘾的毒药\r\n它反覆骗着我\r\n爱的痛了\r\n痛的哭了\r\n哭的累了\r\n矛盾心里总是强求\r\n劝自己要放手\r\n闭上眼让你走\r\n烧掉日记重新来过\r\n爱的痛了\r\n痛的哭了\r\n哭的累了\r\n矛盾心里总是强求\r\n劝自己要放手\r\n闭上眼让你走\r\n烧掉日记重新来过','2019-08-20 09:33:38.360600','2019-08-20 09:33:38.360668',1);
/*!40000 ALTER TABLE `note_note` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES (1,'wangbadan','123'),(4,'wangba','123'),(6,'tarena','123');
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

-- Dump completed on 2019-08-21 10:05:40

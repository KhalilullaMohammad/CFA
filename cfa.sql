-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: cfa
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `name` varchar(30) DEFAULT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(70) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `mobile` varchar(10) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('GopiChand','gopi','gopichandvallabhaneni5@gmail.com','gopi','6305537768');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaign`
--

DROP TABLE IF EXISTS `campaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaign` (
  `cid` varchar(10) NOT NULL,
  `name` tinytext,
  `username` varchar(30) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `fund_required` int DEFAULT NULL,
  `funds_collected` int DEFAULT '0',
  `dname` varchar(15) DEFAULT NULL,
  `dfile` longblob,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(20) DEFAULT 'Not Approved',
  PRIMARY KEY (`cid`),
  KEY `username` (`username`),
  CONSTRAINT `campaign_ibfk_1` FOREIGN KEY (`username`) REFERENCES `register` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign`
--

LOCK TABLES `campaign` WRITE;
/*!40000 ALTER TABLE `campaign` DISABLE KEYS */;
INSERT INTO `campaign` VALUES ('N2hY7iT4f','Lost all the money in surgery need ur help','eswar','Please help us',10000,0,'datta-task1.txt',_binary 'import subprocess as sp\r\nimport re\r\n\r\naccuracy = 1\r\nwhile True:\r\n    pshellcomm = [\'powershell\']\r\n    pshellcomm.append(\'add-type -assemblyname system.device; \'\\\r\n                      \'$loc = new-object system.device.location.geocoordinatewatcher;\'\\\r\n                      \'$loc.start(); \'\\\r\n                      \'while(($loc.status -ne \"Ready\") -and ($loc.permission -ne \"Denied\")) \'\\\r\n                      \'{start-sleep -milliseconds 100}; \'\\\r\n                      \'$acc = %d; \'\\\r\n                      \'while($loc.position.location.horizontalaccuracy -gt $acc) \'\\\r\n                      \'{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; \'\\\r\n                      \'$loc.position.location.latitude; \'\\\r\n                      \'$loc.position.location.longitude; \'\\\r\n                      \'$loc.position.location.horizontalaccuracy; \'\\\r\n                      \'$loc.stop()\' %(accuracy))\r\n\r\n\r\n\r\n    p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)\r\n    (out, err) = p.communicate()\r\n    out = re.split(\'\\n\', out)\r\n    lat = str(float(out[0]))\r\n    long = str(float(out[1]))\r\n    veer=lat+\',\'+long\r\n    print(str(veer))\r\n    break\r\nimport gmap as g\r\nfrom geopy.geocoders import Nominatim\r\ngeoLoc = Nominatim(user_agent=\"GetLoc\")\r\n\r\nlocname = geoLoc.reverse(g.veer)\r\nv=locname.address\r\nprint(v)\r\nd=[]\r\nfor i in v:\r\n    \"\".join(i)\r\nd=v\r\nn=d.split(\',\')\r\nc=n[0]\r\n\r\n\r\nfrom bs4 import BeautifulSoup\r\nimport requests\r\nimport main as m\r\nheaders = {\r\n	\'User-Agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\'}\r\n\r\n\r\ndef weather(city):\r\n	city = city.replace(\" \", \"+\")\r\n	res = requests.get(\r\n		f\'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8\', headers=headers)\r\n\r\n	soup = BeautifulSoup(res.text, \'html.parser\')\r\n	location = soup.select(\'#wob_loc\')[0].getText().strip()\r\n	weather = soup.select(\'#wob_tm\')[0].getText().strip()\r\n	print(location)\r\n	print(weather+\"°C\")\r\n\r\n\r\ncity =m.c\r\ncity = city+\" weather\"\r\nweather(city)\r\n\r\n\r\n','2023-05-01 11:46:50','Approved'),('O7qX4bE0l','Suffering from brain tumor','eswar','Please Help us',50000,0,'Aws.txt.txt',_binary 'ec2(vartual servers)\r\nAMI is os+ some predefined applictions\r\nIn bound & ourbound rules allow\r\n(windows)mobaxterm RDP client,port 3389\r\n(linux) ssh client,port 22\r\nssh -i linux keypair(pem,ppk) ip of server\r\nmobaxterm,mobilehosts uses pem key \r\ntool putty use ppk key \r\n\r\n\r\n\r\n\r\nWebCommerce:---https://github.com/eisnerh/WebCommerce.git\r\nkinsmanlibrary:---https://github.com/spereverde/kinsmanlibrary.git\r\nDjango-WebApp:---https://github.com/smahesh29/Django-WebApp.git\r\nHot-Food:----https://github.com/shyam999/Hot-Food.git\r\nCRM Project(Contact Management Project):--https://github.com/studygyaan/Django-CRM-Project.git\r\n\r\n\r\n\r\n\r\naws login:\r\nuser--datta@codegnan.com\r\npsw:--Vdatta2521\r\n\r\naws rds cridentials:--\r\nlocalhost:--spm.ctbgpu7gycn4.ap-northeast-1.rds.amazonaws.com\r\nuser--admin\r\npsw--Datta2521\r\n\r\n\r\n\r\n\r\njinja2 template engine:--\r\n{%....%}---used for conditional,for loop statements\r\n{{    }}---for experssions to print output\r\n{{\'#\'}}----this for comments\r\n','2023-05-01 11:35:21','Approved');
/*!40000 ALTER TABLE `campaign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `name` varchar(30) DEFAULT NULL,
  `email` varchar(70) NOT NULL,
  `subject` varchar(25) DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `name` varchar(30) DEFAULT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(70) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `mobile` varchar(10) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('eswar nandivada','eswar','eswar@codegnan.com','2001','9177806313');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01 15:04:28

/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2018-07-10 16:58:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) DEFAULT NULL,
  `password` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '1', '1');
INSERT INTO `user` VALUES ('2', '2', '2');
INSERT INTO `user` VALUES ('4', '4', '4');
INSERT INTO `user` VALUES ('5', '5', '5');
INSERT INTO `user` VALUES ('6', '6', '6');
INSERT INTO `user` VALUES ('7', '7', '7');
INSERT INTO `user` VALUES ('8', '8', '8');
INSERT INTO `user` VALUES ('9', '9', '9');
INSERT INTO `user` VALUES ('10', '0', '0');

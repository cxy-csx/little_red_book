
CREATE TABLE `lrb_board` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `user_id`  varchar(40) NOT NULL DEFAULT '0' COMMENT '用户id',
  `board_id` varchar(40) NOT NULL DEFAULT '0' COMMENT '专辑id',
  `name` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '专辑名称',
  `note` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '笔记数',
  `follower` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '粉丝数',
  `spider_time` char(19) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '爬取时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `user_id` (`user_id`) USING BTREE,
  UNIQUE KEY `board_id` (`board_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='小红书专辑表';



INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (5, '5e3bd70700000000010026b7', '5ea80e0700000000010093eb', '我的自律励志生活分享', 105, 30, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (6, '5e3bd70700000000010026b7', '5ea80d860000000001001855', '伪学霸的爱情故事分享', 7, 10, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (7, '5e3bd70700000000010026b7', '5ea80bdd0000000001007ab2', '学习方法分享', 39, 70, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (8, '5e3bd70700000000010026b7', '5f9e14c1000000000100343f', '加分技能get', 6, 6, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (9, '5e3bd70700000000010026b7', '5ea80b30000000000100791a', '司法考试备考经验分享', 15, 64, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (10, '5e3bd70700000000010026b7', '5f30300c000000000101df1c', '成绩认证', 2, 4, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (11, '5e3bd70700000000010026b7', '5ea80d2f0000000001007dd2', '高考相关，高考加油！', 10, 12, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (12, '5e3bd70700000000010026b7', '5ea80dce0000000001007f20', '公务员考试经验分享', 7, 46, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (13, '5e3bd70700000000010026b7', '5e3beffe00000000010012a5', '个人专辑', 63, 9, '2021-02-01 18:24:38');
INSERT INTO `lrb_board`(`id`, `user_id`, `board_id`, `name`, `note`, `follower`, `spider_time`) VALUES (14, '5e3bd70700000000010026b7', '5f9a2b240000000001008ced', '时间管理', 1, 8, '2021-02-01 18:24:38');





CREATE TABLE `lrb_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `user_id` varchar(40) NOT NULL DEFAULT '0' COMMENT '用户id',
  `nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户昵称',
  `avatar` varchar(250)  NOT NULL DEFAULT '' COMMENT '用户头像',
  `brief` varchar(300)  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '个人介绍',
  `location` varchar(30)  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '位置描述',
  `following` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '关注',
  `follower` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '粉丝',
  `starer` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '获赞与收藏',
  `spider_time` char(19) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '爬取时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='小红书用户表';


INSERT INTO `lrb_user`(`id`, `user_id`, `nickname`, `avatar`, `brief`, `location`, `following`, `follower`, `starer`, `spider_time`) VALUES (4, '5c14bae100000000070124ab', '上杉大荔枝', 'https://img.xiaohongshu.com/avatar/600f0f1940a7480001cc2bd8.jpg@240w_240h_90q_1e_1c_1x.jpg', 'baseball,\nconsole game,\nmusical&classical&rock,\nlego,\nprogrammer.', '地球的某一片红薯地', 25, 11, 345, '2021-01-26 16:26:26');
INSERT INTO `lrb_user`(`id`, `user_id`, `nickname`, `avatar`, `brief`, `location`, `following`, `follower`, `starer`, `spider_time`) VALUES (5, '5c9f38070000000017023e64', '元气少女羊', 'https://img.xiaohongshu.com/avatar/5efaad75e2a1ef00010d8600.jpg@240w_240h_90q_1e_1c_1x.jpg', '👧可爱的日常分享✨\n🐑书桌|美食|生活好物\n📬50833379@qq.com', '中国', 119, 16000, 114000, '2021-01-26 16:26:34');
INSERT INTO `lrb_user`(`id`, `user_id`, `nickname`, `avatar`, `brief`, `location`, `following`, `follower`, `starer`, `spider_time`) VALUES (6, '5c274816000000000502173f', '我的发卡nie🎡', 'https://img.xiaohongshu.com/avatar/5cc98809c0d8360001e5ea33.jpg@240w_240h_90q_1e_1c_1x.jpg', '一个懒懒的_____', '地球的某一片红薯地', 1, 8, 117, '2021-01-26 16:26:40');
INSERT INTO `lrb_user`(`id`, `user_id`, `nickname`, `avatar`, `brief`, `location`, `following`, `follower`, `starer`, `spider_time`) VALUES (7, '56f72db084edcd7a854bf04d', '硅谷普通人', 'https://img.xiaohongshu.com/avatar/5ff01b255968edfe10d95226.jpg@240w_240h_90q_1e_1c_1x.jpg', '感受当下。', '美国', 39, 75, 648, '2021-01-26 16:26:47');
INSERT INTO `lrb_user`(`id`, `user_id`, `nickname`, `avatar`, `brief`, `location`, `following`, `follower`, `starer`, `spider_time`) VALUES (8, '5a57953211be105e0641de82', 'emma', 'https://img.xiaohongshu.com/avatar/5f4c7556a4cd6e0001204d59.jpg@240w_240h_90q_1e_1c_1x.jpg', '暂时还没有个性签名哦～', '美国纽约市', 41, 10, 84, '2021-01-26 16:26:54');






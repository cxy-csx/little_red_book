
CREATE TABLE `lrb_tags`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `tag_id` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '0' COMMENT '标签id',
  `tag_name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '标签名字',
  `tag_url` varchar(400) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '标签链接',
  `refer` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'index' COMMENT '推荐关键字',
  `spider_time` char(19) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '爬取时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tag_name`(`tag_name`) USING BTREE,
  UNIQUE INDEX `tag_id`(`tag_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '小红书标签表' ROW_FORMAT = Dynamic;


INSERT INTO `lrb_tags` VALUES (45, '2305849101392979230', '蓝牙耳机', 'https://www.xiaohongshu.com/mobile/tags/2305849101392979230?name=%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (46, '2368271611397986055', '充电', 'https://www.xiaohongshu.com/mobile/tags/2368271611397986055?name=%E5%85%85%E7%94%B5', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (47, '2305852470357839336', '降噪', 'https://www.xiaohongshu.com/mobile/tags/2305852470357839336?name=%E9%99%8D%E5%99%AA', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (48, '2305844686374780608', '耳机', 'https://www.xiaohongshu.com/mobile/tags/2305844686374780608?name=%E8%80%B3%E6%9C%BA', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (49, '2305844674941299064', '穿搭', 'https://www.xiaohongshu.com/mobile/tags/2305844674941299064?name=%E7%A9%BF%E6%90%AD', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (50, '2305845532184500126', '潮流', 'https://www.xiaohongshu.com/mobile/tags/2305845532184500126?name=%E6%BD%AE%E6%B5%81', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (51, '2305845963427643683', '钢琴', 'https://www.xiaohongshu.com/mobile/tags/2305845963427643683?name=%E9%92%A2%E7%90%B4', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (52, '2368271611431633670', '质地', 'https://www.xiaohongshu.com/mobile/tags/2368271611431633670?name=%E8%B4%A8%E5%9C%B0', 'index', '2021-01-21 11:14:41');
INSERT INTO `lrb_tags` VALUES (53, '2305860643879073691', '大油田', 'https://www.xiaohongshu.com/mobile/tags/2305860643879073691?name=%E5%A4%A7%E6%B2%B9%E7%94%B0', '花西子', '2021-01-21 11:14:44');
INSERT INTO `lrb_tags` VALUES (54, '2162506652309902743', '花西子', 'https://www.xiaohongshu.com/mobile/tags/2162506652309902743?name=%E8%8A%B1%E8%A5%BF%E5%AD%90', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (55, '2368271611397986057', '粉质', 'https://www.xiaohongshu.com/mobile/tags/2368271611397986057?name=%E7%B2%89%E8%B4%A8', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (56, '2305844686878660436', '粉饼', 'https://www.xiaohongshu.com/mobile/tags/2305844686878660436?name=%E7%B2%89%E9%A5%BC', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (57, '2305846523014878291', '定妆粉', 'https://www.xiaohongshu.com/mobile/tags/2305846523014878291?name=%E5%AE%9A%E5%A6%86%E7%B2%89', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (58, '2305844666595205683', '眼影', 'https://www.xiaohongshu.com/mobile/tags/2305844666595205683?name=%E7%9C%BC%E5%BD%B1', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (59, '2305987797834325763', '服帖', 'https://www.xiaohongshu.com/mobile/tags/2305987797834325763?name=%E6%9C%8D%E5%B8%96', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (60, '2305844616056258181', '口红', 'https://www.xiaohongshu.com/mobile/tags/2305844616056258181?name=%E5%8F%A3%E7%BA%A2', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (61, '2305845585089975934', '妆容', 'https://www.xiaohongshu.com/mobile/tags/2305845585089975934?name=%E5%A6%86%E5%AE%B9', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (62, '2305845729099786369', '试色', 'https://www.xiaohongshu.com/mobile/tags/2305845729099786369?name=%E8%AF%95%E8%89%B2', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (63, '2305846820096325531', '素颜', 'https://www.xiaohongshu.com/mobile/tags/2305846820096325531?name=%E7%B4%A0%E9%A2%9C', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (64, '2305857138038502903', '无滤镜', 'https://www.xiaohongshu.com/mobile/tags/2305857138038502903?name=%E6%97%A0%E6%BB%A4%E9%95%9C', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (65, '2305844676131045514', '眉笔', 'https://www.xiaohongshu.com/mobile/tags/2305844676131045514?name=%E7%9C%89%E7%AC%94', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (66, '2305915447680576114', '豆沙', 'https://www.xiaohongshu.com/mobile/tags/2305915447680576114?name=%E8%B1%86%E6%B2%99', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (67, '2296570660471980302', '花西子宠粉进行时', 'https://www.xiaohongshu.com/mobile/tags/2296570660471980302?name=%E8%8A%B1%E8%A5%BF%E5%AD%90%E5%AE%A0%E7%B2%89%E8%BF%9B%E8%A1%8C%E6%97%B6', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (68, '2305849002744874699', '哑光', 'https://www.xiaohongshu.com/mobile/tags/2305849002744874699?name=%E5%93%91%E5%85%89', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (69, '2305846409748738853', '显白', 'https://www.xiaohongshu.com/mobile/tags/2305846409748738853?name=%E6%98%BE%E7%99%BD', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (70, '2305845118064315314', '艺术品', 'https://www.xiaohongshu.com/mobile/tags/2305845118064315314?name=%E8%89%BA%E6%9C%AF%E5%93%81', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (71, '2305845949175391466', '雕花', 'https://www.xiaohongshu.com/mobile/tags/2305845949175391466?name=%E9%9B%95%E8%8A%B1', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (72, '2305844846970388106', '婚纱照', 'https://www.xiaohongshu.com/mobile/tags/2305844846970388106?name=%E5%A9%9A%E7%BA%B1%E7%85%A7', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (73, '2305844656214359547', '写真', 'https://www.xiaohongshu.com/mobile/tags/2305844656214359547?name=%E5%86%99%E7%9C%9F', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (74, '2305844628981400069', '礼物', 'https://www.xiaohongshu.com/mobile/tags/2305844628981400069?name=%E7%A4%BC%E7%89%A9', '花西子', '2021-01-21 11:14:45');
INSERT INTO `lrb_tags` VALUES (76, '2305845158794744781', '烘焙', 'https://www.xiaohongshu.com/mobile/tags/2305845158794744781?name=%E7%83%98%E7%84%99', 'index', '2021-01-21 14:38:34');
INSERT INTO `lrb_tags` VALUES (77, '2305844797853579208', '蛋糕', 'https://www.xiaohongshu.com/mobile/tags/2305844797853579208?name=%E8%9B%8B%E7%B3%95', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (78, '2306109311972487129', '模具', 'https://www.xiaohongshu.com/mobile/tags/2306109311972487129?name=%E6%A8%A1%E5%85%B7', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (79, '2305844654098985987', '甜品', 'https://www.xiaohongshu.com/mobile/tags/2305844654098985987?name=%E7%94%9C%E5%93%81', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (80, '1513878978231684070', '深圳', 'https://www.xiaohongshu.com/mobile/tags/1513878978231684070?name=%E6%B7%B1%E5%9C%B3', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (81, '2224079363857974341', '甜蜜时光甜品蛋糕培训', 'https://www.xiaohongshu.com/mobile/tags/2224079363857974341?name=%E7%94%9C%E8%9C%9C%E6%97%B6%E5%85%89%E7%94%9C%E5%93%81%E8%9B%8B%E7%B3%95%E5%9F%B9%E8%AE%AD', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (82, '2305844617192194603', '美食', 'https://www.xiaohongshu.com/mobile/tags/2305844617192194603?name=%E7%BE%8E%E9%A3%9F', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (83, '2305854624715812837', '新年礼物', 'https://www.xiaohongshu.com/mobile/tags/2305854624715812837?name=%E6%96%B0%E5%B9%B4%E7%A4%BC%E7%89%A9', 'index', '2021-01-21 14:38:35');
INSERT INTO `lrb_tags` VALUES (84, '2234874841713734862', '蛋糕培训', 'https://www.xiaohongshu.com/mobile/tags/2234874841713734862?name=%E8%9B%8B%E7%B3%95%E5%9F%B9%E8%AE%AD', 'index', '2021-01-21 14:38:35');






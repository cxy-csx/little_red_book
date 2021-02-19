# little_red_book
 小红书爬虫简单版

- 文件说明
    - example_html  存放小红书官网示例html代码的文件夹
    - sql           存放表结构和示例数据的文件夹
    - test          存放开发阶段测试文件的文件夹
    - call_windows.py  远程调用windows文件（暂无用）
    - common.py     公用/配置文件
    - get_note.py   获取笔记内容
    - get_user.py   主入口文件
    - get_user_fire.py   主入口文件（火狐版）
    - lrb_note.py   model文件lrb_note表
    - lrb_tags.py   model文件lrb_tags表
    - lrb_user.py   model文件lrb_user表
    - requirements.txt   环境依赖的扩展包
 
- 用法 
    - 进入common.py修改数据库参数，第19-22行，MYSQL_HOST，MYSQL_USER，MYSQL_PWD，MYSQL_DB四个值
    
    - 在数据库环境中导入sql文件夹中的.sql文件，导入后各表有少量测试数据，你可以自行清空
    
    - 安装requirements.txt中的扩展包，环境是python3
  
    - 配置好系统中的selenium + webdriver,优先推荐使用chrome，实在没有情况下可用firefox
  
    - 在命令行中cd到当前文件目录，执行 python3 get_user.py -u 5e3bd70700000000010026b7（chrome版），或者 python3 get_user_fire.py -u 5e3bd70700000000010026b7（firefox版）
  
    - 其中5e3bd70700000000010026b7是网页版用户主页的用户标记，例如 https://www.xiaohongshu.com/user/profile/562ef75ae00dd861d410784a，
    https://www.xiaohongshu.com/user/profile/5dc0e8c90000000001004610， 运行后将会爬取该用户的基本信息，相关笔记和相关专辑，请耐心等待，一般执行一个用户需要3-5分钟。

    
- 疑问参考
    - 本爬虫参考了如下连接，如有疑问请查看翻阅
    - https://blog.csdn.net/weixin_42185136/article/details/90764908
    - https://blog.csdn.net/blueheart20/article/details/81566903
    - https://www.jianshu.com/p/dd848e40c7ad
    - https://www.cnblogs.com/573734817pc/p/11177010.html
    - https://cuiqingcai.com/1319.html
    - https://www.cnblogs.com/zhangxinqi/p/9210211.html
 
- 特别说明
    - 本仓库仅用于技术开源，供爬虫爱好者研究。切勿使用本仓库用于非法商业行为，否则请自行承担责任，本人在此申明不承担任何由此生成的法律责任。


 
 
insert into booktest_bookinfo(book_name,book_pub_date,book_read,book_comment,isDelete)values
	('射雕英雄传','1980-5-1',12,40,0);
	('天龙八部','1986-7-24',36,40,0),
	('笑傲江湖','1985-12-24',37,50,0),
	('雪山飞狐','1987-11-11',56,85,0);

	insert into booktest_heroinfo(hero_name,hero_gender,hero_book_id,hero_comment,isDelete)values
	('黄蓉',0,25,'打狗棒法',0),
	('黄药师',1,25,'弹指神通',0),
	('欧阳峰',1,25,'蛤蟆功',0),
	('梅超风',0,25,'九阴白骨爪',0);
	('乔峰',1,2,'降龙十八掌',0),
	('段誉',1,2,'六脉神剑',0),
	('虚竹',1,2,'天山六阳掌',0),
	('王语嫣',0,2,'神仙姐姐',0),
	('令狐冲',1,3,'独孤九剑',0),
	('任盈盈',0,3,'弹琴',0),
	('岳不群',1,3,'华山剑法',0),
	('东方不败',0,3,'葵花宝典',0),
	('胡斐',1,4,'胡家刀法',0),
	('苗若兰',0,4,'黄衣',0),
	('程灵素',0,4,'医术',0),
	('袁紫衣',0,4,'六合拳',0);

create table django_session(
session_id int(11) PRIMARY KEY not null AUTO_INCREMENT,
session_data varchar(20),
expires_date int(50));

alter table django_session change session_id session_key varchar(50);
alter table django_session change expires_date expire_date varchar(50);
alter table django_session modify session_data varchar(20);
	

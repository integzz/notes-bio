# 快速入门 - SQL 数据库

## 1. 数据库简介

### 1.1. E-R 模型

一个数据库就是一个完整的业务单元，可包含多张表，数据被存储在表中。当前物理的数据库均是按照 E-R 模型（entry-relationship model）进行设计的

1. 一个实体（entry）变换为数据库中的一个表，相当于一个对象
2. 关系用于描述实体间的对应规则，包括一对一、一对多、多对多
3. 关系会变换为数据库表中的一个列
4. 关系型数据库中一行就是一个对象
5. 数据往往会存储在服务器

### 1.2. 三范式

经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式（normal form，NF）:

1. 第一范式（1NF）: 列不可拆分，即关系不可拆分
2. 第二范式（2NF）: 唯一标识，可通过一个属性找到其对应的唯一对象
3. 第三范式（3NF）: 引用主键，主键即标识；

> 说明: 后一个范式均是在前一个范式的基础上建立的

### 1.3. SQL 语言规范

SQL 语言对大小写不敏感：一般情况下，关键字大写，其他小写

## 2. 事务

将多个操作被当作一个整体对待。

### 2.1. 性质（ACID）

1. 原子性（Atomicity）：整个事务中的所有操作，要么全部完成，要么全部不完成，不可能停滞在中间某个环节。事务在执行过程中发生错误，会被回滚到事务开始前的状态，就像这个事务从来没有执行过一样
2. 一致性（Consistency）：在事务开始之前和事务结束以后，数据库的完整性约束没有被破坏。
3. 隔离性（Isolation）：隔离状态执行事务，使它们好像是系统在给定时间内执行的唯一操作。这种属性有时称为串行化，为了防止事务操作间的混淆，必须串行化或序列化请求，使得在同一时间仅有一个请求用于同一数据。
4. 持久性（Durability）：事务完成后，该事务所对数据库所作的更改便持久的保存在数据库之中，并不会被回滚。

### 2.2. 功能

1. 当一个业务逻辑需要多个 sql 完成时，若其中某条 sql 语句出错，则希望整个操作都退回
2. 使用事务可完成退回的功能，保证业务逻辑的正确性
3. 表的类型必须是 innodb 或 bdb 类型，才可对此表使用事务
4. 主要用于对表进行修改前后的控制

## 3. 用户管理

### 3.1. 用户设置

```sql
-- 创建用户
create user '用户名'@'IP 地址' identified by '密码';
-- 删除用户
drop user '用户名'@'IP 地址';
-- 修改用户
rename user '用户名'@'IP 地址'; to '新用户名'@'IP 地址';
-- 修改密码
set password for '用户名'@'IP 地址'=password('新密码')
```

### 3.2. 用户权限设置

```sql
-- 查看权限
show grants for '用户'@'IP 地址'
-- 授权
grant 权限 on 数据库. 表 to '用户'@'IP 地址'
-- 取消权限
revoke 权限 on 数据库. 表 from '用户'@'IP 地址'

-- 备注
-- 数据库中的所有
数据库名.*
-- 指定数据库中的某张表
数据库名. 表
-- 指定数据库中的存储过程
数据库名. 存储过程
-- 所有数据库
*.*
-- 用户只能在改 IP 下才能访问
用户名@IP 地址
-- 用户只能在改 IP 段下才能访问 (通配符%表示任意)
用户名@192.168.1.%
-- 用户可再任意 IP 下访问 (默认 IP 地址为%)
用户名@%
```

## 4. 数据与键

### 4.1. 数据操作

| 对象   |                     定义                     |                 备注                 |
| ------ | :------------------------------------------: | :----------------------------------: |
| 数据库 |               一些关联表的集合               |
| 数据表 |                  数据的矩阵                  |
| 列     |                相同类型的数据                |
| 行     |                一组相关的数据                |
| 冗余   |                 存储两倍数据                 | 冗余降低了性能，但提高了数据的安全性 |
| 值     | 行的具体信息，每个值必须与该列的数据类型相同 |
| 索引   | 对数据库表中一列或多列的值进行排序的一种结构 |           类似于书籍的目录           |

### 4.2. 键

| 对象   |              定义              |          备注          |
| ------ | :----------------------------: | :--------------------: |
| 键     |   键的值在当前列中具有唯一性   |                        |
| 超键   | 在关系中能唯一标识元组的属性集 |                        |
| 候选键 |      不含有多余属性的超键      |                        |
| 主键   |   用于惟一确定一个记录的字段   | 一个表中只能含一个主键 |
| 外键   |         用于关联两个表         |                        |
| 复合键 |     将多个列作为一个索引键     |    一般用于复合索引    |

> 参照完整性要求关系中不允许引用不存在的实体，与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。

## 5. 一级命令

### 5.1. 库和表的创建

1. 库和表：创建（CREATE）、删除（DROP）
2. 库：打开（USE）、备份、回复

- 表一旦建好，就尽量不要改变其结构
- 对重要数据，可设置一个 isDelete 的列，类型为 bit，表示逻辑删除

### 5.2. 表的结构设计

1. 字段性质：名称、类型、长度
2. 字段约束（ALTER...ADD|DROP|CHANGE）

- PRIMARY KEY|FOREIGN KEY
- NOT NULL, UNIQUE, DEFAULT
- AUTO CREMENT：字段的值由 MySQL 系统负责维护

> 主键的名称一般为 id，设置为 int 型，无符号数，自动增长，非空

### 5.3. 表的数据操作

1. 添加：INSERT INTO
2. 删除：DELETE FROM...WHERE
3. 修改：UPDATE...WHERE
4. 查询：SELECT ...FROM...WHERE
5. 备份：SELECT INTO...(IN...) FROM

## 6. 表的创建

```sql
-- 多级表创建
CREATE TABLE multi_tbl(
  food_id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  food_name VARCHAR(20) NOT NULL
  parent_id SMALLINT UNSIGNED NOT NULL DEFAULT 0
);
INSERT multi_tbl(main_name, parent_id) VALUES('FOOD', DEFAULT);
INSERT multi_tbl(main_name, parent_id) VALUES('FRIUT', 1);
INSERT multi_tbl(main_name, parent_id) VALUES('APPLE', 2);
INSERT multi_tbl(main_name, parent_id) VALUES('ORANGE', 2);
INSERT multi_tbl(main_name, parent_id) VALUES('GREEN APPLE', 3);
```

## 7. 常用字段

### 7.1. AS

```sql
SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
INNER JOIN economies AS e
ON c.code = e.code;
```

### 7.2. DISTINCT

```sql
-- 一般情况下，仅使用 DISTINCT 处理单个字段，否则容易引起歧义
-- 多字段不重复查询，使用 GROUP BY
SELECT COUNT(DISTINCT s_id) FROM student;
-- The continents WHERE all countries have a population <= 25000000
SELECT DISTINCT continent FROM world x
  WHERE 25000000>=ALL
  (SELECT population FROM world y
    WHERE x.continent=y.continent AND population>0)
-- the name of all players who scored a goal against Germany
SELECT DISTINCT player
  FROM goal JOIN game
  ON game.id = goal.matchid AND goal.teamid!='GER' AND (game.team1='GER' OR game.team2='GER')
```

### 7.3. LIKE

```sql
-- ale 开头的所有（多个字符串）
SELECT * FROM 表 WHERE s_name LIKE 'ale%'
-- ale 开头的所有（一个字符）
SELECT * FROM 表 WHERE s_name LIKE 'ale_'
-- 以 "A" 或 "L" 或 "N" 开头
SELECT * FROM Persons
WHERE City LIKE '[ALN]%'
-- 不以 "A" 或 "L" 或 "N" 开头
SELECT * FROM Persons
WHERE City LIKE '[!ALN]%'
SELECT * FROM nobel
WHERE winner LIKE 'EUGENE O''NEILL'
```

## 8. 范围

### 8.1. IN & BETWEEN

```sql
--- <>相当于 NOT IS
-- Name AND the population for Scandinavia.
SELECT name, population FROM world
  WHERE name IN ('Sweden', 'Norway', 'Denmark');
-- All details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.
SELECT yr, subject, winner FROM nobel
  WHERE yr BETWEEN 1980 AND 1989 AND subject='literature'
```

### 8.2. ALL

```sql
-- Countries have a GDP greater than every country in Europe
-- (Some countries may have NULL gdp values)
-- ALL 不能加=，否则将加上欧洲 GDP 最大值
SELECT name FROM world
  WHERE gdp > ALL
  (SELECT gdp FROM world
    WHERE continent='Europe' AND gdp>0)
-- The largest country (by area) in each continent
-- 自比较需要限定其范围
SELECT continent, name, area FROM world x
  WHERE area >= ALL
  (SELECT area FROM world y
    WHERE y.continent=x.continent AND population>0)
-- The countries have populations more than three times that of any of their neighbours (in the same continent)
SELECT name, continent FROM world x
  WHERE x.population/3 >= ALL
    (SELECT population FROM world y
      WHERE x.continent=y.continent AND x.name!=y.name AND y.population>0)
```

## 9. 分组

### 9.1. GROUP...BY & ORDER...BY

GROUP BY 必须在 WHERE 之后，ORDER BY 之前；ORDER...BY 直接使用字段，不加假名

```sql
-- 聚合查询：GROUP BY 非聚合数据 HAVING 聚合条件
SELECT num, nid FROM 表 WHERE nid > 10 GROUP BY num, nid ORDER BY nid DESC
-- 包含查询：GROUP BY ... HAVING
SELECT num FROM 表 GROUP BY num HAVING max(id) > 10
-- 置为行首或行尾
-- the 1984 winners AND subject ordered by subject AND winner name; but list Chemistry AND Physics last
SELECT winner, subject FROM nobel
  WHERE yr=1984
  ORDER BY subject IN ('Physics', 'Chemistry') ASC, subject, winner
```

### 9.2. LIMIT

```sql
-- 前 5 行
SELECT * FROM 表 LIMIT 5;
-- 第 4-5 行
SELECT * FROM 表 LIMIT 4, 5;
-- 从第 4 行开始的 5 行
SELECT * FROM 表 LIMIT 5 OFF 4;
SELECT continent, name FROM world x
  WHERE x.name =
  (SELECT y.name FROM world y
    WHERE y.continent=x.continent
      ORDER BY name LIMIT 1)
```

## 10. 多表操作

![sql_join](images/sql_join.png)

### 10.1. JOIN

```sql
-- JOIN == INNER JOIN，无对应关系则不显示
-- The dates of the matches AND the name of the team in which 'Fernando Santos' was the team1 coach
SELECT game.mdate, eteam.teamname
  FROM game JOIN eteam
  ON eteam.id=game.team1 AND eteam.coach='Fernando Santos'
-- LEFT JOIN：以 A 表为基础查找，若 B 中无对应关系，则值为 null
SELECT A.num, A.name, B.name
  FROM A LEFT JOIN B
  USING(nid)
-- RIGHT JOIN：以 B 表为基础查找，若 A 中无对应关系，则值为 null
SELECT A.num, A.name, B.name
  FROM A RIGHT JOIN B
  USING(nid)
-- FULL JOIN：有对应关系的合并，其余保留，非重复字段不加 TABLE 名区分
SELECT name AS country, code, region, basic_unit
  FROM countries FULL JOIN currencies
  USING (code)
  WHERE region = 'North America' OR region IS NULL
  ORDER BY region;
-- CROSS JOIN：没有 ON，相当于合并，并混合排序
SELECT c.name AS city, l.name AS language
  FROM cities AS c
  CROSS JOIN languages AS l
  WHERE c.name LIKE 'Hyder%';
```

### 10.2. USING

USING：Postgres 独有，用于 JOIN 中相同 ON 字段的省略，在自关联中应用极多。

```sql
-- 自关联
-- 直接自关联，会出现相同组合（仅次序不同）
SELECT p1.country_code,
     p1.size AS size2010,
     p2.size AS size2015
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code
-- 此时需要在末尾补充相同字段的关系
  AND p1.year = p2.year - 5;
-- the services which connect the stops 'Craiglockhart' and 'Tollcross'
SELECT a.company, b.num
  FROM route AS a JOIN route AS b
  USING(company) AND USING(num)
  -- 等价于 ON a.company=b.company AND a.num=b.num
  JOIN stops as x ON a.stop=x.id
  JOIN stops as y ON b.stop=y.id
  WHERE x.name='Craiglockhart' AND y.name='Tollcross'
```

### 10.3. 集合操作

```sql
-- UNION：取并集，重合部分合并
SELECT yr, subject, winner FROM nobel
  WHERE subject = 'physics' AND yr=1980
UNION
SELECT yr, subject, winner FROM nobel
  WHERE subject ='chemistry' AND yr=1984
-- UNION ALL：取并集，不处理重合部分
SELECT nickname
  FROM A
UNION ALL
SELECT s_name
  FROM B
-- INTERSECT：取交集
-- EXCEPT：取补集
```

## 11. 聚合与条件

### 11.1. 聚合

```sql
-- the name AND the population of each country in Europe
-- Show the population as a percentage of the population of Germany
SELECT name, CONCAT
  (ROUND(100*population/
    (SELECT population FROM world
      WHERE name='Germany')), '%')
  FROM world WHERE continent='Europe'
```

### 11.2. 嵌套聚合

```sql
/*
SELECT countries.name AS country, COUNT(*) AS cities_num
FROM cities
INNER JOIN countries
ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;
*/
SELECT countries.name AS country,
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
SELECT local_name, subquery.lang_num
FROM countries,
  (SELECT code, COUNT(*) AS lang_num
   FROM languages
   GROUP BY code) AS subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;
```

### 11.3. 条件

```sql
-- CASE...WHEN...THEN...ELSE...END...AS...FROM
SELECT name, continent, code, surface_area,
  CASE WHEN surface_area > 2000000 THEN 'large'
    WHEN surface_area >350000 THEN 'medium'
    ELSE 'small' END
    AS geosize_group
INTO surface_plus
FROM countries;
WHERE year = 2015;
-- COALESCE takes any number of arguments and returns the first not-null value
-- the MSP with no party (such as Canavan, Dennis) you show the string None
SELECT name, party,
  COALESCE(party, 'None') AS aff
  FROM msp
  WHERE name LIKE 'C%';
-- NULLIF returns NULL if the two arguments are equal
-- otherwise NULLIF returns the first argument
SELECT name, party,
  NULLIF(party, 'Lab') AS aff
  FROM msp
  WHERE name LIKE 'C%';
```

## 12. 自定义函数

### 12.1. 创建函数

```sql
-- 模板
CREATE FUNCTION func_name()
RETURNS {VARCHAR|INTEGER|REAL|DECIMAL}
routine_body
-- 实例 1
CREATE FUNCTION chn_time()
RETURNS VARCHAR(30)
RETURN DATE_FORMAT(NOW(), '%Y 年%m 月%d 日');
-- 实例 2
CREATE FUNCTION mean(num1 SMALLINT UNSIGNED, num2 SMALLINT UNSIGNED)
RETURNS FLOAT(10, 2) UNSIGNED
RETURN (num1+num2)/2;
-- 实例 3
DELIMITER //
CREATE FUNCTION add_user(user VARCHAR(20))
RETURNS INT UNSIGNED
BEGIN
INSERT data_base(user) VALUES(user);
RETURN LAST_INSERT_ID();
END
//
```

### 12.2. 删除函数

```sql
DROP FUNCTION [IF EXISTS] func_name
```

### 12.3. `:=`

用户变量赋值有两种方式：用`=`，和用`:=`，其区别在于使用 set 命令对用户变量进行赋值时，两种方式都可使用

当使用 select 语句对用户变量进行赋值时，只能使用`:=`方式，因为在 select 语句中，`=`被看作是比较操作符（用于判断，返回 Boolean）

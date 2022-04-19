# 유저 생성
`CREATE USER 'nodejs'@'%' IDENTIFIED BY '111111';`
# 사용자 확인
`SELECT Host,User FROM mysql.user;`
# 권한 부여
```
GRANT ALL PRIVILLEGES ON opentutorials.* TO `nodejs`@`%`;
```
# 권한 적용
`FLUSH PRIVILEGES;`
# 데이터베이스 보기
`show databases;`
# 데이터베이스 생성
`CREATE DATABASE opentutorials;`
# 테이블 생성
``` SQL
CREATE TABLE `topic` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(30) NOT NULL,
    `description` text,
    `created` datetime NOT NULL,
    `author_id` int(11) DEFAULT NULL,
    PRIMARY KEY(`id`)
);
```
# 데이터 삽입
``` SQL
INSERT INTO `topic` VALUES (1, `MySQL`, `MySQL is...`, `2018-01-01 12:10:11`, 1);
```
# 데이터 가져오기
``` SQL
SELECT * FROM topic
```
``` SQL
SELECT * FROM topic WHERE id=1
```
# 데이터 갱신
``` SQL
UPDATE topic SET title=?, description=?, author_id1 WHERE id=?
```
# 데이터 삭제
``` SQL
DELETE FROM topic WHERE id=?
```
# 테이블 결합
``` SQL
SELECT * FROM topic LEFT JOIN author ON topic.author_id=author.id
```
# 데이터 베이스 선택
``` SQL
mysql> use mysql;
```
# 테이블 보기
``` SQL
mysql> show tables;
```
# 테이블 내용 보기
``` SQL
select * from 테이블명
```
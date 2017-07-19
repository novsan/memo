-- テーブル作成
create table weather(
  city varchar(80),
  temp_lo int,
  temp_hi int,
  prcp real,
  date date
);
create table cities(
  name varchar(80),
  location point
);
drop table cities; -- テーブル削除
-- データ挿入
insert into weather values();
insert into weather(city,temp_lo,temp_hi,prcp,date) values('San Francisco',43,57,0.0,'1994-11-29');
insert into weather(date,city,temp_hi,temp_lo) values('1994-11-29','Hayward',54,37);
insert into weather values('San Francisco',46,50,0.25,'1994-11-27');
insert into cities values('San Francisco','(-194.0,53.0)');
copy weather from '/home/user/weather.txt'; -- ファイルの中身からsqlをコピー
-- テーブルへの問い合わせ
select * from weather;
select city,temp_lo,temp_hi,prcp,date from weather;
select city,(temp_hi+temp_lo)/2 as temp_avg,date from weather;
select * from weather where city='San Francisco' and prcp>0.0;
select * from weather order by city;
select * from weather order by city,temp_lo;
select distinct city from weather;
select distinct city from weather order by city;
-- テーブル間を結合
select * from weather,cities where city=name;
select city,temp_lo,temp_hi,prcp,date,location from weather,cities where city=name;
select weather.city,weather.temp_lo,weather.temp_hi,weather.prcp,weather.date,cities.location from weather,cities where cities.name=weather.city;
-- ↓ 内部結合
select * from weather inner join cities on(weather.city=cities.name);
-- 外部結合
select * from weather left outer join cities on(weather.city=cities.name);
-- 自己結合
select w1.city,w1.temp_lo as low,w1.temp_hi as high,
       w2.city,w2.temp_lo as low,w2.temp_hi as high
from weather w1,weather w2
where w1.temp_lo<w2.temp_lo
and w1.temp_hi>w2.temp_hi;
select * from weather w,cities c where w.city=c.name;

-- 集約関数
select max(temp_lo) from weather;
select city from weather where temp_lo=(select max(temp_lo) from weather);
select city,max(temp_lo) from weather group by city;
select city,max(temp_lo) from weather group by city having max(temp_lo)<40;
select city,max(temp_lo) from weather where city like 'S%' group by city having max(temp_lo)<40;
-- 更新
update weather set temp_hi=temp_hi-2,temp_lo=temp_lo-2 where date>'1994-11-28';
-- 削除
delete from weather where city='Hayward';
-- ビューの作成
create view myview as
  select city,temp_lo,temp_hi,prcp,date,location
    from weather,cities
    where city=name;
-- 外部キー
create table cities(
  city varchar(80) primary key,
  location point
);
create table weather(
  city varchar(80) references cities(city), -- citiesのcityにない項目は挿入できない
  temp_lo int,
  temp_hi int,
  prcp real,
  date date
);
-- トランザクション
begin; -- トランザクション開始
update weather set date='2017-01-01' where city='San Francisco';
savepoint mySave; -- やり直しポイントの作成
update cities set name='TestCity';
rollback to mySave; -- やり直しポイントまで処理を戻す
commit; -- トランザクション確定
-- ウインドウ関数
select city,temp_lo,avg(temp_lo) over(partition by city) from weather;
select city,temp_lo,rank() over(partition by city order by temp_lo desc) from weather;
select sum(temp_lo) over w,avg(temp_lo) over w from weather window w as(partition by city order by temp_lo desc);
-- 継承
create table cities(
  name text,
  population real,
  altitude int
);
create table capitals(
  state char(2)
) inherits(cities);
insert into cities values('Las Vegas',100000,2174);
insert into cities values('Mariposa',89000,1953);
insert into cities values('Las Vegas',65000,845);
insert into capitals values('LA',1200000,1200,'ca');
select name,altitude from only cities where altitude>1000;
-- with句
with cte1 as(
  select name,population from cities
),cte2 as (
  select name,altitude from cities
)
select * from cte1
union all
select * from cte2;
with cte1 as(select city,temp_lo from weather),
cte2 as(select * from cte1)
select * from cte2 order by temp_lo; 
-- 一時テーブル
create temp table test as (
  select name,population from cities
);

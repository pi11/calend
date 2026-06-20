alter TABLE "cal_holiday" add "day_of_the_year" integer NOT NULL default 0;
alter TABLE "cal_holiday" add "week_of_the_month" integer NOT NULL default 0;
alter TABLE "cal_holiday" add "week_day" integer NOT NULL default 0;
alter TABLE "cal_holiday" add "date_type" integer NOT NULL default 0;
alter TABLE "cal_holiday" add "image" varchar(100);
alter table cal_holiday add "next_date" date;

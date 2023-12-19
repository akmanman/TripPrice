### 启动步骤
1、cd TripPrice

2、export FLASK_APP=main

3、nohup flask run --host=0.0.0.0 --port=3009 &

### 请求接口
/api/v1/get_info

### 请求入参
####
    {
        "method": "flight",                 -- method 固定传入 flight
        "params": {                         
            "departure": "成都",             -- departure       出发地
            "destination": "哈尔滨",         -- destination     目的地
            "flight_date": "2023-12-19"     -- flight_date     出发日期
        }
    }

### 返回结果
###
    [
        {
            "airline_name": "海航旗下祥鹏航空",             -- airline_name 航空公司
            "arrival_airport_name": "太平国际机场",        -- arrival_airport_name 到达机场
            "arrival_time": "2023-12-19 17:45:00",       -- arrival_time 到达时间
            "departure_airport_name": "成都天府国际机场",   -- departure_airport_name 出发机场
            "departure_time": "2023-12-19 14:05:00",     -- departure_time 出发时间
            "flight_number": "8L9645",                   -- flight_number 航班号
            "price": 1550,                               -- price 机票价格
            "punctuality_date": "100%"                   -- punctuality_date 准点率
        },
        {
            "airline_name": "厦门航空",
            "arrival_airport_name": "太平国际机场",
            "arrival_time": "2023-12-19 23:35:00",
            "departure_airport_name": "成都天府国际机场",
            "departure_time": "2023-12-19 19:55:00",
            "flight_number": "MF5173",
            "price": 2100,
            "punctuality_date": "100%"
        },
        {
            "airline_name": "厦门航空",
            "arrival_airport_name": "太平国际机场",
            "arrival_time": "2023-12-19 14:20:00",
            "departure_airport_name": "双流国际机场",
            "departure_time": "2023-12-19 10:20:00",
            "flight_number": "MF5479",
            "price": 2100,
            "punctuality_date": "100%"
        },
        {
            "airline_name": "中国国航",
            "arrival_airport_name": "太平国际机场",
            "arrival_time": "2023-12-19 20:30:00",
            "departure_airport_name": "成都天府国际机场",
            "departure_time": "2023-12-19 16:45:00",
            "flight_number": "CA2729",
            "price": 1600,
            "punctuality_date": "100%"
        },
        {
            "airline_name": "中国国航",
            "arrival_airport_name": "太平国际机场",
            "arrival_time": "2023-12-19 19:00:00",
            "departure_airport_name": "成都天府国际机场",
            "departure_time": "2023-12-19 14:05:00",
            "flight_number": "CA2717",
            "price": 2980,
            "punctuality_date": "93%"
        }
    ]

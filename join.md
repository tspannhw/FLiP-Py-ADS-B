### Joining Aircraft Stream in Flink SQL with Weather Stream

````
CREATE CATALOG pulsar WITH (
   'type' = 'pulsar',
   'service-url' = 'pulsar://pulsar1:6650',
   'admin-url' = 'http://pulsar1:8080',
   'format' = 'json'
);

USE CATALOG pulsar;

SHOW TABLES;

describe aircraft;
describe aircraftweather;

````


### Weather Stream

````

Raw JSON Weather Data
{
"noNamespaceSchemaLocation":null,
"version":1.0,
"credit":"NOAA's National Weather Service",
"credit_URL":"https://weather.gov/",
"image":
{"url":"https://weather.gov/images/xml_logo.gif",
"title":"NOAA's National Weather Service",
"link":"https://www.weather.gov"},
"suggested_pickup":"15 minutes after the hour",
"suggested_pickup_period":60,
"location":"Saguache, Saguache Municipal Airport, CO",
"station_id":"K04V",
"latitude":38.09722,
"longitude":-106.16861,
"observation_time":"Last Updated on Sep 12 2022, 4:15 pm MDT",
"observation_time_rfc822":"Mon, 12 Sep 2022 16:15:00 -0600",
"weather":"Fair",
"temperature_string":"79.0 F (26.0 C)",
"temp_f":79.0,
"temp_c":26.0,
"relative_humidity":8,
"wind_string":
"West at 6.9 MPH (6 KT)",
"wind_dir":"West",
"wind_degrees":250,
"wind_mph":6.9,
"wind_kt":6,
"pressure_in":30.25,
"dewpoint_string":"12.2 F (-11.0 C)",
"dewpoint_f":12.2,
"dewpoint_c":-11.0,
"visibility_mi":10.0,
"icon_url_base":"https://forecast.weather.gov/images/wtf/small/",
"two_day_history_url":"https://www.weather.gov/data/obhistory/K04V.html",
"icon_url_name":"skc.png",
"ob_url":"https://www.weather.gov/data/METAR/K04V.1.txt",
"disclaimer_url":"https://www.weather.gov/disclaimer.html",
"copyright_url":"https://www.weather.gov/disclaimer.html",
"privacy_policy_url":"https://www.weather.gov/notice.html"
}

````

### Flink SQL Tables

````

describe aircraft;
+------------------+-----------------------+------+-----+--------+-----------+
|             name |                  type | null | key | extras | watermark |
+------------------+-----------------------+------+-----+--------+-----------+
|         alt_baro |                   INT | true |     |        |           |
|         alt_geom |                   INT | true |     |        |           |
|        baro_rate |                   INT | true |     |        |           |
|         category |                STRING | true |     |        |           |
|        emergency |                STRING | true |     |        |           |
|           flight |                STRING | true |     |        |           |
|               gs |                DOUBLE | true |     |        |           |
|              gva |                   INT | true |     |        |           |
|              hex |                STRING | true |     |        |           |
|              lat |                DOUBLE | true |     |        |           |
|              lon |                DOUBLE | true |     |        |           |
|             mach |                DOUBLE | true |     |        |           |
|         messages |                   INT | true |     |        |           |
|             mlat | ARRAY<ROW<> NOT NULL> | true |     |        |           |
|            nac_p |                   INT | true |     |        |           |
|            nac_v |                   INT | true |     |        |           |
| nav_altitude_mcp |                   INT | true |     |        |           |
|      nav_heading |                DOUBLE | true |     |        |           |
|          nav_qnh |                DOUBLE | true |     |        |           |
|              nic |                   INT | true |     |        |           |
|         nic_baro |                   INT | true |     |        |           |
|               rc |                   INT | true |     |        |           |
|             rssi |                DOUBLE | true |     |        |           |
|              sda |                   INT | true |     |        |           |
|             seen |                DOUBLE | true |     |        |           |
|        seen_post |                DOUBLE | true |     |        |           |
|              sil |                   INT | true |     |        |           |
|         sil_type |                STRING | true |     |        |           |
|            speed |                DOUBLE | true |     |        |           |
|           squawk |                   INT | true |     |        |           |
|             tisb | ARRAY<ROW<> NOT NULL> | true |     |        |           |
|            track |                DOUBLE | true |     |        |           |
|          version |                   INT | true |     |        |           |
+------------------+-----------------------+------+-----+--------+-----------+


Join on aircraft.lon = X, aircraft.lat = Y

````

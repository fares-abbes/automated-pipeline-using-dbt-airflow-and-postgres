{{ config(
    materialized='table',
    unique_key='report_id'
) }}
select 
    city,
    date(weather_time_local) as date,
    round(avg(temperature)::numeric, 2) as avg_temperature,
    round(avg(wind_speed)::numeric, 2) as avg_wind_speed
from {{ ref('staging_weather_data') }}
group by 
    city,
    date(weather_time_local)
order by 
    city,
    date(weather_time_local)
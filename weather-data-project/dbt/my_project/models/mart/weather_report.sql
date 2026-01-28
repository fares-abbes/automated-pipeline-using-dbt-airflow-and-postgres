{{ config(
    materialized='table',
    unique_key='report_id'
) }}
select 
    city,
    temperature,
    weather_description,
    wind_speed,
    weather_time_local
 from {{ ref('staging_weather_data') }}
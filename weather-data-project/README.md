# Weather Data Pipeline Project

## 📋 Project Overview

This is an **automated data engineering pipeline** that collects real-time weather data from New York City, stores it in a PostgreSQL database, and transforms it using dbt (Data Build Tool). The entire workflow is orchestrated by Apache Airflow and containerized using Docker.

## 🏗️ Architecture

The project consists of four main components:

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────┐
│   Airflow   │─────>│ API Request  │─────>│  PostgreSQL │─────>│   dbt    │
│ Orchestrator│      │ (Weatherstack)│      │  Database   │      │Transform │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────┘
```

### Components:

1. **Apache Airflow** - Orchestrates the data pipeline
2. **Weather API** - Fetches weather data from Weatherstack API
3. **PostgreSQL** - Stores raw and transformed data
4. **dbt** - Transforms raw data into analytics-ready tables

## 🚀 What Does This Project Do?

### Data Collection (Every 5 Minutes)
- Fetches current weather data for **New York City** from Weatherstack API
- Collects metrics including:
  - Temperature
  - Weather description (e.g., "Mist", "Clear")
  - Wind speed
  - Local time
  - UTC offset

### Data Storage
- Stores raw weather data in PostgreSQL database
- Schema: `dev.raw_weather_data`
- Tracks when data was collected (`inserted_at` timestamp)

### Data Transformation (dbt)
- Transforms raw data into staging tables
- Converts timestamps from UTC to local time
- Creates analytics-ready tables for downstream use

### Automation
- Airflow DAG runs **every 5 minutes**
- Automatically fetches, stores, and can trigger dbt transformations
- Self-healing and monitored through Airflow UI

## 🛠️ Technology Stack

- **Docker & Docker Compose** - Container orchestration
- **Apache Airflow 3.1.5** - Workflow orchestration
- **PostgreSQL 15.15** - Data warehouse
- **dbt-postgres 1.9** - Data transformation
- **Python 3.x** - Application logic
- **Weatherstack API** - Weather data source

## 📁 Project Structure

```
weather-data-project/
├── docker-compose.yaml          # Docker services configuration
├── airflow/
│   └── dags/
│       ├── orchestrator.py      # Main DAG (runs every 5 min)
│       └── insert_records.py    # Legacy ingestion script
├── api-request/
│   ├── api_request.py           # Weather API client
│   └── insert_records.py        # Data ingestion logic
├── dbt/
│   ├── profiles.yml             # dbt connection settings
│   └── my_project/
│       ├── dbt_project.yml
│       └── models/
│           ├── sources/
│           │   └── sources.yml  # Source table definitions
│           └── staging/
│               └── staging.sql  # Staging transformations
└── postgres/
    └── airflow_init.sql         # Initial database setup
```

## 🚦 Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Internet connection (for API calls)

### Setup & Run

1. **Clone the repository**
   ```bash
   cd repos/weather-data-project
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access services**
   - **Airflow UI**: http://localhost:8080
     - Username: Check Airflow standalone output
     - Password: Check Airflow standalone output
   - **PostgreSQL**: `localhost:5000`
     - Database: `db`
     - Username: `db_user`
     - Password: `db_password`

4. **Monitor the pipeline**
   - Open Airflow UI
   - Check the `weather-api-orchestrator` DAG
   - Data collection runs every 5 minutes

### Stopping Services
```bash
docker-compose down
```

### Stopping and Removing All Data
```bash
docker-compose down -v
```

## 📊 Data Flow

1. **Airflow DAG triggers** (every 5 minutes)
   ↓
2. **API Request** - Calls Weatherstack API for NYC weather
   ↓
3. **Data Insertion** - Inserts raw data into `dev.raw_weather_data` table
   ↓
4. **dbt Transformation** - Transforms data in staging layer
   ↓
5. **Analytics-Ready Data** - Available for queries/dashboards

## 🗄️ Database Schema

### Raw Table: `dev.raw_weather_data`
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| city | TEXT | City name (New York) |
| temperature | FLOAT | Temperature in Celsius |
| weather_description | TEXT | Weather condition |
| wind_speed | FLOAT | Wind speed |
| time | TIMESTAMP | Local time of observation |
| inserted_at | TIMESTAMP | UTC time when record was inserted |
| utc_offset | TEXT | UTC offset for timezone conversion |

## 🔧 Configuration

### API Key
Update the Weatherstack API key in `api-request/api_request.py`:
```python
api_key = "your_api_key_here"
```

### Schedule
Modify the schedule in `airflow/dags/orchestrator.py`:
```python
schedule=timedelta(minutes=5)  # Change to desired interval
```

### Location
Change the city in `api-request/api_request.py`:
```python
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=London"
```

## 📈 Monitoring & Troubleshooting

### Check Container Logs
```bash
# Airflow logs
docker logs airflow_container

# Database logs
docker logs weather-data-project-db-1

# dbt logs
docker logs dbt_container
```

### Check Database Records
```bash
docker exec -it weather-data-project-db-1 psql -U db_user -d db
```
```sql
SELECT * FROM dev.raw_weather_data ORDER BY inserted_at DESC LIMIT 10;
```

### Airflow DAG Not Running?
1. Check Airflow UI at http://localhost:8080
2. Verify DAG is enabled (toggle switch)
3. Check DAG run history for errors

## 🎯 Use Cases

- **Weather trend analysis** - Track temperature changes over time
- **Learning data engineering** - Hands-on experience with modern data stack
- **Real-time monitoring** - Observe weather patterns every 5 minutes
- **ETL pipeline template** - Use as base for other data pipelines

## 🔮 Future Enhancements

- [ ] Add more cities for comparison
- [ ] Create data visualization dashboard (e.g., Metabase, Grafana)
- [ ] Add data quality tests in dbt
- [ ] Implement alerting for extreme weather conditions
- [ ] Add historical weather data analysis
- [ ] Create mart layer for business analytics
- [ ] Add automated dbt runs after each data ingestion

## 📝 Notes

- The project uses a **mock data function** available in `api_request.py` for testing without API calls
- Airflow runs in **standalone mode** for simplicity (not production-ready)
- PostgreSQL data is persisted in `./postgres/data` volume

## 🤝 Contributing

This is a learning/portfolio project. Feel free to fork and enhance it!

## 📄 License

This project is for educational purposes.

---

**Built with** ❄️ by monitoring New York weather every 5 minutes!

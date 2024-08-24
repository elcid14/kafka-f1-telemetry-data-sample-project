# F1 Telemetry Data Kafka Project

## Description

This project is used to show an understanding and knowledge of Kafka, pub/sub infrastructure, and ETL concepts more generally.
The project is designed to have the following outcomes:

1. Feed sample f1 telemetry data from openf1 schema into Kafka topic.
2. The Kafka producer then generates a new b sting message of the telemetry data.
3. The Kafka consumer then processed the message, and writes to data to postgersql table to persist for future front end application.
4. Utilize streamz library to consume Kafka streams from one topic, transform the data, then stream to new topic and have consumer write that data to postgresql table.

## Development Notes:
- Requires Python version 3.10^
- Requires install poetry to properly use poetry shell to manage depdendcies(infrastructure and scripts have seperate venvs as we do not need to share packages between the two at a global level)
- Requires docker installed.

## Directory structure:
```
├── README.md
├── infrastructure
│   ├── docker-compose.yml
│   └── models
│       ├── main.py
│       ├── poetry.lock
│       └── pyproject.toml
└── scripts
    ├── consumer.py
    ├── create-topic.sh
    ├── generate_f1_telemetry_data.py
    ├── poetry.lock
    ├── producer.py
    └── pyproject.toml
```

## Running pipeline:

1. cd into infrastructure directory.
2. 

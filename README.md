# F1 Telemetry Data Kafka Project

## Description

This project is used to show an understanding and knowledge of Kafka, pub/sub infrastructure, and ETL concepts more generally
The project is designed to have the following outcomes:

1. Feed sample f1 telemetry data from openf1 schema into Kafka topic.
2. The Kafka producer then generates a new b sting message of the telemetry data.
3. The Kafka consumer then processed the message, and writes to data to postgersql table to persist for future front end application. 

## Directory structure:

> 
>
>
>
>
>
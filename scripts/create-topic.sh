while ! nc -z localhost:9092; do
    sleep 0.1
done

kafka-topics --create --topic f1-telem-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

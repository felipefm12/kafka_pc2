from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('test-topic', b'Hola mundo con Kafka!')
print("Message produced: Hola mundo con Kafka!")

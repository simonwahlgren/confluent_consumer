## Versions
```sh
$ docker-compose exec consumer python
>>> import confluent_kafka
>>> confluent_kafka.version()
('0.11.0', 720896)
>>> confluent_kafka.libversion()
('0.11.0', 721151)
```
## Reproduce
1. Start the environment
```sh
docker-compose up -d
docker-compose logs -f consumer
```
2. In another terminal produce a message
```sh
echo $(date) | kafkacat -P -b localhost -t foobar
```
3. Everything should nice and dandy up to this point, but if we produce another
message the consumer process will get stuck.

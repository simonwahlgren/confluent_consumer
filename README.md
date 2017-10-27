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

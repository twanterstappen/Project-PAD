docker compose up -d
docker compose -f docker-compose-lvl1.yaml -d

if [ "$( docker container inspect -f '{{.State.Running}}' $container_name )" == "true" ]; then ...
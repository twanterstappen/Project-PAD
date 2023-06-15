#!/bin/bash
current=$(pwd)


read -p "Do you want to compose up(y/N)?" CONT

if [ "$CONT" = "y" ] ; then
    echo -ne '\e[33mRemoving all containers/images/volumes\e[0m'
    sleep 1
    echo -ne "."
    echo -ne "."
    echo -ne "."
    sleep 1

    # stop all containers
    docker stop $(docker ps -aq)
    # remove all containers
    docker rm $(docker ps -aq)
    # remove all images
    docker rmi $(docker images -q)
    # remove all volumes
    docker volume prune -f

    echo -ne '\e[33mStart composing\e[0m'
    sleep 1
    echo -ne "."
    echo -ne "."
    echo -ne "."
    sleep 1

    # main website
    docker compose up -d
    # sql1
    docker compose -f ctf/sql1/docker-compose.yaml up -d
    # sql2
    docker compose -f ctf/sql2/docker-compose.yaml up -d
    # sql3
    docker compose -f ./ctf/sql3/docker-compose.yaml up -d
    # crypto1
    docker compose -f ./ctf/crypto1/docker-compose.yaml up -d
    # crypto2
    docker compose -f ./ctf/crypto2/docker-compose.yaml up -d
    # crypto3
    docker compose -f ./ctf/crypto3/docker-compose.yaml up -d
    # url1
    docker compose -f ./ctf/url1/docker-compose.yaml up -d
    # url2
    docker compose -f ./ctf/url2/docker-compose.yaml up -d
    # impersonation1
    docker compose -f ./ctf/impersonation1/docker-compose.yaml up -d
    # steganography
    docker compose -f ./ctf/steganography1/docker-compose.yaml up -d
else
    echo -ne '\e[33mRemoving all containers/images/volumes\e[0m'
    sleep 1
    echo -ne "."
    echo -ne "."
    echo -ne "."
    sleep 1

    # stop all containers
    docker stop $(docker ps -aq)
    # remove all containers
    docker rm $(docker ps -aq)
    # remove all images
    docker rmi $(docker images -q)
    # remove all volumes
    docker volume prune -f
fi



echo -e '\e[32mDone\e[0m'
sleep 5
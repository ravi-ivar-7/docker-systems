This is a simple example of a scale-to-zero scenario with docker, traefik and sablier.

For more informations, see [this blog post](https://www.production-ready.de/2023/08/20/docker-scale-to-zero-with-traefik-sablier-en.html)
(german version [here](https://www.production-ready.de/2023/08/20/docker-scale-to-zero-with-traefik-sablier.html)).




docker compose -f docker-compose-traefik.yaml up -d
docker compose -f docker-compose-whoami.yaml up -d


above code is required when we want our sablier service to run independent of traefik conatiner, but we can also lable sablier with traefik direclty

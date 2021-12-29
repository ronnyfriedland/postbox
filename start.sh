/bin/sh

set -e

sudo docker run -dit --privileged --rm --name postbox --network=intranet -e VAULT_URL=https://$(sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' vault):8200 -e VAULT_TOKEN=$VAULT_TOKEN -v $PWD:/postbox postbox

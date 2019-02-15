# Delete old Docker Images
`docker rmi $(docker images --filter "since=511136ea3c5a" -q)`

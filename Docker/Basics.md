# Delete old Docker Images
`docker rmi $(docker images --filter "since=[PutImageShaHere]" -q)`

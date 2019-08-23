# Disk Images

## Copy all partitions of an SD card
1. `diskutil list`
2. Select from that list the identifier (like `/dev/random-made-up-name`) that corresponds to the device you wanna copy
3. `sudo dd bs=8192 if='/dev/THAT-THING-YOU-SELECTED' of="path/to/put/the/dmgfile.dmg"`

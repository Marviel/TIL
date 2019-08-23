# Disk Images

## Copy all partitions of an SD card
0. `diskutil list`
1. Select from that list the identifier (like `/dev/disk2`) that corresponds to the device you wanna copy (if your system supports `rdisk`, add an `r` at the beginning to make it faster -- a-la `/dev/disk2` -> `/dev/rdisk2`)
2. (optional) get the optimal block size by running `stat -s /dev/THE-DEVICE-ID` and recording the value of `st_blksize`
3. `sudo dd bs=8192 if='/dev/THAT-THING-YOU-SELECTED' of="path/to/put/the/dmgfile.dmg"` (substitute `st_blksize` for 8192 if you did the previous step)
4. Wait for a long time.



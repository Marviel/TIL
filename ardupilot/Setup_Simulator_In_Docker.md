# Outside the docker container

Run the docker container to expose the correct ports, such as:
- 5670
- 5541
- 14550
- 14551

# Inside the docker container

```shell
./waf copter
./waf configure SITL_x86_64_linux_gnu
pip install -U future
./waf copter
cd ArduCopter/
pip install -U pymavlink
sim_vehicle.py -w
```

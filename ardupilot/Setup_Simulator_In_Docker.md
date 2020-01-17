# Outside the docker container

--master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551

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

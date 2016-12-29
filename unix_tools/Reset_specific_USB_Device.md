#Intro
I find myself sometimes wanting to identify and reset a *specific* usb device. 
This can be helpful as a hotplugging technique, or just for badly designed usb devices.

#Steps

First run:

```
sudo apt-get install libusb-dev
```

Then, this c++ file should perform the task you ask.
```
#include <libusb-1.0/libusb.h>

int resetDeviceConnection(UINT_16 vid, UINT_16 pid){
    /*Open libusb*/
    int resetStatus = 0;
    libusb_context * context;
    libusb_init(&context);
    
    libusb_device_handle * dev_handle = libusb_open_device_with_vid_pid(context,vid,pid);
    if (dev_handle == NULL){
      printf("usb resetting unsuccessful! No matching device found, or error encountered!\n");
      resetStatus = 1;
    }
    else{
      /*reset the device, if one was found*/
      resetStatus = libusb_reset_device(dev_handle);
    }
    /*exit libusb*/
    libusb_exit(context);
    return resetStatus;
}
```

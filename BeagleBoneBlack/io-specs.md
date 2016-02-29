The BeagleBoneBlack is great, but it's important to note a few things about its io capabilities.

1. GPIO is 3.3v. Make sure that if you're trying to use anything other than that as your GPIO that you get some logic level converters (check sparkfun)
2. The USB hub is *not powered very well*.  It'll work for things like keyboards, but for anything else you'll need to use a powered usb hub.

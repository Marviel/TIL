Apparently, when you add a script to rc.local, that script has the ability to run before the raspberry pi is assigned an ip addresss.

So, if you try to, say, open a socket in a script that starts via rc.local, you could have a bad time.

I encountered this situation when I switched from my raspberry pi B+ to a raspberry pi 3. Obviously, the 3 is faster.

The simple fix for this is just to add in a "sleep" command for however long it takes for the ip address to be assigned.

I'm sure there's a cleverer way to go about this, but that seems to work for my simple purposes.

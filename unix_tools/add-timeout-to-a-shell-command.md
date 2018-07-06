# The timeout Command

*OSX NOTE: 'timeout' cmd requires you to first 'brew install coreutils', and is called with 'gtimeout'*

if you run:

    timeout [DURATION (float)][INCREMENT ('s'|'m'|'h'|'d')]  [COMMAND]
    

Then you'll get a timeout lasting DURATION INCREMENTs.
The default is seconds.

So, for instance:

    timeout 3s top

gives you the top screen for 3 seconds, and then the 'top' command terminates.


# Reference:

http://man7.org/linux/man-pages/man1/timeout.1.html

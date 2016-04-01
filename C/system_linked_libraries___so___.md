#.SO files and the like

When you run gcc/g++, you're able to specify the "-l" flag, which allows you to link system libraries into whatever it is you're compiling.

For example, in some instances (using the Timing libraries) you need to link the real time libraries. The g++ flag for that is "-lrt".

So, if you're compiling a program called "RealTime.cpp" you might compile it like so:

    g++ -g -o RealTimeExecutable RealTime.cpp -lrt
    

I'm not sure exactly where this lives, but on my system if I put a ".so" file in the folder: "/usr/local/lib/", and name it "libmylib.so",
you should be able to link to it from gcc/g++ like so:

    g++ -g -o Program Program.cpp -lmylib
    
(The "lib-" prefix on the file "libmylib.so" is ignored.

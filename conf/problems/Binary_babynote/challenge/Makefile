all:
	gcc -Wl,-z,now,-z,relro babynote.c -o babynote -pie -fstack-protector
	mv babynote ../distfiles
	cp /lib/x86_64-linux-gnu/libc-2.27.so ../distfiles
	cp babynote.c ../distfiles

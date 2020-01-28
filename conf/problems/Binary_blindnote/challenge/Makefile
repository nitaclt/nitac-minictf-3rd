all:
	gcc -Wl,-z,now,-z,relro blindnote.c -o blindnote -pie -fstack-protector
	mv blindnote ../distfiles
	cp /lib/x86_64-linux-gnu/libc-2.27.so ../distfiles
	cp blindnote.c ../distfiles

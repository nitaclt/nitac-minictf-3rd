FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install xinetd
RUN groupadd -r pwn && useradd -r -g pwn pwn

ADD assets/pwn.xinetd /etc/xinetd.d/pwn
ADD assets/init.sh    /etc/init.sh
ADD assets/redir.sh   /home/pwn/redir.sh
RUN chmod 550        /home/pwn/redir.sh
RUN chmod 700        /etc/init.sh
RUN chmod 1733 /tmp /var/tmp /dev/shm

ADD flag.txt  /home/pwn/flag.txt
ADD shellcode /home/pwn/shellcode
RUN chmod 440 /home/pwn/flag.txt
RUN chmod 550 /home/pwn/shellcode

RUN chown -R root:pwn /home/pwn

RUN ls /home/pwn -lh

RUN service xinetd restart

ENTRYPOINT /etc/init.sh
EXPOSE 80

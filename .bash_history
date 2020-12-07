apt update && apt upgrade -y && apt autoremove -y
apt install libprotobuf-dev libprotobuf-c-dev protobuf-c-compiler protobuf-compiler python-protobuf
apt install pkg-config python-ipaddress libbsd-dev iproute2 libnftables-dev libcap-dev libnl-3-dev libnet-dev libaio-dev
apt install pkg-config python-ipaddress libbsd-dev iproute2 nftables libcap-dev libnl-3-dev libnet-dev libaio-dev 
add-apt-repository ppa:criu/ppa
apt update
apt install criu
git clone https://github.com/checkpoint-restore/criu.git
history
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt update
apt-cache policy docker-ce=17.03.2~ce-0~ubuntu-xenial
apt-get install docker-ce=17.03.2~ce-0~ubuntu-xenial
docker run -d --name looper2 --security-opt seccomp:unconfined busybox          /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker checkpoint create --checkpoint-dir=/tmp looper2 checkpoint2
nano /etc/docker/daemon.json
service docker restart
docker version
docker status
service docker status
docker ps
docker run -d --name looper2 --security-opt seccomp:unconfined busybox          /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker rm -rf $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker run -d --name looper2 --security-opt seccomp:unconfined busybox          /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker checkpoint create --checkpoint-dir=/tmp looper2 checkpoint2
docker create --name looper-clone --security-opt seccomp:unconfined busybox          /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker start --checkpoint-dir=/tmp --checkpoint=checkpoint2 looper-clone
docker ps
docker rm -f $(docker ps -aq)
exit
ls
cd heartbleed-masstest/
./ssltest.py 172.17.0.2 -p 9000
cd /
python3
docker ps
docker run -dit --name main_web root_web-server
docker rm /main_web
docker run -dit --name main_web root_web-server
docker rm /main_web
docker run -dit --name main_web root_web-server
docker stop -f $(docker ps -aq) && docker rm /main_web
docker ps
docker run -dit --name main_web root_web-server
docker run -dit --name main_web
docker run -dit main_web
docker run -dit root_web-server
docker ps
docker ps --format {{.Image}}
docker run -dit root_web-server
docker ps
docker rm -f $(docker ps -aq)
docker ps
docker logs
docker logs $(docker ps)
docker logs $(docker ps -q)
docker logs root_web-server
docker ps
docker ps -aq
docker ps -a
docker logs main_web
docker ps
docker run -dit --name main_web root_web-server
docker rm /main_web
docker run -dit --name main_web root_web-server
docker ps
cd ../webserver/
docker build .
docker ps
docker images
cd ..
ls
docker-compose up
apt install docker-compose
curl -L https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose 
docker-compose up
docker-compose up --scale web-server=20
pwd
ls
docker-compose up
pwd
ls
docker ps
docker images
docker rmi -f $(docker images -q)
docker-compose up
docker-compose build
docker run -d root_web-server
docker ps -q
docker cp 5c47d7b73d01:/openssl-1.0.2l/ssl/d1_both.c
docker cp 5c47d7b73d01:/openssl-1.0.2l/ssl/d1_both.c .
docker cp d1_both.c 5c47d7b73d01:/openssl-1.0.2l/ssl/d1_both.c
cd ..
cd heartbleed-masstest/
ls
docker inspect $(docker ps -q)
docker inspect $(docker ps -q) | grep IPA
python
chmod +x ssltest.py 
./ssltest.py 172.17.0.2 -p 12345
ls
rm log.txt results.txt 
rm index.html*
ls
pip install netaddr
apt install python-pip
pip install netaddr
pip install --upgrade pip
pip install netaddr
./ssltest.py 172.17.0.2 -p 12345
./ssltest.py 172.17.0.2 -p 9000
docker exec -it $(docker ps -q) /bin/bash
./ssltest.py 172.17.0.2 -p 9000
docker inspect $(docker ps -q) | grep IPA
./ssltest.py 172.17.0.2 -p 9000
./ssltest.py 172.17.0.2 -p 12345
nmap
./ssltest.py 127.0.0.1 -p 80
ufw allow 80

docker inspect $(docker ps -q) | grep IPA
wget 127.0.0.1/mal:9000
wget 127.0.0.1:9000/mal
wget 127.0.0.1:9001/mal
wget 127.0.0.1:9000/mal
wget 127.0.0.1:9001/mal
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
pip install --upgrade sultan
pip3 install --upgrade sultan
apt instal python3-pip
apt install python3-pip
python4
python3
python
pip3
python3-pip
pip3 help
pip3 -v
python3 -m pip install --upgrade pip
pip3 install sultan
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9000/malicious
wget 127.0.0.1:9001/malicious
wget 127.0.0.1:9002/malicious
wget 127.0.0.1:9000/malicious
docker ps
docker run -d --name looper2 --security-opt seccomp:unconfined busybox /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker checkpoint create --checkpoint-dir=/tmp looper2 checkpoint2 --leave-running=true
rm /tmp/checkpoint2/
rm -rf /tmp/checkpoint2/
ls
docker checkpoint create --checkpoint-dir=/tmp looper2 checkpoint2 --leave-running=true
docker create --name looper-clone --security-opt seccomp:unconfined busybox /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'
docker start --checkpoint-dir=/tmp --checkpoint=checkpoint2 looper-clone
ifconfig
docker inspect $(docker ps -q) | grep IPA
openssl s_server
openssl req -x509 -nodes -newkey rsa -keyout key.pem -out cert.pem -subj /CN=localhost
echo 'hello, world.' >index.txt
openssl s_server -key key.pem -cert cert.pem -WWW
cp -r vulnerable/ honey_patched
ls
whereis openssl
cd honey_patched/
docker build .
git clone https://github.com/openssl/openssl.git && git switch OpenSSL_1_0_2-stable
docker stop $(docker ps -aq)
apt install git
git checkout -b OpenSSL_1_0_2-stable
docker images
docker run -it f643c72bc252 /bin/bas
docker run -it f643c72bc252 /bin/bash
docker build .
docker build .\
docker 
docker build .\
docker build .
docker ps -aq
docker ps -a
docker run -it 33d1b6c5b4f5 /bin/bash
docker run -it pensive_morse /bin/bash
docker images
docker run -it 387143c5c97e /bin/bash
docker build .
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)
docker build .
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)
docker rmi -f $(docker images -q)
docker build .
docker rmi -f $(docker images -q)
docker build .
docker rmi -f $(docker images -q)
docker build .
docker images
docker run -it d9984043087a /bin/bash
docker rmi -f $(docker images -q)
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)
docker build .
docker images
docker run -it 07606d2ef7e2 /bin/bash
docker build .
docker images
docker run -it 2ab13369fb37 /bin/bash
docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)
docker build .
docker images
docker run -it 2b09fd05540f /bin/bash
docker run -it 2b09fd05540f /bin/bash -p 80:80
docker run -p 80:12345 -it 2b09fd05540f /bin/bash
cd ../proxy-server/
ls
apt install python3
python3 proxy-server.py 
docker ps
python3 proxy-server.py 
docker images
docker ps
docker images
docker images -h
docker images -f REPOSITORY
docker images root_web-server
docker images --format "{{.Repository}}"
docker images
docker images -q
docker rmi 8a4a79f43682
docker rmi -f  8a4a79f43682
docke rps
docker ps
docker stop $(docker ps -q)
docker rmi -f  8a4a79f43682
docker rmi -f $(docker images -q)
python3 proxy-server.py 
cd ..
python3 proxy-server.py 
docker rmi -f $(docker images -q)
python3 proxy-server.py 
docker rmi -f $(docker images -q)
python3 proxy-server.py 
docker rmi -f $(docker images -q)
python3 proxy-server.py 
docker rmi -f $(docker images -q)
python3 proxy-server.py 
docker rmi -f $(docker images -q)
python3 proxy-server.py 
python3 proxy-server.py
docker images --format {{.Repository}}
docker rmi -f $(docker images -q)
python3 proxy-server.py
docker rmi -f $(docker images -q)
python3 proxy-server.py
docker rmi -f $(docker images -q)
python3 proxy-server.py
cd honey_patched/
ls
nano +4040 t1_lib.c 
nano t1_lib.c 
cat t1_lib.c | grep silently
cat t1_lib.c | grep payload
cat t1_lib.c 
cat t1_lib.c | head -n 20
exit

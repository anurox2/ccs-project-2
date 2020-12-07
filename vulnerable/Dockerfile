## Get old debian version
FROM debian:wheezy

# Environment variables to be setup
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Backup the old sources file at /etc/apt/sources.list
RUN mv /etc/apt/sources.list /etc/apt/sources.listbackup
COPY ./sources.list /etc/apt/sources.list

# Get current
RUN apt-get -o Acquire::Check-Valid-Until=false update -y
RUN apt-get dist-upgrade -y

# Install packages 
RUN apt-get install -y wget
RUN apt-get install -y apache2 multiarch-support

# Install vulnerable versions from wayback/snapshot archive
RUN wget http://snapshot.debian.org/archive/debian/20130319T033933Z/pool/main/o/openssl/libssl1.0.0_1.0.1e-2_amd64.deb -O /tmp/libssl1.0.0_1.0.1e-2_amd64.deb && \
 dpkg -i /tmp/libssl1.0.0_1.0.1e-2_amd64.deb

RUN wget http://snapshot.debian.org/archive/debian/20130319T033933Z/pool/main/o/openssl/openssl_1.0.1e-2_amd64.deb -O /tmp/openssl_1.0.1e-2_amd64.deb && \
 dpkg -i /tmp/openssl_1.0.1e-2_amd64.deb


ENV DEBIAN_FRONTEND noninteractive

# Setup vulnerable web server and enable SSL based Apache instance
# ADD index.html /var/www/

# Disable listening on port 80
RUN sed -i 's/^NameVirtualHost/#NameVirtualHost/g' /etc/apache2/ports.conf
RUN sed -i 's/^Listen/#Listen/g' /etc/apache2/ports.conf

# RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/vul.key -out /etc/ssl/vul.crt -subj "/C=US/ST=KS/L=Wichita/O=WSU/OU=EECS/CN=172.18.0.2/emailAddress=aman@aman.com"

COPY ./default-ssl /etc/apache2/sites-available/default-ssl


# Enable SSL    
RUN a2enmod ssl
# RUN a2dissite default
# Enable the secure default website
RUN a2ensite default-ssl

# Clean up 
RUN apt-get autoremove -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the port for usage with the docker -P switch
EXPOSE 443

# Run Apache 2
# CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
CMD apache2ctl -D FOREGROUND
# RUN /usr/sbin/apache2ctl -D FOREGROUND
# RUN service apache2 restart
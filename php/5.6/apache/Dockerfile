FROM php:5.6-apache

RUN groupadd -f -g 1000 localgroup \
	&& useradd -u 1000 -g 1000 localuser \
	&& mkdir -p /home/localuser \
	&& chown -R /home/localuser \
	&& echo -e "COLUMNS=1024\nLINES=50" > /home/localuser/.bashrc

RUN apt-get update \
	&& apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng12-dev \
		libcurl4-openssl-dev \
		libxml2-dev \
		libmemcached-dev \
		zlib1g-dev \

	&& docker-php-ext-install -j$(nproc) calendar \
	&& docker-php-ext-install -j$(nproc) ctype \
	&& docker-php-ext-install -j$(nproc) curl \
	&& docker-php-ext-install -j$(nproc) dom \
	&& docker-php-ext-install -j$(nproc) fileinfo \
	&& docker-php-ext-install -j$(nproc) hash \
	&& docker-php-ext-install -j$(nproc) iconv \
	&& docker-php-ext-install -j$(nproc) json \
	&& docker-php-ext-install -j$(nproc) mbstring \
	&& docker-php-ext-install -j$(nproc) mcrypt \
	&& docker-php-ext-install -j$(nproc) mysqli \
	&& docker-php-ext-install -j$(nproc) pdo \
	&& docker-php-ext-install -j$(nproc) pdo_mysql \
	&& docker-php-ext-install -j$(nproc) soap \
	&& docker-php-ext-install -j$(nproc) xml \
	&& docker-php-ext-install -j$(nproc) xmlreader \
	&& docker-php-ext-install -j$(nproc) zip \
	&& pecl install memcached-2.2.0 \
	&& docker-php-ext-enable memcached \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ENV PMA_VERSION 4.6.5.2
ENV PMA_DOWNLOAD_URL https://files.phpmyadmin.net/phpMyAdmin/${PMA_VERSION}/phpMyAdmin-${PMA_VERSION}-all-languages.tar.gz

RUN cd /usr/share \
	&& curl --output phpMyAdmin.tar.gz --location ${PMA_DOWNLOAD_URL} \
	&& tar -xzf phpMyAdmin.tar.gz \
	&& mv phpMyAdmin-* phpMyAdmin \
	&& cp phpMyAdmin/config.sample.inc.php phpMyAdmin/config.inc.php \
	&& echo "\$cfg['Servers'][\$i]['host'] = \$_ENV['PMA_HOST'] ? \$_ENV['PMA_HOST'] : 'localhost';\$cfg['blowfish_secret'] = '3a7f33fc853c';" >> phpMyAdmin/config.inc.php \
	&& echo "Alias /phpmyadmin /usr/share/phpMyAdmin/\n<Directory /usr/share/phpMyAdmin/>\n\tRequire all granted\n\tOptions FollowSymlinks\n</Directory>" > /etc/apache2/conf-enabled/phpMyAdmin.conf \
	&& rm -f phpMyAdmin.tar.gz

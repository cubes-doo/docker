FROM php:7.2-fpm

ARG localuser=1000
ARG localgroup=1000

RUN groupadd -f -g $localgroup localgroup \
	&& useradd -u $localuser -g $localgroup localuser \
	&& mkdir -p /home/localuser \
	&& chown -R localuser:localgroup /home/localuser \
	&& printf "COLUMNS=1024\nLINES=50\n" | tee /home/localuser/.bashrc \
	&& printf "[www]\nuser=localuser\ngroup=localgroup\n" | tee /usr/local/etc/php-fpm.d/zz-local.conf \
	
	&& apt-get update \
	
	&& apt-get -y install libmcrypt-dev \
	&& printf "\n" | pecl install mcrypt-1.0.1 \
	&& docker-php-ext-enable mcrypt \
	
	&& apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
	
	&& docker-php-ext-install -j$(nproc) \
		bcmath \
		mysqli \
		pdo_mysql \
		zip \
		
	&& apt-get -y install libxml2-dev \
	&& docker-php-ext-install -j$(nproc) \
		simplexml \
		soap \
	
	&& apt-get -y install libmagickwand-dev \
	&& printf "\n" | pecl install imagick \
	&& docker-php-ext-enable imagick \
	
	&& apt-get -y install libssl-dev \
	&& printf "\n" | pecl install mongodb \
	&& docker-php-ext-enable mongodb \
	
	&& printf "\n" | pecl install redis \
	&& docker-php-ext-enable redis \
	
	&& apt-get -y install libyaml-dev \
	&& printf "\n" | pecl install yaml \
	&& docker-php-ext-enable yaml \
	
	
	&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
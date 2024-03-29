FROM php:7.4-fpm

ARG localuser=1000
ARG localgroup=1000

RUN groupadd -f -g $localgroup localgroup \
&& useradd -u $localuser -g $localgroup localuser \
&& mkdir -p /home/localuser \
&& chown -R localuser:localgroup /home/localuser \
&& printf "COLUMNS=1024\nLINES=50\n" | tee /home/localuser/.bashrc \
&& printf "[www]\nuser=localuser\ngroup=localgroup\n" | tee /usr/local/etc/php-fpm.d/zz-local.conf \
\
&& apt-get update \
&& apt install ca-certificates \
&& apt install libgnutls30 \
\
&& apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libwebp-dev \
&& docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
&& docker-php-ext-install -j$(nproc) gd \
\
&& docker-php-ext-install -j$(nproc) exif \
\
&& apt-get install -y \
    libzip-dev \
&& docker-php-ext-install -j$(nproc) \
    bcmath \
    mysqli \
    pdo_mysql \
    zip \
\
&& apt-get -y install libxml2-dev \
&& docker-php-ext-install -j$(nproc) \
    simplexml \
    soap \
\
&& apt-get -y install libgmp-dev \
&& docker-php-ext-install -j$(nproc) \
    gmp \
\
&& apt-get -y install libmagickwand-dev \
&& printf "\n" | pecl install imagick \
&& docker-php-ext-enable imagick \
\
&& apt-get -y install libssl-dev \
&& printf "\n" | pecl install mongodb \
&& docker-php-ext-enable mongodb \
\
&& printf "\n" | pecl install redis \
&& docker-php-ext-enable redis \
\
&& apt-get -y install libyaml-dev \
&& printf "\n" | pecl install yaml \
&& docker-php-ext-enable yaml \
\
&& apt-get install -y \
    fontconfig \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    xfonts-base \
    xfonts-75dpi \
&& curl -L https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb --output ./wkhtml.deb \
&& dpkg -i ./wkhtml.deb \
&& rm -f ./wkhtml.deb \
\
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
\
&& curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
&& apt-get install -y nodejs
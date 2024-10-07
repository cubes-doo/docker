FROM php:8.3-cli

ARG localuser=1000
ARG localgroup=1000

RUN groupadd -f -g $localgroup localgroup \
&& useradd -u $localuser -g $localgroup localuser \
&& mkdir -p /home/localuser \
&& chown -R localuser:localgroup /home/localuser \
&& printf "COLUMNS=1024\nLINES=50\n" | tee /home/localuser/.bashrc \
\
&& apt-get update \
&& apt-get install wget \
&& apt install ca-certificates \
&& apt install libgnutls30 \
&& wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb \
&& dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb \
\
&& docker-php-ext-install -j$(nproc) opcache \
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
&& apt-get install -y libc-client-dev libkrb5-dev \
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
&& docker-php-ext-install -j$(nproc) imap \
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
&& apt-get install -y ffmpeg \
\
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
\
&& curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
&& apt-get install -y nodejs

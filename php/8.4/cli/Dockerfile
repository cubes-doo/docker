FROM php:8.4-cli

ARG localuser=1000
ARG localgroup=1000

# 1. Kreiranje lokalnog korisnika
RUN groupadd -f -g $localgroup localgroup \
    && useradd -u $localuser -g $localgroup localuser \
    && mkdir -p /home/localuser \
    && chown -R localuser:localgroup /home/localuser \
    && printf "COLUMNS=1024\nLINES=50\n" | tee /home/localuser/.bashrc

# 2. Instalacija zvaničnog PHP Extension Installer-a
ADD --chmod=0755 https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

# 3. Instalacija svih PHP ekstenzija
RUN install-php-extensions \
    opcache \
    gd \
    exif \
    bcmath \
    mysqli \
    pdo_mysql \
    zip \
    intl \
    simplexml \
    soap \
    gmp \
    mongodb \
    redis \
    yaml \
    imap

# 4. Instalacija sistemskih zavisnosti za wkhtmltopdf i ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
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
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 5. Preuzimanje libssl1.1 za ARM64 arhitekturu (potrebno za wkhtmltopdf)
RUN wget http://ports.ubuntu.com/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_arm64.deb \
    && dpkg -i libssl1.1_1.1.1f-1ubuntu2_arm64.deb \
    && rm -f libssl1.1_1.1.1f-1ubuntu2_arm64.deb

# 6. Preuzimanje i instalacija wkhtmltopdf za ARM64
RUN curl -L https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_arm64.deb --output ./wkhtml.deb \
    && dpkg -i ./wkhtml.deb \
    && rm -f ./wkhtml.deb

# 7. Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# 8. Node.js (verzija 20.x)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
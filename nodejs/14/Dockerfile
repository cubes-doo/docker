FROM node:14-buster

#make npm -i command possible to run without sudo
RUN apt-get -y update && \
    apt-get -y install man && \
    mkdir /home/node/.npm-packages && \
    chown node: /home/node/.npm-packages && \
    npm config set prefix /home/node/.npm-packages && \
    echo "\nNPM_PACKAGES=/home/node/.npm-packages\n" >> /home/node/.bashrc && \
    echo "export PATH=\"\$PATH:\$NPM_PACKAGES/bin\"\n" >> /home/node/.bashrc && \
    echo "export MANPATH=\"\${MANPATH-\$(manpath)}:\$NPM_PACKAGES/share/man\"\n" >> /home/node/.bashrc && \
    echo "npm config set prefix /home/node/.npm-packages\n" >> /home/node/.bashrc

#add google cloud tools
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && \
    apt-get update -y && \
    apt-get install google-cloud-sdk -y

ENTRYPOINT ["tail", "-f", "/dev/null"]
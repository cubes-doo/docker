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

ENTRYPOINT ["tail", "-f", "/dev/null"]
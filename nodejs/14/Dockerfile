FROM node:14-buster

RUN mkdir /home/node/.npm-global \
    && npm config set prefix '~/.npm-global' \
    && chown -R node: /home/node/.npm-global

ENTRYPOINT ["tail", "-f", "/dev/null"]
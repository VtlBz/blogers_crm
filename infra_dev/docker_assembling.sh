apk update
apk upgrade --no-cache
rm -rf /var/cache/apk/*

addgroup -g 101 -S master
adduser -u 101 -S -h /home/master -G master master
chown master:master -R /home/master

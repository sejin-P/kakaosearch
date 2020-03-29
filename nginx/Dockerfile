FROM launcher.gcr.io/google/nginx1:1.13
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
RUN rm /etc/logrotate.d/nginx
COPY sites-enabled/nginx.logrotate /etc/logrotate.d/
COPY sites-enabled/nginx.conf /etc/nginx/
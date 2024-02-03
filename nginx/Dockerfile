FROM nginx:1.21-alpine


RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY 46DABE79CB0A0888EF34912A40924D45.txt /var/www/
COPY private.key /etc/ssl/
COPY certificate.crt /etc/ssl
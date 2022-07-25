FROM nginx:1.21-alpine


COPY ./docs/_build/html /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
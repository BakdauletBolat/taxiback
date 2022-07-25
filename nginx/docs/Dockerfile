FROM nginx:1.21-alpine


COPY ./_build/html /usr/share/nginx/html

RUN cd /usr/share/nginx/html && mkdir docs
RUN  cp /usr/share/nginx/html/index.html /usr/share/nginx/html/docs/ 
RUN  cp -rf /usr/share/nginx/html/_images/ /usr/share/nginx/html/docs/ 
RUN  cp -rf /usr/share/nginx/html/_static/ /usr/share/nginx/html/docs/ 
RUN  cp -rf /usr/share/nginx/html/modules/ /usr/share/nginx/html/docs/ 


RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/nginx.conf /etc/nginx/conf.d

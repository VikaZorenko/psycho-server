FROM nginx:1.14

COPY ./deploy/nginx/default /etc/nginx/conf.d/default.conf

CMD ["bash", "-c", "nginx -g 'daemon off;'"]

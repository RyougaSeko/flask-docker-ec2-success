FROM nginx:latest

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./server.conf /etc/nginx/conf.d/server.conf


CMD ["nginx", "-g", "daemon off;"]

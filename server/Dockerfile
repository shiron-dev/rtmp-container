FROM alpine:latest

RUN apk update
RUN apk add --no-cache git g++ pcre-dev openssl-dev zlib-dev make
RUN wget https://nginx.org/download/nginx-1.24.0.tar.gz
RUN tar -xvf nginx-1.24.0.tar.gz
RUN git clone https://github.com/arut/nginx-rtmp-module.git
RUN cd nginx-1.24.0 && \
  ./configure \
  --with-http_ssl_module \
  --sbin-path=/usr/sbin/nginx \
  --conf-path=/etc/nginx/nginx.conf \
  --add-module=../nginx-rtmp-module && \
  make && \
  make install
RUN rm -rf nginx-1.24.0.tar.gz nginx-1.24.0 nginx-rtmp-module

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html

RUN mkdir -p /tmp/hls

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

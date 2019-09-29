FROM nginx:1.14-alpine
LABEL maintainer="dyb<dyb0204@gmail.com>"
ENV NGX_DOC_ROOT='/data/web/html/'
ADD index.html ${NGX_DOC_ROOT}
ADD entrypoint.sh /bin/
EXPOSE 80/tcp
#HEALTHCHECK --start-period=5s CMD wget -O - -q http://{IP:-0.0.0.0}
CMD ["/usr/sbin/nginx","-g","daemon off;"]
ENTRYPOINT [ "/bin/entrypoint.sh" ]

#!/bin/sh
#
cat > /etc/nginx/conf.d/default.conf << EOF
server {
        server_name 0.0.0.0;
        listen ${IP:-0.0.0.0}:${PORT:-80};
        root ${NGX_DOC_ROOT:-/usr/share/nginx/html};
}
EOF

exec "$@"

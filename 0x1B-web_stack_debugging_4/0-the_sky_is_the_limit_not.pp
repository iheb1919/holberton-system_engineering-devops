# fixes limits
exec {'fix unlimit':
    command => 'sed -i s/15/1000/ /etc/default/nginx && service nginx restart',
    path    => '/usr/bin/sudo /bin/',
}
# The_sky_is_the_limit_not
exec {'fix':
    command => 'sed -i s/15/1000/ /etc/default/nginx && service nginx restart',
    path    => '/usr/bin/sudo /bin/',
}
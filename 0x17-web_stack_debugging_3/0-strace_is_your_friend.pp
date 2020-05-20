# 0. Strace is your friend
exec {'fconfig':
provider => 'shell',
path     => ['/usr/bin/sudo', '/bin', ],
command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
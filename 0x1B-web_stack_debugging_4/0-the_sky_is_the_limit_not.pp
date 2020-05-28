# fix limit
exec {'fix':
    command => '/usr/bin/sudo /bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 10000\"/g" /etc/default/nginx',
    path    => '/bin',
    provider => shell,
}
exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
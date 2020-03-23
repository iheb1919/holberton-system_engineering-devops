# manifest that kills a procces named killmenow

exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
}
#!/usr/bin/env ruby
match_data = ARGV[0].match(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/)

sender = match_data[1]
receiver = match_data[2]
flags = match_data[3]

puts [sender, receiver, flags].join(',')

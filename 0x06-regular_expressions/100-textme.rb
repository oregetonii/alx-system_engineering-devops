#!/usr/bin/env ruby
#Scan log file, capture sender, receiver, and flags

puts ARGV[0].scan(/from:(\+?\d+|\w+)|to:(\+?\d+|\w+)|flags:([\-?\d:]+)/).join(",")

#!/usr/bin/env ruby
#Sacn log file, capture sender, receiver, and flags

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*)\]/).join(",")

#!/usr/bin/env ruby
#Match a ten-digit phone number

puts ARGV[0].scan(/^[0-9]{10}$/).join

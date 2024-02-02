#!/usr/bin/env ruby
#Match str starting with "h" and ands "n", a char between

puts ARGV[0].scan(/^h.n$/).join

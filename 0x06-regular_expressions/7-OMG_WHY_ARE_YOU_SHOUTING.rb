#!/usr/bin/env ruby
# A regular expression that is matches only capital letters A-Z
puts ARGV[0].scan(/[A-Z]/).join

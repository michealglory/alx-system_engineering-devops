#!/usr/bin/env ruby
# A regular expression that is matches specified pattern
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')

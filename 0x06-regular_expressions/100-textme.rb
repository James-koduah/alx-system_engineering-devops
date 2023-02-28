#!/usr/bin/env ruby


sen = ARGV[0].scan(/from:(\+*\w+)/)
rec = ARGV[0].scan(/to:(\+*\w+)/)
flags = ARGV[0].scan(/flags:(\S*\d:\S*\d:\S*\d:\S*\d:\S*\d)/)

sen.concat([","])
rec.concat([","])
sen.concat(rec, flags)
puts sen.join

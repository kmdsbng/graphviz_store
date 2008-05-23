#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'
require 'base'

run_script {
  dot_file = TEMPDIR + "/#{$cgi['key']}.dot"
  graph_file = TEMPDIR + "/#{$cgi['key']}.gif"

  write_to_dot(dot_file, $cgi['src'], $cgi['title'])
  make_graph(dot_file, graph_file)
  output_graph(graph_file)
}


#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'
require 'base'
require 'db'

def send_404_not_found
  print $cgi.header({'status' => '404 Not Found'})
end

run_script {
  dot_file = DOTDIR + "/" + $cgi['key'].to_s + '.dot'
  graph_file = GRAPHDIR + "/" + $cgi['key'].to_s + '.gif'
  if File.exist?(graph_file)
    output_graph(graph_file)
    return
  end

  record = get_graph_from_db($cgi['key'])
  if record
    write_to_dot(dot_file, record['src'], record['title'])
    make_graph(dot_file, graph_file)
    output_graph(graph_file)
  else
    send_404_not_found()
  end
}


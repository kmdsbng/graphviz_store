#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'
require 'base'

def save(src, title, key)
  $con.transaction {
    sql = <<EOS
insert graph
   set title = '#{title.addslash}',
       src = '#{src.addslash}',
       hash = '#{key.addslash}'
EOS
    $con.query(sql)
  }
end

def make_complete_page_url(key)
  Pathname.new(ENV['REQUEST_URI']).dirname.to_s + '/complete.cgi?key=' + key
end

def redirect_to_complete_page(key)
  print $cgi.header({'status' => '302 Found', 'Location' => make_complete_page_url(key)})
end

run_script {
  key = generate_unique_key()
  dot_file = DOTDIR + "/" + key + ".dot"
  graph_file = GRAPHDIR + "/" + key + ".gif"

  save($cgi['src'], $cgi['title'], key)
  write_to_dot(dot_file, $cgi['src'], $cgi['title'])
  make_graph(dot_file, graph_file)
  redirect_to_complete_page(key)
}


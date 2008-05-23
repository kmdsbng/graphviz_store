require 'date'
require 'cgi'
require 'pp'
require 'pathname'
require 'graph'
require 'db'

DOTDIR = '/home/kmdsbng/www/graphviz/dot'
GRAPHDIR = '/home/kmdsbng/www/graphviz/graph'
THUMBNAILDIR = '/home/kmdsbng/www/graphviz/thumbnail'
TEMPDIR = '/home/kmdsbng/www/graphviz/temp'
FONTFILE = "/home/kmdsbng/work/fonts/ipagp-mona.ttf"
INPUT_CGI_URL = '/graphviz/input.cgi'
GRAPH_CGI_URL = '/graphviz/graph.cgi'
THUMBNAIL_CGI_URL = '/graphviz/graph.cgi'
GRAPHDIR_URL = '/graphviz/graph'
THUMBNAILDIR_URL = '/graphviz/graph'

$cgi = CGI.new

# easy framework that trap exception
def run_script
  begin
    yield
  rescue Exception => x
    print "Content-type: text/plain\r\n\r\n"
    print "Exception: " + x.message + "\r\n\r\n"
    puts x.backtrace
  end
end

CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
def generate_key( length = 30 )
  password = ''
  length.times do
    i = rand( self.class::CHARS.length * (2 ** 8)) / (2**8)
    password += self.class::CHARS[i..i]
  end
  password
end
      
def generate_unique_key( length = 30 )
  $con.transaction {
    while(true)
      key = generate_key(length)
      rset = $con.query("select id from graph where hash = '#{key.addslash}' and valid = 1")
      return key if rset.num_rows == 0
    end
  }
end
      
# graph utility
def convert_to_dot(src, title="")
  header = <<EOS
digraph mygraph {
  node [fontname="#{FONTFILE}", style="setlinewidth(1)", fontsize="10"];
  edge [fontname="#{FONTFILE}", style="bold", fontsize="10"];
  graph [fontname="#{FONTFILE}", labelloc="t"];
  graph [label="#{title}"];
EOS

  footer = <<EOS
}
EOS

  header + src.slice(0, 10000) + footer
end

def write_to_dot(file, body, title)
  File.open(file, 'w') {|f|
    f.write convert_to_dot(body, title)
  }
end

def make_graph(input, output)
  %x(/home/kmdsbng/bin/dot -Tgif #{input} -o #{output})
end

def output_graph(graph_file)
  graph = File.read(graph_file)
  print "Content-type: image/gif\r\n\r\n"
  STDOUT.write graph
end

class String
  def addslash
    self.gsub(/\\/){"\\\\"}.gsub(/\'/){"\\\'"}.gsub(/\"/){"\\\""}
  end
end



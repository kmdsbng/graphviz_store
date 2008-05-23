#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'

require 'base'

run_script {
  graph = get_graph_by_key($cgi['key'])
  key = generate_key()

  body = <<EOS
  <html>
  <head>
  <meta content="text/html; charset=UTF-8" http-equiv="content-type">
  <title>graphviz</title>
  <style>
  table td {
    vertical-align: top;
  }

  table td {
    border: 2px black solid;
  }

  textarea {
    border: 1px black solid;
    font-size: 80%;
  }
  </style>
  </head>
  <body>
  <h1>graphviz</h1>
  <div>Enterキーを押すとグラフが更新されます</div>
  <table>
  <tr>
  <td>
  <form action="save.cgi" method="post">
  <input type="hidden" name="key" value="#{key}" >
  Title:
  <input type="text" name="title" id="title" size="40" value="#{CGI.escapeHTML(graph ? graph.title.to_s : '')}"><br>
  <textarea name="src" rows="23" cols="40" id="src">#{CGI.escapeHTML(graph ? graph.src.to_s : '')}</textarea><br>
  <input type="submit" value="保存" >

  </form>
  </td>
  <td>
  <div id="graph_space">
  </div>
  </td>
  </tr>
  </table>

  <script type="text/javascript" src="js/jquery.js"></script>
  <script type="text/javascript">
  function replace_graph() {
    $('#graph_space').html(
      '<img src="graph_temp.cgi?' + $('form').serialize() + '&t=' + Date.now() + '">'
    )
  }

  // init script
  $(
  function() {
    $('#src').keydown(
      function(event) {
	switch (event.keyCode) {
	  case 13: 
	    replace_graph(); 
	    return true; 
	}
      }
    );

    $('#title').keydown(
      function(event) {
	switch (event.keyCode) {
	  case 13: 
	    replace_graph(); 
	    return false; 
	}
      }
    );

    replace_graph();
  }
  );
  </script>
  </body>
  </html>

EOS

  print $cgi.header
  puts body

}



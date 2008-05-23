#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'
require 'base'
require 'db'



def make_list_content(graphs)

  htmls = []
  graphs.map{|item|
    <<EOS

<div class="list_item">
<table>
      <tr>
      <td width="100">
      <a href="#{item.get_url()}"><img src="#{item.get_thumbnail_url()}" width="100" height="100"></a><br>
      <a href="#{item.get_edit_url()}">コピーを編集</a>
      </td>
      <td width="200">
	#{item.title.to_s.empty? ? 'No title' : CGI.escapeHTML(item.title)}
      </td>
      </tr>
</table>
</div>

EOS
  }.each_with_index{|e,i|
    htmls << e
    if i % 2 != 0
      htmls << '<div style="clear: both"></div>'
    end

  }

  htmls.join

end


run_script {
  graphs = get_recent_graphs()
  list_content = make_list_content(graphs)

  print $cgi.header

  body = <<EOS
  <html>
  <head>
  <meta content="text/html; charset=UTF-8" http-equiv="content-type">
  <title>graphviz</title>
  <style>
  table td {
    vertical-align: top;
  }

  table {
    border: 2px black solid;
    margin: 2px;
  }

  textarea {
    border: 1px black solid;
    font-size: 80%;
  }

  div.list_item {
    float: left;
  }

  </style>
  </head>
  <body>
  <h1>graphviz</h1>
  <div>
    <a href="input.cgi">グラフを新規作成</a>
  </div>
  <br><br>
  <div style="margin: 2px; width: 310px; border: 2px black solid; padding: 2px;">
    最近のグラフ
  </div>

  #{list_content}

  <div style="clear: both"></div>


  </body>
</html>

EOS

  puts body

}



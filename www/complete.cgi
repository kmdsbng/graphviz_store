#!/usr/local/bin/ruby -Ku
$: << '/home/kmdsbng/graph/lib'
require 'base'

run_script {
  print $cgi.header

  body = <<EOS
  <html>
  <head>
  <meta content="text/html; charset=UTF-8" http-equiv="content-type">
  <title>graphviz</title>
  </head>
  <body>
  <div>
  グラフを保存しました<br><br>

  <a href="#{Graph.get_url($cgi['key'])}" >グラフ画像</a>: 作成したグラフ画像のURLです<br>
  <a href="#{Graph.get_edit_url($cgi['key'])}" >グラフを元に新規作成</a>: このグラフをもとに新しいグラフを編集します<br><br>
  <a href="./">トップに戻る</a>
  </div>

  <div>
    <img src="#{Graph.get_url($cgi['key'])}" style="border: 2px black solid">
  </div>
  </body>
  </html>

EOS

  puts body
}


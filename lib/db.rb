require 'mysql'
require 'const'

$con = Mysql.connect('localhost', DB_USER, DB_PASS)
$con.query 'use kmdsbng_graph'

class Mysql
  def transaction
    unless @in_transaction
      @in_transaction = true
      rollbacked = false
      begin
        query('begin')
        yield self
      rescue Exception => x
        query('rollback')
        rollbacked = true
        raise x
      ensure
        query('commit') unless rollbacked
        @in_transaction = false
      end 
    else
      yield self
    end
  end

end

def get_graph_from_db(key)
  $con.transaction {
    rset = $con.query("select * from graph where valid = 1 and hash = '#{key}'")
    while (row = rset.fetch_hash)
      return row
    end
  }
  return nil
end

def get_graph_by_key(key)
  Graph.new(get_graph_from_db(key))
end

def get_recent_graphs
  result = []
  $con.transaction {
    rset = $con.query("select * from graph where valid = 1 order by updated_at desc limit 10")
    while (row = rset.fetch_hash)
      result << Graph.new(row)
    end
  }
  return result
end



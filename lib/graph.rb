class Graph

  attr_accessor :id, :hash, :src, :title

  def initialize(row)
    row ||= {}
    [:id, :hash, :src, :title].each {|e|
      self.send(e.to_s + '=', row[e.to_s])
    }
  end

  def key
    @hash
  end

  def get_url
    self.class.get_url(key)
  end

  def get_thumbnail_url
    self.class.get_thumbnail_url(key)
  end

  def get_edit_url
    self.class.get_edit_url(key)
  end

  class << self
    def get_url(key)
      GRAPHDIR_URL + "/#{key}.gif"
    end

    def get_thumbnail_url(key)
      GRAPHDIR_URL + "/#{key}.gif"
    end

    def get_edit_url(key)
      INPUT_CGI_URL + "?key=#{key}"
    end
  end
end




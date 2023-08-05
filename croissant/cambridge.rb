require 'open-uri'
require 'nokogiri'
word = ARGV.join("-")
d = Nokogiri::HTML.parse(open('https://dictionary.cambridge.org/us/dictionary/french-english/'+word))
puts d.css(".dictionary")[0].text

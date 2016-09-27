# require 'mini_magick'
require 'rtesseract'

RTesseract.configure do |config|
  config.processor = "mini_magick"
end

citation = RTesseract.new('citation-examples/1.png')
puts '*****************************'
p citation
puts '*****************************'
p citation.to_s
puts '*****************************'

# citation2 = RTesseract.new('citation-examples/BluebookSessionWorksheet.pdf')
# p citation2.to_s
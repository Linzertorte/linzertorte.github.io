(1..17).each do |i|
  system("python paella.py goldb1ch%02d.txt > goldb1ch%02d.html"%[i,i])
end

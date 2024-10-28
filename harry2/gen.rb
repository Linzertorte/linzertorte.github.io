(1..18).each do |i|
  system("python paella.py goldb2ch%02d.txt > gold%02d.html"%[i,i])
end

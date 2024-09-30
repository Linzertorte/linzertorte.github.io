(1..17).each do |i|
  system("python paella.py gold%02d.txt > gold%02d.html"%[i,i])
end

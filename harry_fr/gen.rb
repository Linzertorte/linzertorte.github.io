#(1..17).each do |i|
i = 2
  system("python paella.py b2ch%02d.txt > goldb2ch%02d.html"%[i,i])
  system("python tiramisu.py b2ch%02d.txt > b2ch%02d.csv"%[i,i])
#end

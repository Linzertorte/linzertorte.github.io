#(1..17).each do |i|
i = 1
  system("python paella.py goldb1ch%02d.txt > goldb1ch%02d.html"%[i,i])
  system("python tiramisu.py goldb1ch%02d.txt > b1ch%02d.csv"%[i,i])
#end

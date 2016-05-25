set terminal png size 800,600
set xdata time
# eg. May-08-21:02:03
set timefmt '%Y-%m-%d %H:%M:%S'
set output '/var/www/html/__xuanran001__/xuanran001_perf.png'
# time range must be in same format as data file
set xrange [time(0) - 12*3600 + 8*3600 : time(0) + 8*3600] #reverse
set yrange [0:10]
set grid
set xlabel 'Past 24hr'
set ylabel 'Celsius/Persent'
set title 'Download time'
set key left box
set datafile missing
set datafile separator ","
plot '/var/www/html/__xuanran001__/xuanran001_perf.log' using 1:8 index 0 title 'time_total' with points pointtype 13

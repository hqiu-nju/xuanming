### script for preparing data for FAST on ska machine

### conda activate FRB on sci1
### this step converts all psrfits to filterbanks first, data is tscrunched
python3 fits2fil.py /data-cold/not-backup/h.qiu/fast/obs1_symlink/FRB_210407_tracking-M01_*.fits -n 5232 -o fast_lowerband_bin4 -N 100 -b 4

python3 fits2fil.py /data-cold/not-backup/h.qiu/fast/obs1_symlink/FRB_210407_tracking-M01_*.fits --ch1 5232 -n 2960 -o fast_upperband_bin2 -N 100 -b 2

#### produce iqrm fitted filterbanks
x=0; while  [ $x -le 5 ];
iqrm_apollo_cli -i ../filterbanks_20211016/fast_lowerband_bin4_${x}.fil -o iqrm_lo_${x}.fil -f 5238 -s 12571200 -r constant -k 1
$(( x++ )); done



##### run rfifind on data

# rfifind -filterbank -o prep -blocks 64 fast_lowerband_bin4_0.fil

x=0; while  [ $x -le 5 ];
do rfifind -filterbank -o process_211016_lo_bin4_${x} -blocks 64 fast_lowerband_bin4_${x}.fil
$(( x++ )); done



x=0; while  [ $x -le 5 ];
do rfifind -psrfits -o process_211016_lo_bin4_${x} -blocks 64 fast_lowerband_bin4_${x}.fits
$(( x++ )); done

x=0; while  [ $x -le 5 ];
do python3 fil2fits.py fast_lowerband_bin4_${x}.fil -o fast_lowerband_bin4_${x}
$(( x++ )); done


x=0; while  [ $x -le 5 ];
do rfifind -filterbank -o process_211016_hi_bin2_${x} -blocks 64 fast_upperband_bin2_${x}.fil
$(( x++ )); done



x=0; while  [ $x -le 5 ];
do rfifind -psrfits -o process_211016_hi_bin2_${x} -blocks 64 fast_upperband_bin2_${x}.fits
$(( x++ )); done

x=0; while  [ $x -le 5 ];
do python3 fil2fits.py fast_upperband_bin2_${x}.fil -o fast_upperband_bin2_${x}
$(( x++ )); done

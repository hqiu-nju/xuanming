#!/bin/bash
#
#SBATCH --job-name=iqrm
#SBATCH --output=iqrm
#
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1

#SBATCH --time=1:00:00
#SBATCH --mem-per-cpu=8g

source /home/hqiu/psrhome_2019-03.sh
alias iqrm_apollo_cli=/fred/oz002/hqiu/iqrm_apollo/build/iqrm_apollo/iqrm_apollo_cli


export PATH=/fred/oz002/hqiu/iqrm_apollo/build/iqrm_apollo/:$PATH

x=0; while  [ $x -le 11 ];
do iqrm_apollo_cli -i ../filterbanks_20220123/fast_lowerband_bin4_${x}.fil -o iqrm_lo_${x}.fil -f 5238 -s 3276800 -r constant -k 1
$(( x++ )); done


x=0; while  [ $x -le 11 ];
do iqrm_apollo_cli -i ../filterbanks_20220123/fast_upperband_bin2_${x}.fil -o iqrm_hi_${x}.fil -f 2960 -s 3276800 -r constant -k 1
$(( x++ )); done

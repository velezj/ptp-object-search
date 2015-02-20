SEED=$7
GSL_RNG_SEED=$SEED /home/velezj/projects/gits/p2l-system/build/bin/p2l-rawseeds-experiments-runner --world=$1 --model=$2 --planner=$3 --add-empty-regions=0 --centered-window=0 --initial-window-fraction=$4 --goal-fraction-found=$5 --experiment-id=$6 --seed=$SEED 
#echo "SEED $SEED $1 $2 $3 $4 $5 $6 $7"


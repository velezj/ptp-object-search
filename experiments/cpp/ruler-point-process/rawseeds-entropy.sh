
ts=`date +%s.%N`
hst=`hostname`

for (( id=1; id < 15; id++ ))
do
    
    SEED=`date +%N`
    GSL_RNG_SEED=$SEED /home/velezj/projects/gits/p2l-system/build/bin/p2l-rawseeds-experiments-runner --world=rawseeds::biccoca_2009_02_27a --model=rawseeds::ruler_2d_mean_008 --planner=rawseeds::coverage_planner_10grid --add-empty-regions=0 --centered-window=1 --initial-window-fraction=0.5 --goal-fraction-found=1.0 --experiment-id=jj2/coverage/01 --seed=$SEED 

done

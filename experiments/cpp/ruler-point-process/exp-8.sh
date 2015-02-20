
ts=`date +%s.%N`
hst=`hostname`

for (( id=1; id < 100; id++ ))
do
    experiment_dir="/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/experiment-8/sweep-$hst-$ts/$id"
    SEED=`date +%N`
    echo $experiment_dir
    mkdir -p $experiment_dir
    GSL_RNG_SEED=$SEED /home/velezj/projects/gits/p2l-system/build/bin/p2l-planner-core-experiment-8 $experiment_dir $SEED | tee $experiment_dir/out.out
    
done


from multiprocessing.pool import ThreadPool
import subprocess
import itertools

def run_f_centered( args ):
    world, model, planner, init, goal, trial = args
    
    eid = "density/" + world + "/" + model + "/" + planner + "/" + str(init) + "/" + str(goal) + "/01" 
    cmd = "/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/density-trial.sh " + world + " " + model + " " + planner + " " + str(init) + " " + str(goal) + " " + eid
    ret = 0
    ret = subprocess.call(cmd, shell=True, cwd="/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/")


    with open( "density-experiment.trace", "a+") as trace_file:
        trace_file.write( "finished: " + str(args) + "  RET=" + str(ret) + "\n")
        trace_file.flush()



def run_f_noncentered( args ):
    world, model, planner, init, goal, trial = args
    
    eid = "density/" + world + "/noncentered/" + model + "/" + planner + "/" + str(init) + "/" + str(goal) + "/01" 
    cmd = "/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/density-trial-noncentered.sh " + world + " " + model + " " + planner + " " + str(init) + " " + str(goal) + " " + eid
    ret = 0
    ret = subprocess.call(cmd, shell=True, cwd="/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/")


    with open( "density-experiment.trace", "a+") as trace_file:
        trace_file.write( "finished: " + str(args) + "  RET=" + str(ret) + "\n")
        trace_file.flush()


def run_f_seeded_centered( args ):
    world, model, planner, init, goal, trial, seed = args
    
    eid = "density/" + world + "/" + model + "/" + planner + "/" + str(init) + "/" + str(goal) + "/01" 
    cmd = "/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/density-trial-seeded.sh " + world + " " + model + " " + planner + " " + str(init) + " " + str(goal) + " " + eid + " " + str(seed)
    ret = 0
    ret = subprocess.call(cmd, shell=True, cwd="/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/")


    with open( "density-experiment.trace", "a+") as trace_file:
        trace_file.write( "finished: " + str(args) + "  RET=" + str(ret) + "\n")
        trace_file.flush()



def run_f_seeded_noncentered( args ):
    world, model, planner, init, goal, trial, seed = args
    
    eid = "density/" + world + "/noncentered/" + model + "/" + planner + "/" + str(init) + "/" + str(goal) + "/01" 
    cmd = "/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/density-trial-seeded-noncentered.sh " + world + " " + model + " " + planner + " " + str(init) + " " + str(goal) + " " + eid + " " + str(seed)
    ret = 0
    ret = subprocess.call(cmd, shell=True, cwd="/home/velezj/projects/gits/p2l-system/experiments/cpp/ruler-point-process/")


    with open( "density-experiment.trace", "a+") as trace_file:
        trace_file.write( "finished: " + str(args) + "  RET=" + str(ret) + "\n")
        trace_file.flush()



def run_f( args ):
    world, model, planner, init, goal, trial, centered = args
    if centered:
        run_f_centered( (world,model,planner,init,goal,trial) )
    else:
        run_f_noncentered( (world,model,planner,init,goal,trial) )

def run_f_trial_seeded( args ):
    world, model, planner, init, goal, trial, centered = args
    if centered:
        run_f_seeded_centered( (world,model,planner,init,goal,trial,trial + 30000) )
    else:
        run_f_seeded_noncentered( (world,model,planner,init,goal,trial,trial + 30000) )


if __name__ == "__main__":

    # planners       = ["rawseeds::one_action_entropy_reduction_planner_002_10grid",
    #                   "rawseeds::shortest_path_next_planner_003_10grid",
    #                   "rawseeds::coverage_planner_10grid"]
    # worlds         = ["rawseeds::random-subset-0.1::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.2::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.3::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.4::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.5::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.6::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.7::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.8::biccoca_2009_02_27a",
    #                   "rawseeds::random-subset-0.9::biccoca_2009_02_27a",
    #                   "rawseeds::biccoca_2009_02_27a"]

    planners       = ["rawseeds::one_action_entropy_reduction_planner_002_10grid",
                      "rawseeds::shortest_path_next_planner_003_10grid"]
    worlds         = ["rawseeds::biccoca_2009_02_27a"]

    
    models         = ["rawseeds::ruler_2d_mean_lengthprior_008"]
    #init_fractions = [ 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.55, 0.6, 0.65, 0.7, 0.8, 0.85, 0.9, 0.95 ]
    init_fractions = [ 0.5 ]
    goal_fractions = [ 1.0 ]
    centered = [ True ]
    trials_per_setting = 2
    
    num_processes = 10
    
    pool = ThreadPool( num_processes )
    


    # run the trials
    pool.map( run_f_trial_seeded, itertools.product(worlds,models,planners,init_fractions,goal_fractions, range(trials_per_setting), centered ) )

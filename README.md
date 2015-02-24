# ptp-object-search
Javier Velez Plan-To-Perceive Object Search System core


# Building from Source

## Getting the Source and initializing submodules

	git clone http://github.com/velezj/ptp-object-search.git
	git submodule init
	git submodule update --rebase

## Building (PODS interface)

The sotware is a collection of PODS so we can simply create our build directory and type 'make'

		cd ptp-object-search/
		mkdir -p build
		cd pods
		make


# Running the experiments

## Frist, start Couchdb for storing the experiment results

In the first terminal:
	cd ptp-object-search/build/bin
	./couchdb

Select the world, model and planner wanted (these are named) as well
as an experiment ID.  For example, I will choose:

- `world=rawseeds::biccoca_2009_02_27a`
- `model=rawseeds::ruler_2d_mean_008`
- `planner=rawseeds::one_action_entropy_reduction_planner_002_1e3grid`
- `ID=test-exp-001`

run the experiment runner with chosen parameters

	cd ptp-object-search/build/bin
	./p2l-rawseeds-experiments-runner
		--world=rawseeds::biccoca_2009_02_27a
		--model=rawseeds::ruler_2d_mean_008
		--planner=rawseeds::one_action_entropy_reduction_planner_002_1e3grid
		--experiment-id=test-exp-001

There are many more parameters which teh runner takes as command line
arguments, see `./p2l-rawseeds-experiments-runner --help` for a
complete list.

The registered worlds, models and planners can be found inside
`ptp-object-search/pods/ptp-object-search-experiments/src/register.cpp`


# Hacking away at the code

# References


# ptp-object-search
Javier Velez Plan-To-Perceive Object Search System core


# Building from Source

## Getting the Source and initializing submodules

	git clone http://github.com/velezj/ptp-object-search.git
	git submodule init
	git submodule update --rebase

## Initial Build (requires manual edits _ewww_)

1. Edit ptp-object-search/pods/tobuild.txt and move the
   ptp-object-search-planner-core to be below the
   ptp-object-search-ruler-point-process line.
   
1. Edit the
   `ptp-object-search/pods/ptp-object-search-planner-core/CMakeLists.txt`
   to remove the point process depedencies and the planner that uses
   them.
   
   - remove `src/one_action_entropy_reduction_planner.cpp` from
     `add_library(` section
   - remove `src/one_action_entropy_reduction_planner.hpp` from
     `pods_install_headers` section
   - remove `p2l-ruler-point-process` from
     `pods_use_pkg_config_packages`
   - remove `p2l-igmm-point-process` from
     `pods_use_pkg_config_packages`
   - remove `p2l-ruler-point-process` from
     `pods_install_pkg_config_file` `REQUIRES` section
   - remove `p2l-igmm-point-process` from
     `pods_install_pkg_config_file` `REQUIRES` section
	 
1. First build. This _will fail_ but it will get a version of the
   ruler and IGMM point process libraries built so they can be picked
   up by the planner core

1. Edit back in the dependencies you removed. Easiest just to checkout
   the `ptp-object-search/pods/ptp-object-search-planner-core/CMakeLists.txt`
   again and discard the changes you made

		cd ptp-object-search/pods/ptp-object-search-planner-core/
		git checkout CMakeLists.txt

1. Edit back the order for building ptp-object-search-planner-core

		git checkout -- ptp-object-search/pods/tobuild.txt

1. Second build. This should all build with no errors.
		

# Running the experiments

# Hacking away at the code

# References


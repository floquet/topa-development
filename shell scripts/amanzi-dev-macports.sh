#
# Set ASCEM_HOME
#
export ASCEM_HOME=/ascem

#
# Set AMANZI_HOME
#
export AMANZI_HOME=${ASCEM_HOME}/amanzi

#
# Set Amanzi Machine/System Information
#
. ${AMANZI_HOME}/tools/init/amanzi-machine-env.sh

#
# Load modules on Mac PowerBook
#
module load amanzi/gcc-macports/1.0

#
# Amanzi Installation
#
export AMANZI_INSTALL_DIR=${ASCEM_HOME}/amanzi/install/${AMANZI_SYS_path}/devel
#export AMANZI_INSTALL_DIR=${ASCEM_HOME}/amanzi/install/${AMANZI_SYS_path}/release-0.83
export AMANZI_EXE=${AMANZI_INSTALL_DIR}/bin/amanzi
export AMANZI_XSD=${AMANZI_INSTALL_DIR}/bin/amanzi.xsd

#
# Macports MPI
# - probably stick this in a module
#
export MPI_HOME=/opt/local


#
# Set parameters for running verfication / benchmark tests
#
export AMANZI_RUN_PARALLEL=yes
export AMANZI_MPI_EXEC=mpirun
export AMANZI_MPI_MAXPROCS=6
export AMANZI_MPI_NP=6
export AMANZI_MPI_NUMPROCS_FLAG=-n

#
# Benchmark Simulators
#
export AT123DAT_EXE=$ASCEM_HOME/AT123D/AT123D-AT/at123dat

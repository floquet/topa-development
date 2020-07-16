# =====================================================================
#
# .bashrc: OS and Version information for use with builds
#
# Contacts: David Moulton (moulton@lanl.gov)
# Date:     March 26, 2013
#
# =====================================================================

#
#  Set base OS information
#
export AMANZI_OS_type=`uname -s`
export AMANZI_OS_arch=`uname -m`

#
#  Which OS and version are we running:
#
if [ $AMANZI_OS_type == "Linux" ]; then
    if [ -f /etc/redhat-release ]; then
	export AMANZI_OS_vendor=RHEL
	export AMANZI_OS_version=`cat /etc/redhat-release | sed -e 's/[^0-9]*//g' | sed -e 's/^\(.\{1\}\)/\1./'`
    elif [ -f /etc/SuSE-release ]; then
	export AMANZI_OS_vendor=SUSE
	VERSION=`grep VERSION /etc/SuSE-release | sed -e 's/.*= //'`
	PATCHLEVEL=`grep PATCHLEVEL /etc/SuSE-release | sed -e 's/.*= //'`
	export AMANZI_OS_version=${VERSION}.${PATCHLEVEL}
    elif [ -f /etc/lsb-release ]; then
    # Note Hopper is a SUSE system and has an /etc/lsb-release file so order of tests is important
	DISTRIB_ID=`grep DISTRIB_ID /etc/lsb-release | sed -e 's/.*=//'`
	if [ ${DISTRIB_ID} == "Ubuntu" ]; then
	    export AMANZI_OS_vendor=Ubuntu
	    export AMANZI_OS_version=`cat /etc/lsb-release | grep DISTRIB_RELEASE | sed -e 's/.*=//'`
	fi
    fi
elif [ $AMANZI_OS_type == "Darwin" ]; then
    export AMANZI_OS_vendor=OSX
    export AMANZI_OS_version=`sw_vers -productVersion`
fi

#
#  Should we create an AMANZI_OS_path ?
#

#
#  Installations will use the AMANZI_SYS_path constructed from the OS information
#
#  NB: If it is one of the special institutional systems we use the hostname
#
if [ -n "${NERSC_HOST}" ]; then
    if [ ${NERSC_HOST} == "hopper" ]; then
	export AMANZI_SYS_path='hopper'
    else
	echo "Unknown NERSC Host: ${NERSC_HOST}"
    fi
else
    export AMANZI_SYS_path=${AMANZI_OS_vendor}-${AMANZI_OS_version}-${AMANZI_OS_arch}
fi

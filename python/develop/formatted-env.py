# https://stackoverflow.com/questions/4906977/how-do-i-access-environment-variables-from-python
import os # environment variables

print( "print without formatting: key, ':', os.environ[key]" )
for key in os.environ: print( key, ':', os.environ[ key ] )

print( "\nprint with formatting: key, ':', os.environ[key]" )
for key in os.environ: print( '{:>30} {:<4} {:}'.format( key, ':', os.environ[ key ] ) )

print( "\nprint with nested loop" )
for variable, value in os.environ.items( ):
    print( variable, value )
# dantopa@Lax-Millgram:develop $ date
# Tue Nov 20 21:22:44 MST 2018

# dantopa@Lax-Millgram:develop $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/develop

# dantopa@Lax-Millgram:develop $ python --version
# Python 3.6.7

# dantopa@Lax-Millgram:develop $ py formatted-env.py
# print without formatting: key, ':', os.environ[key]
# bold :
# master : /Users/dantopa/Documents/GitHub/LLNL-master-open-mpi
# partition : log-in
# HOSTNAME : MacBookPro11,3
# TERM_PROGRAM : Apple_Terminal
# gflags : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
# my_log : /Lax-Millgram/log-in-MacBookPro11,3/uname_variables.txt
# SHELL : /bin/bash
# TERM : xterm-256color
# u_Tlaltecuhtli : /Volumes/Tlaltecuhtli/
# fortran_compiler_mpi_cray : ftn
# TMPDIR : /var/folders/k6/5wm3hql10qv_g1ymbplcd0zr0000gr/T/
# fortran_compiler_caf : caf
# Apple_PubSub_Socket_Render : /private/tmp/com.apple.launchd.zEpO0z2yuy/Render
# file_lstopo : /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-lstopo.pdf
# TERM_PROGRAM_VERSION : 400
# vault : /Lax-Millgram/log-in-MacBookPro11,3/configure
# OLDPWD : /Users/dantopa/Documents/GitHub/topa-development/python
# TERM_SESSION_ID : 2726AC2A-0C0F-4B48-B769-45AFEE1536DC
# os : darwin
# dropbox : /Users/dantopa/Dropbox
# nagflags : -g -C=all -colour -compatible -f2008 -free -gc -gline -info -nan -O2 -pg -time -v -V
# gflags48 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all
# myssh : ssh -l -XY dantopa
# normal :
# USER : dantopa
# moniker : dantopa
# SSH_AUTH_SOCK : /private/tmp/com.apple.launchd.wxsCQuHAIM/Listeners
# bitbucket : /Users/dantopa/Documents/Bitbucket
# host_name : Lax-Millgram
# gflags45 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens
# PATH : /opt/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/local/bin:/Library/TeX/texbin:/opt/X11/bin
# scratch : /Volumes/Tlaltecuhtli/
# gflags47 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination
# PWD : /Users/dantopa/Documents/GitHub/topa-development/python/develop
# mySpack : /Users/dantopa/Applications/spack.macbook
# file_hwloc : /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-hwloc-ls.txt
# LANG : en_US.UTF-8
# github : /Users/dantopa/Documents/GitHub
# fortran_compiler_gnu : gfortran
# ego : /Lax-Millgram
# bash_scripts : /Users/dantopa/Documents/GitHub/LLNL-bash
# XPC_FLAGS : 0x0
# PS1 : \[\033[00;35m\]\u\[\033[00m\]@\[\033[00;35m\]\H\[\033[00m\]:\[\033[00;33m\]\W\[\033[00m\] $\033[00;36m
# XPC_SERVICE_NAME : 0
# SHLVL : 1
# HOME : /Users/dantopa
# id : /Lax-Millgram/log-in-MacBookPro11,3
# repos : /Users/dantopa/Documents
# cflags : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived -fcoarray=lib
# me : dantopa@lanl.gov
# LOGNAME : dantopa
# core : /Users/dantopa/Documents/GitHub/LLNL-bash/core-scripts
# crayflags : -g -fbacktrace
# gflags4 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5
# gflags5 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto
# gflags6 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra
# DISPLAY : /private/tmp/com.apple.launchd.p9bXjXLI3d/org.macosforge.xquartz:0
# gflags7 : -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
# short_name : MacBookPro11,3
# SECURITYSESSIONID : 186a7
# fortran_compiler_mpi_gnu : mpif90
# bash_file : .profile
# _ : /opt/local/bin/python
# __CF_USER_TEXT_ENCODING : 0x1F8:0x0:0x0
# __PYVENV_LAUNCHER__ : /opt/local/bin/python
#
# print with formatting: key, ':', os.environ[key]
#                           bold :
#                         master :    /Users/dantopa/Documents/GitHub/LLNL-master-open-mpi
#                      partition :    log-in
#                       HOSTNAME :    MacBookPro11,3
#                   TERM_PROGRAM :    Apple_Terminal
#                         gflags :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
#                         my_log :    /Lax-Millgram/log-in-MacBookPro11,3/uname_variables.txt
#                          SHELL :    /bin/bash
#                           TERM :    xterm-256color
#                 u_Tlaltecuhtli :    /Volumes/Tlaltecuhtli/
#      fortran_compiler_mpi_cray :    ftn
#                         TMPDIR :    /var/folders/k6/5wm3hql10qv_g1ymbplcd0zr0000gr/T/
#           fortran_compiler_caf :    caf
#     Apple_PubSub_Socket_Render :    /private/tmp/com.apple.launchd.zEpO0z2yuy/Render
#                    file_lstopo :    /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-lstopo.pdf
#           TERM_PROGRAM_VERSION :    400
#                          vault :    /Lax-Millgram/log-in-MacBookPro11,3/configure
#                         OLDPWD :    /Users/dantopa/Documents/GitHub/topa-development/python
#                TERM_SESSION_ID :    2726AC2A-0C0F-4B48-B769-45AFEE1536DC
#                             os :    darwin
#                        dropbox :    /Users/dantopa/Dropbox
#                       nagflags :    -g -C=all -colour -compatible -f2008 -free -gc -gline -info -nan -O2 -pg -time -v -V
#                       gflags48 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all
#                          myssh :    ssh -l -XY dantopa
#                         normal :
#                           USER :    dantopa
#                        moniker :    dantopa
#                  SSH_AUTH_SOCK :    /private/tmp/com.apple.launchd.wxsCQuHAIM/Listeners
#                      bitbucket :    /Users/dantopa/Documents/Bitbucket
#                      host_name :    Lax-Millgram
#                       gflags45 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens
#                           PATH :    /opt/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/local/bin:/Library/TeX/texbin:/opt/X11/bin
#                        scratch :    /Volumes/Tlaltecuhtli/
#                       gflags47 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination
#                            PWD :    /Users/dantopa/Documents/GitHub/topa-development/python/develop
#                        mySpack :    /Users/dantopa/Applications/spack.macbook
#                     file_hwloc :    /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-hwloc-ls.txt
#                           LANG :    en_US.UTF-8
#                         github :    /Users/dantopa/Documents/GitHub
#           fortran_compiler_gnu :    gfortran
#                            ego :    /Lax-Millgram
#                   bash_scripts :    /Users/dantopa/Documents/GitHub/LLNL-bash
#                      XPC_FLAGS :    0x0
#                            PS1 :    \[\033[00;35m\]\u\[\033[00m\]@\[\033[00;35m\]\H\[\033[00m\]:\[\033[00;33m\]\W\[\033[00m\] $\033[00;36m
#               XPC_SERVICE_NAME :    0
#                          SHLVL :    1
#                           HOME :    /Users/dantopa
#                             id :    /Lax-Millgram/log-in-MacBookPro11,3
#                          repos :    /Users/dantopa/Documents
#                         cflags :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived -fcoarray=lib
#                             me :    dantopa@lanl.gov
#                        LOGNAME :    dantopa
#                           core :    /Users/dantopa/Documents/GitHub/LLNL-bash/core-scripts
#                      crayflags :    -g -fbacktrace
#                        gflags4 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5
#                        gflags5 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto
#                        gflags6 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra
#                        DISPLAY :    /private/tmp/com.apple.launchd.p9bXjXLI3d/org.macosforge.xquartz:0
#                        gflags7 :    -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
#                     short_name :    MacBookPro11,3
#              SECURITYSESSIONID :    186a7
#       fortran_compiler_mpi_gnu :    mpif90
#                      bash_file :    .profile
#                              _ :    /opt/local/bin/python
#        __CF_USER_TEXT_ENCODING :    0x1F8:0x0:0x0
#            __PYVENV_LAUNCHER__ :    /opt/local/bin/python
# print with nested loop
# bold
# master /Users/dantopa/Documents/GitHub/LLNL-master-open-mpi
# partition log-in
# HOSTNAME MacBookPro11,3
# TERM_PROGRAM Apple_Terminal
# gflags -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
# my_log /Lax-Millgram/log-in-MacBookPro11,3/uname_variables.txt
# SHELL /bin/bash
# TERM xterm-256color
# u_Tlaltecuhtli /Volumes/Tlaltecuhtli/
# fortran_compiler_mpi_cray ftn
# TMPDIR /var/folders/k6/5wm3hql10qv_g1ymbplcd0zr0000gr/T/
# fortran_compiler_caf caf
# Apple_PubSub_Socket_Render /private/tmp/com.apple.launchd.zEpO0z2yuy/Render
# file_lstopo /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-lstopo.pdf
# TERM_PROGRAM_VERSION 400
# vault /Lax-Millgram/log-in-MacBookPro11,3/configure
# OLDPWD /Users/dantopa/Documents/GitHub/topa-development/python
# TERM_SESSION_ID 2726AC2A-0C0F-4B48-B769-45AFEE1536DC
# os darwin
# dropbox /Users/dantopa/Dropbox
# nagflags -g -C=all -colour -compatible -f2008 -free -gc -gline -info -nan -O2 -pg -time -v -V
# gflags48 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all
# myssh ssh -l -XY dantopa
# normal
# USER dantopa
# moniker dantopa
# SSH_AUTH_SOCK /private/tmp/com.apple.launchd.wxsCQuHAIM/Listeners
# bitbucket /Users/dantopa/Documents/Bitbucket
# host_name Lax-Millgram
# gflags45 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens
# PATH /opt/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/local/bin:/Library/TeX/texbin:/opt/X11/bin
# scratch /Volumes/Tlaltecuhtli/
# gflags47 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination
# PWD /Users/dantopa/Documents/GitHub/topa-development/python/develop
# mySpack /Users/dantopa/Applications/spack.macbook
# file_hwloc /Lax-Millgram/log-in-MacBookPro11,3/Lax-Millgram-log-in-hwloc-ls.txt
# LANG en_US.UTF-8
# github /Users/dantopa/Documents/GitHub
# fortran_compiler_gnu gfortran
# ego /Lax-Millgram
# bash_scripts /Users/dantopa/Documents/GitHub/LLNL-bash
# XPC_FLAGS 0x0
# PS1 \[\033[00;35m\]\u\[\033[00m\]@\[\033[00;35m\]\H\[\033[00m\]:\[\033[00;33m\]\W\[\033[00m\] $\033[00;36m
# XPC_SERVICE_NAME 0
# SHLVL 1
# HOME /Users/dantopa
# id /Lax-Millgram/log-in-MacBookPro11,3
# repos /Users/dantopa/Documents
# cflags -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived -fcoarray=lib
# me dantopa@lanl.gov
# LOGNAME dantopa
# core /Users/dantopa/Documents/GitHub/LLNL-bash/core-scripts
# crayflags -g -fbacktrace
# gflags4 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5
# gflags5 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto
# gflags6 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra
# DISPLAY /private/tmp/com.apple.launchd.p9bXjXLI3d/org.macosforge.xquartz:0
# gflags7 -g -ffpe-trap=denormal,invalid,zero -fbacktrace -Wall -Wextra -Waliasing -Wsurprising -Wimplicit-procedure -Wintrinsics-std -Og -pedantic -fmax-errors=5 -fcheck=all -fcheck=do -fcheck=pointer -fno-protect-parens  -Wfunction-elimination -faggressive-function-elimination -Wc-binding-type -Wrealloc-lhs-all -Wuse-without-only -fdiagnostics-color=auto  -Wconversion-extra  -finit-derived
# short_name MacBookPro11,3
# SECURITYSESSIONID 186a7
# fortran_compiler_mpi_gnu mpif90
# bash_file .profile
# _ /opt/local/bin/python
# __CF_USER_TEXT_ENCODING 0x1F8:0x0:0x0
# __PYVENV_LAUNCHER__ /opt/local/bin/python

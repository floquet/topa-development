# https://stackoverflow.com/questions/739993/how-can-i-get-a-list-of-locally-installed-python-modules

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

# l127914@pn1249300.lanl.gov:alpha $ py installs.py
# Traceback (most recent call last):
#   File "installs.py", line 3, in <module>
#     import pip
# ModuleNotFoundError: No module named 'pip'

# l127914@pn1249300.lanl.gov:alpha $ date
# Wed Dec 19 15:26:44 MST 2018

# l127914@pn1249300.lanl.gov:alpha $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/ppt/alpha

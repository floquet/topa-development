class C(object):
    def __init__(self):
        self._file_name = None

    @property
    def file_name(self):
        """I'm the 'file_name' property."""
        print("getter of file_name called")
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        print("setter of file_name called")
        self._file_name = value

    @file_name.deleter
    def file_name(self):
        print("deleter of file_name called")
        del self._file_name

c = C()
c.file_name = "file.rst"  # setter called
foo = c.file_name    # getter called
print( "foo = ", foo, "; efile_namepected file.rst" )
del c.file_name      # deleter called


# l127914@pn1249300.lanl.gov:class $ python so-example-02.py
# setter of file_name called
# getter of file_name called
# foo =  file.rst ; efile_namepected file.rst
# deleter of file_name called

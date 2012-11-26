#siculiserver.py
##Aka robotframework-siculiserver
Jython script to run a robot remote library exposing the Siculi API (and popen)

##Under windows

run like so (if installed to "C:\Program Files (x86)\Sikuli X\"):

    SET OLDPATH=%PATH%
    SET PATH=%OLDPATH%;C:\Program Files (x86)\Sikuli X\libs
    SET PATH=%OLDPATH%;C:\Program Files (x86)\Java\jre7\lib
    SET SIKULI_HOME=C:\Program Files (x86)\Sikuli X\
    java -cp "%SIKULI_HOME%sikuli-script.jar" org.python.util.jython siculiserver.py
    SET PATH=%OLDPATH%
    
##Under bash
this works ($PATH_TO_SIKULI is what you set in siculi_installer):

    OLDPATH=$PATH
    PATH=$OLDPATH:$PATH_TO_SIKULI/lib
    java -cp "$PATH_TO_SIKULI/sikuli-script.jar" org.python.util.jython siculiserver.py
    PATH=$OLDPATH

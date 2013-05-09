SET OLDPATH=%PATH%
::
:: These paths are the defaults for Sikuli X and Java 6 - if they're not
:: correct, change them
::
SET PATH=%OLDPATH%;C:\Program Files (x86)\Sikuli X\libs
SET PATH=%PATH%;C:\Program Files (x86)\Java\jre6\lib
SET JAVA="C:\Program Files\Java\jre6\bin\java.exe"
::
::  This should already be set, but if not, uncomment it
::
::  SET SIKULI_HOME=C:\Program Files (x86)\Sikuli X\
for /f %%i in ('python -c "import jython_sikuli_server; import os; print os.path.dirname(os.path.dirname(jython_sikuli_server.__file__))"') do set PACKAGE_PATH=%%i
for /f %%i in ('CD') do set CURRENT_DIR=%%i
cd %PACKAGE_PATH%
%JAVA% -cp "%SIKULI_HOME%sikuli-script.jar" org.python.util.jython -m jython_sikuli_server
SET PATH=%OLDPATH%
cd CURRENT_DIR%

#!/bin/sh

#
# This is the path to the sikuli-script jar as found on osx, update to reflect
# your platform
#
PATH_TO_SIKULI_JAR=/Applications/Sikuli-IDE.app/Contents/Resources/Java/
PACKAGE_PATH=`python -c "import jython_sikuli_server; import os; print os.path.dirname(os.path.dirname(jython_sikuli_server.__file__))"`
CURRENT_DIR=`pwd`
cd $PACKAGE_PATH
java -cp "$PATH_TO_SIKULI_JAR/sikuli-script.jar" org.python.util.jython -m jython_sikuli_server
cd $CURRENT_DIR

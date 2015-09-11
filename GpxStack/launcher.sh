
# get the file directory
INSTALL_DIR=$(dirname $0)
cd $INSTALL_DIR

# updating LD_LIBRARY_PATH for accessing to library installed with
# MacPort such as Cairo
export LD_LIBRARY_PATH=/opt/local/lib:$LD_LIBRARY_PATH

# adding lib dir to PYHTONPATH
export PYTHONPATH=$INSTALL_DIR/lib/:$PYTHONPATH




python src/main.py


# tests
#python test/gpxpy_test.py
#python test/gizeh_test.py
#python test/gizeh2_test.py
#python test/gizeh3_test.py

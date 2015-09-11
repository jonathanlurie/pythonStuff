
# get the file directory
INSTALL_DIR=$(dirname $0)
cd $INSTALL_DIR

# adding lib dir to PYHTONPATH
export PYTHONPATH=$INSTALL_DIR/lib/:$PYTHONPATH


export LD_LIBRARY_PATH=$INSTALL_DIR/lib/:$LD_LIBRARY_PATH

python src/main.py

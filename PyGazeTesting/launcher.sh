
# get the file directory
INSTALL_DIR=$(dirname $0)
cd $INSTALL_DIR

# adding lib dir to PYHTONPATH
export PYTHONPATH=$INSTALL_DIR/lib/:$PYTHONPATH
export PYTHONPATH=$INSTALL_DIR/lib/renegateLibs/:$PYTHONPATH



#python src/main.py
#python test/examples/show_webcam/camtest.py
python test/examples/simple_experiment/simple_experiment.py

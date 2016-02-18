export SRC_DIR=~/gitRepos/trackletOverlay
export DST_DIR=~/gitRepos/trackletOverlay
protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/trackletOverlay.proto 

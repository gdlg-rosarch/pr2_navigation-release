# Script generated with Bloom
pkgdesc="ROS - This package holds navigation-specific sensor configuration options and launch files for the PR2."
url='http://ros.org/wiki/pr2_navigation_perception'

pkgname='ros-kinetic-pr2-navigation-perception'
pkgver='0.1.27_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-filters'
'ros-kinetic-geometry-msgs'
'ros-kinetic-laser-filters'
'ros-kinetic-laser-geometry'
'ros-kinetic-laser-tilt-controller-filter'
'ros-kinetic-message-filters'
'ros-kinetic-pcl-ros'
'ros-kinetic-pr2-machine'
'ros-kinetic-pr2-navigation-self-filter'
'ros-kinetic-roscpp'
'ros-kinetic-semantic-point-annotator'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-topic-tools'
)

depends=('ros-kinetic-dynamic-reconfigure'
'ros-kinetic-filters'
'ros-kinetic-geometry-msgs'
'ros-kinetic-laser-filters'
'ros-kinetic-laser-geometry'
'ros-kinetic-laser-tilt-controller-filter'
'ros-kinetic-message-filters'
'ros-kinetic-pcl-ros'
'ros-kinetic-pr2-machine'
'ros-kinetic-pr2-navigation-self-filter'
'ros-kinetic-roscpp'
'ros-kinetic-semantic-point-annotator'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=pr2_navigation_perception
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_navigation_perception $srcdir/pr2_navigation_perception
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}


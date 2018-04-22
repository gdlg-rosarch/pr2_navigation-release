# Script generated with Bloom
pkgdesc="ROS - This package holds launch files for running the"
url='http://ros.org/wiki/pr2_navigation_slam'

pkgname='ros-kinetic-pr2-navigation-slam'
pkgver='0.1.27_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-gmapping'
'ros-kinetic-joint-trajectory-generator'
'ros-kinetic-move-base'
'ros-kinetic-pr2-machine'
'ros-kinetic-pr2-move-base'
'ros-kinetic-pr2-navigation-config'
'ros-kinetic-pr2-tuck-arms-action'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=pr2_navigation_slam
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_navigation_slam $srcdir/pr2_navigation_slam
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


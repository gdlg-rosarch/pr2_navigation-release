# Script generated with Bloom
pkgdesc="ROS - The pr2_navigation stack holds common configuration options for running the"
url='http://ros.org/wiki/pr2_navigation'

pkgname='ros-kinetic-pr2-navigation'
pkgver='0.1.27_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-laser-tilt-controller-filter'
'ros-kinetic-pr2-move-base'
'ros-kinetic-pr2-navigation-config'
'ros-kinetic-pr2-navigation-global'
'ros-kinetic-pr2-navigation-local'
'ros-kinetic-pr2-navigation-perception'
'ros-kinetic-pr2-navigation-self-filter'
'ros-kinetic-pr2-navigation-slam'
'ros-kinetic-pr2-navigation-teleop'
'ros-kinetic-semantic-point-annotator'
)

conflicts=()
replaces=()

_dir=pr2_navigation
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_navigation $srcdir/pr2_navigation
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


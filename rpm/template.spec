Name:           ros-kinetic-pr2-navigation-slam
Version:        0.1.27
Release:        0%{?dist}
Summary:        ROS pr2_navigation_slam package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_navigation_slam
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gmapping
Requires:       ros-kinetic-joint-trajectory-generator
Requires:       ros-kinetic-move-base
Requires:       ros-kinetic-pr2-machine
Requires:       ros-kinetic-pr2-move-base
Requires:       ros-kinetic-pr2-navigation-config
Requires:       ros-kinetic-pr2-tuck-arms-action
Requires:       ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-catkin

%description
This package holds launch files for running the

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 12 2018 Devon Ash <dash@clearpathrobotics.com> - 0.1.27-0
- Autogenerated by Bloom


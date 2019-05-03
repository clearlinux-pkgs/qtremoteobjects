#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtremoteobjects
Version  : 5.12.3
Release  : 17
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.3/submodules/qtremoteobjects-everywhere-src-5.12.3.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.3/submodules/qtremoteobjects-everywhere-src-5.12.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtremoteobjects-bin = %{version}-%{release}
Requires: qtremoteobjects-lib = %{version}-%{release}
Requires: qtremoteobjects-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
Put all documentation images into this folder.

%package bin
Summary: bin components for the qtremoteobjects package.
Group: Binaries
Requires: qtremoteobjects-license = %{version}-%{release}

%description bin
bin components for the qtremoteobjects package.


%package dev
Summary: dev components for the qtremoteobjects package.
Group: Development
Requires: qtremoteobjects-lib = %{version}-%{release}
Requires: qtremoteobjects-bin = %{version}-%{release}
Provides: qtremoteobjects-devel = %{version}-%{release}
Requires: qtremoteobjects = %{version}-%{release}

%description dev
dev components for the qtremoteobjects package.


%package lib
Summary: lib components for the qtremoteobjects package.
Group: Libraries
Requires: qtremoteobjects-license = %{version}-%{release}

%description lib
lib components for the qtremoteobjects package.


%package license
Summary: license components for the qtremoteobjects package.
Group: Default

%description license
license components for the qtremoteobjects package.


%prep
%setup -q -n qtremoteobjects-everywhere-src-5.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1556923644
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtremoteobjects
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtremoteobjects/LICENSE.LGPL3
cp tools/repc/moc_copy/util/licenseheader.txt %{buildroot}/usr/share/package-licenses/qtremoteobjects/tools_repc_moc_copy_util_licenseheader.txt
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/repc

%files dev
%defattr(-,root,root,-)
/usr/bin/repc
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_local_backend_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_qnx_backend_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_qnx_global_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_qnx_qiodevices_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_qnx_server_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnection_tcpip_backend_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qconnectionfactories_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectnode_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectpacket_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectpendingcall_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectregistrysource_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectreplica_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectsource_p.h
/usr/include/qt5/QtRemoteObjects/5.12.3/QtRemoteObjects/private/qremoteobjectsourceio_p.h
/usr/include/qt5/QtRemoteObjects/QAbstractItemModelReplica
/usr/include/qt5/QtRemoteObjects/QIOQnxSource
/usr/include/qt5/QtRemoteObjects/QIntHash
/usr/include/qt5/QtRemoteObjects/QQnxNativeIo
/usr/include/qt5/QtRemoteObjects/QQnxNativeServer
/usr/include/qt5/QtRemoteObjects/QRemoteObjectAbstractPersistedStore
/usr/include/qt5/QtRemoteObjects/QRemoteObjectDynamicReplica
/usr/include/qt5/QtRemoteObjects/QRemoteObjectHost
/usr/include/qt5/QtRemoteObjects/QRemoteObjectHostBase
/usr/include/qt5/QtRemoteObjects/QRemoteObjectNode
/usr/include/qt5/QtRemoteObjects/QRemoteObjectPendingCall
/usr/include/qt5/QtRemoteObjects/QRemoteObjectPendingCallWatcher
/usr/include/qt5/QtRemoteObjects/QRemoteObjectPendingReply
/usr/include/qt5/QtRemoteObjects/QRemoteObjectRegistry
/usr/include/qt5/QtRemoteObjects/QRemoteObjectRegistryHost
/usr/include/qt5/QtRemoteObjects/QRemoteObjectReplica
/usr/include/qt5/QtRemoteObjects/QRemoteObjectSettingsStore
/usr/include/qt5/QtRemoteObjects/QRemoteObjectSourceLocation
/usr/include/qt5/QtRemoteObjects/QRemoteObjectSourceLocationInfo
/usr/include/qt5/QtRemoteObjects/QRemoteObjectSourceLocations
/usr/include/qt5/QtRemoteObjects/QtRemoteObjects
/usr/include/qt5/QtRemoteObjects/QtRemoteObjectsDepends
/usr/include/qt5/QtRemoteObjects/QtRemoteObjectsVersion
/usr/include/qt5/QtRemoteObjects/qconnection_qnx_qiodevices.h
/usr/include/qt5/QtRemoteObjects/qconnection_qnx_server.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectabstractitemmodeltypes.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectdynamicreplica.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectnode.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectpendingcall.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectregistry.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectreplica.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectsettingsstore.h
/usr/include/qt5/QtRemoteObjects/qremoteobjectsource.h
/usr/include/qt5/QtRemoteObjects/qtremoteobjectglobal.h
/usr/include/qt5/QtRemoteObjects/qtremoteobjectsversion.h
/usr/include/qt5/QtRepParser/QRegexParser
/usr/include/qt5/QtRepParser/QtRepParser
/usr/include/qt5/QtRepParser/QtRepParserDepends
/usr/include/qt5/QtRepParser/QtRepParserVersion
/usr/include/qt5/QtRepParser/parser.g
/usr/include/qt5/QtRepParser/qregexparser.h
/usr/include/qt5/QtRepParser/qtrepparserversion.h
/usr/lib64/cmake/Qt5RemoteObjects/Qt5RemoteObjectsConfig.cmake
/usr/lib64/cmake/Qt5RemoteObjects/Qt5RemoteObjectsConfigExtras.cmake
/usr/lib64/cmake/Qt5RemoteObjects/Qt5RemoteObjectsConfigVersion.cmake
/usr/lib64/cmake/Qt5RemoteObjects/Qt5RemoteObjectsMacros.cmake
/usr/lib64/cmake/Qt5RepParser/Qt5RepParserConfig.cmake
/usr/lib64/cmake/Qt5RepParser/Qt5RepParserConfigVersion.cmake
/usr/lib64/libQt5RemoteObjects.prl
/usr/lib64/libQt5RemoteObjects.so
/usr/lib64/pkgconfig/Qt5RemoteObjects.pc
/usr/lib64/qt5/mkspecs/features/remoteobjects_repc.prf
/usr/lib64/qt5/mkspecs/features/repcclient.pri
/usr/lib64/qt5/mkspecs/features/repccommon.pri
/usr/lib64/qt5/mkspecs/features/repcmerged.pri
/usr/lib64/qt5/mkspecs/features/repcserver.pri
/usr/lib64/qt5/mkspecs/features/repparser.prf
/usr/lib64/qt5/mkspecs/modules/qt_lib_remoteobjects.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_remoteobjects_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_repparser.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_repparser_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5RemoteObjects.so.5
/usr/lib64/libQt5RemoteObjects.so.5.12
/usr/lib64/libQt5RemoteObjects.so.5.12.3
/usr/lib64/qt5/qml/QtQml/RemoteObjects/libqtqmlremoteobjects.so
/usr/lib64/qt5/qml/QtQml/RemoteObjects/plugins.qmltypes
/usr/lib64/qt5/qml/QtQml/RemoteObjects/qmldir
/usr/lib64/qt5/qml/QtRemoteObjects/libqtremoteobjects.so
/usr/lib64/qt5/qml/QtRemoteObjects/plugins.qmltypes
/usr/lib64/qt5/qml/QtRemoteObjects/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL2
/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL3
/usr/share/package-licenses/qtremoteobjects/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtremoteobjects/LICENSE.LGPL3
/usr/share/package-licenses/qtremoteobjects/tools_repc_moc_copy_util_licenseheader.txt

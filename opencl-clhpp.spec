%define commit b9e3d5d
%define snapshot .git20161123.%{commit}

Name:           opencl-clhpp
Version:        2.0.10
Release:        1%{snapshot}%{?dist}
Summary:        OpenCL Host API C++ bindings

License:        KHRONOS
URL:            https://github.com/KhronosGroup/OpenCL-CLHPP

# git clone https://github.com/KhronosGroup/OpenCL-CLHPP.git
# cd OpenCL-CLHPP
# git archive --prefix=OpenCL-CLHPP/ master | bzip2 >../OpenCL-CLHPP.tar.bz2
Source0:        OpenCL-CLHPP.tar.bz2

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  doxygen
Requires:       opencl-headers

%description
The interface is contained with a single C++ header file cl2.hpp and all
definitions are contained within the namespace cl. There is no additional
requirement to include cl.h and to use either the C++ or original C bindings;
it is enough to simply include cl2.hpp.

The bindings themselves are lightweight and correspond closely to the
underlying C API. Using the C++ bindings introduces no additional execution
overhead.


%prep
%setup -q -n OpenCL-CLHPP


%build
mkdir build
pushd build
%{cmake} -DCMAKE_INSTALL_PREFIX=%{_includedir} -DBUILD_EXAMPLES=OFF -DBUILD_TESTS=OFF ..
make
make docs
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%files
%license LICENSE.txt
%doc README.txt build/docs/html/
%{_includedir}/*


%changelog
* Wed Nov 23 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.0.10-1.git20161123.b9e3d5d
- Public release

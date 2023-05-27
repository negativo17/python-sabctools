%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname sabctools

Name:           python-%{srcname}
Version:        7.0.2
Release:        1%{?dist}
Summary:        C implementations of functions for use within SABnzbd
License:        GPLv2+
URL:            https://github.com/sabnzbd/%{srcname}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
This module implements three main sets of C implementations that are used within
SABnzbd:

- yEnc decoding and encoding using SIMD routines
- CRC32 calculations
- Non-blocking SSL-socket reading
- Marking files as sparse

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This module implements three main sets of C implementations that are used within
SABnzbd:

- yEnc decoding and encoding using SIMD routines
- CRC32 calculations
- Non-blocking SSL-socket reading
- Marking files as sparse

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.md
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat May 27 2023 Simone Caronni <negativo17@gmail.com> - 7.0.2-1
- First build.

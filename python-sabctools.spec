%global srcname sabctools

Name:           python-%{srcname}
Version:        8.1.0
Release:        1%{?dist}
Summary:        C implementations of functions for use within SABnzbd
License:        GPLv2+
URL:            https://github.com/sabnzbd/%{srcname}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%description
This module implements three main sets of C implementations that are used within
SABnzbd:

- yEnc decoding and encoding using SIMD routines
- CRC32 calculations
- Non-blocking SSL-socket reading
- Marking files as sparse

%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-sabyenc < 6.0.0

%description -n python3-%{srcname}
This module implements three main sets of C implementations that are used within
SABnzbd:

- yEnc decoding and encoding using SIMD routines
- CRC32 calculations
- Non-blocking SSL-socket reading
- Marking files as sparse

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n  python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Wed Jan 31 2024 Simone Caronni <negativo17@gmail.com> - 1:8.1.0-1
- Update to 8.1.0.

* Sat Nov 11 2023 Simone Caronni <negativo17@gmail.com> - 1:7.1.2-1
- Downgrade to 7.1.2.

* Fri Nov 10 2023 Simone Caronni <negativo17@gmail.com> - 8.0.0-2
- Obsolete sabyenc.

* Fri Nov 10 2023 Simone Caronni <negativo17@gmail.com> - 8.0.0-1
- Update to 8.0.0.

* Fri Nov 10 2023 Simone Caronni <negativo17@gmail.com> - 7.0.2-2
- Clean up SPEC file.

* Sat May 27 2023 Simone Caronni <negativo17@gmail.com> - 7.0.2-1
- First build.

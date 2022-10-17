# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-sh
Epoch: 100
Version: 1.14.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Python process launching
License: MIT
URL: https://github.com/amoffat/sh/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
sh is a full-fledged subprocess replacement for Python 2, Python 3, PyPy
and PyPy3 that allows you to call any program as if it were a function.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-sh
Summary: Python process launching
Requires: python3
Provides: python3-sh = %{epoch}:%{version}-%{release}
Provides: python3dist(sh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-sh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(sh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-sh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(sh) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-sh
sh is a full-fledged subprocess replacement for Python 2, Python 3, PyPy
and PyPy3 that allows you to call any program as if it were a function.

%files -n python%{python3_version_nodots}-sh
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-sh
Summary: Python process launching
Requires: python3
Provides: python3-sh = %{epoch}:%{version}-%{release}
Provides: python3dist(sh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-sh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(sh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-sh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(sh) = %{epoch}:%{version}-%{release}

%description -n python3-sh
sh is a full-fledged subprocess replacement for Python 2, Python 3, PyPy
and PyPy3 that allows you to call any program as if it were a function.

%files -n python3-sh
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog

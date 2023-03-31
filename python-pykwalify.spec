Summary:	Python library for JSON/YAML schema validation
Name:		python-pykwalify
Version:	1.8.0
Release:	3
Group:		Development/Python
License:	BSD
Url:		https://pypi.org/project/pykwalify/
Source0:	https://files.pythonhosted.org/packages/source/p/pykwalify/pykwalify-%{version}.tar.gz
Patch0:		fix-python-requires.patch
BuildRequires:	python3dist(setuptools)
BuildArch:	noarch

%description
Python library for JSON/YAML schema validation

%files
%{_bindir}/*
%{py_puresitedir}/pykwalify
%{py_puresitedir}/pykwalify*.egg-info

#------------------------------------------------------------
%prep
%autosetup -p1 -n pykwalify-%{version}

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check

#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Runtime inspection utilities for typing module
Summary(pl.UTF-8):	Narzędzia do doglądania w czasie działania programu dla modułu typing
Name:		python-typing_inspect
Version:	0.9.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/typing-inspect/
Source0:	https://files.pythonhosted.org/packages/source/t/typing-inspect/typing_inspect-%{version}.tar.gz
# Source0-md5:	334f7f909260ceebb05e10ebd7039ff0
URL:		https://pypi.org/project/typing-inspect/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mypy_extensions >= 0.3.0
BuildRequires:	python-pytest
BuildRequires:	python-typing >= 3.7.4
BuildRequires:	python-typing_extensions >= 3.7.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mypy_extensions >= 0.3.0
BuildRequires:	python3-pytest
BuildRequires:	python3-typing_extensions >= 3.7.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%description -l pl.UTF-8
Moduł "typing_inspect" definiuje eksperymentalne API do inspekcji
w czasie działania programu typów zdefiniowanych w standardowym
module "typing".

%package -n python3-typing_inspect
Summary:	Runtime inspection utilities for typing module
Summary(pl.UTF-8):	Narzędzia do doglądania w czasie działania programu dla modułu typing
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-typing_inspect
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%description -n python3-typing_inspect -l pl.UTF-8
Moduł "typing_inspect" definiuje eksperymentalne API do inspekcji
w czasie działania programu typów zdefiniowanych w standardowym
module "typing".

%package apidocs
Summary:	API documentation for Python typing_inspect module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona typing_inspect
Group:		Documentation

%description apidocs
API documentation for Python typing_inspect module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona typing_inspect.

%prep
%setup -q -n typing_inspect-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test_typing_inspect.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_typing_inspect.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/typing_inspect.py[co]
%{py_sitescriptdir}/typing_inspect-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-typing_inspect
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/typing_inspect.py
%{py3_sitescriptdir}/__pycache__/typing_inspect.cpython-*.py[co]
%{py3_sitescriptdir}/typing_inspect-%{version}-py*.egg-info
%endif

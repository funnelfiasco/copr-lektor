%global srcname Lektor
%global sum A static content management system
%global git_date 20200824
%global git_rev  1438f54
%global git_revision 1438f5444afe4b21f12b131b84b0c24118b61cd3

Name:			python-Lektor
Version:		3.2.0.%{git_date}git%{git_rev}
Release:		3%{?dist}
Summary:		A static content management system

License:		BSD
URL:			https://github.com/lektor/lektor/
#Source0:		https://files.pythonhosted.org/packages/source/L/%{srcname}/%{srcname}-%{version}.tar.gz
Source0:                https://github.com/lektor/lektor/archive/%{git_revision}.zip
# Pass the lowercase argument to slugify in order to make it do what I want
Patch0:         https://raw.githubusercontent.com/funnelfiasco/copr-lektor/main/slugify-no-lowercase.patch
Patch1:         https://raw.githubusercontent.com/funnelfiasco/copr-lektor/main/werkzeug-no-version.patch
BuildArch:		noarch

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
Lektor is a static website generator. It builds out an entire project
from static files into many individual HTML pages and has a built-in
admin UI and minimal desktop app.

%package -n python3-%{srcname}
Summary: A static content management system

Requires:	python3-mistune
Requires:	python3-watchdog
Requires:	python3-argh
Requires:	python3-flask
Requires:	python3-exif
Requires:	python3-requests
Requires:	python3-ndg_httpsclient
Requires:	python3-pyasn1
Requires:	python3-jinja2
Requires:	python3-babel
Requires:	python3-inifile
Requires:	python3-click
Requires:	python3-pathtools
Requires:	python3-werkzeug
Requires:	python3-yaml

Provides:   python3-lektor = %{version}-%{release}

Provides:   lektor = %{version}-%{release}

# Providing and obsoleting the python2 namespace
# for a clean upgrade path after changing the package
# to python 3 only
Provides:   python2-%{srcname} = %{version}-%{release}
Obsoletes:	python2-%{srcname} < %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Lektor is a static website generator. It builds out an entire project
from static files into many individual HTML pages and has a built-in
admin UI and minimal desktop app.

%prep
%setup -n lektor-%{git_revision}
rm -rf %{srcname}.egg-info

%patch0 -p0
%patch1 -p1


%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/lektor
%{_bindir}/lektor

%changelog
* Mon Nov 02 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.2.0.20201102git1438f54-3
- Add explicit dependency on python3-werkzeug and remove the < 1 requirement

* Tue Sep 08 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.2.0.20200824git1438f54-2
- Add a patch to disable auto-lowercase in slugs

* Mon Aug 24 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.2.0git1438f54-1
- Latest upstream snapshot
- Includes/is 3.2.0 release

* Tue Aug 18 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.2.dev0.20200818.git67eab5c-1
- Latest upstream snapshot
- Includes 3.2.dev0 release

* Mon Jul 13 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.1.99.20200712git276397d-1
- Latest upstream snapshot

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Charalampos Stratakis <cstratak@redhat.com> 3.0.1-1
- Upgrade to version 3.0.1
- Change to python3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 01 2016 Charalampos Stratakis <cstratak@redhat.com> 2.3-1
- Upgrade to version 2.3
- Use newest pypi url format

* Mon May 16 2016 Charalampos Stratakis <cstratak@redhat.com> 2.2-1
- Upgrade to version 2.2

* Mon Apr 11 2016 Charalampos Stratakis <cstratak@redhat.com> 2.0-1
- Upgrade to version 2.0

* Tue Feb 23 2016 Charalampos Stratakis <cstratak@redhat.com> 1.2.1-1
- Initial RPM release

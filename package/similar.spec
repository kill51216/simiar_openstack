Name:       similar
Version:    %{version}
Release:    1%{?dist}
Epoch:      1
Summary:    Similar OpenStack Service.

License:    ASL 2.0
URL:        http://github.com/similar
Source:     similar-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python
Requires:       python


%description
Similar OpenStack Service.

%prep
%setup -q -n similar-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

install -d -m 750 %{buildroot}%{_localstatedir}/log/similar
install -d -m 750 %{buildroot}%{_sysconfdir}/similar

install -p -D -m 755 package/systemd/similar-api.service %{buildroot}%{_unitdir}/similar-api.service

install -p -D -m 640 etc/similar/similar.conf  %{buildroot}%{_sysconfdir}/similar/similar.conf
install -p -D -m 640 etc/similar/api-paste.ini  %{buildroot}%{_sysconfdir}/similar/api-paste.ini
install -p -D -m 640 etc/similar/policy.json  %{buildroot}%{_sysconfdir}/similar/policy.json
install -p -D -m 640 etc/logrotate.d/openstack-similar %{buildroot}%{_sysconfdir}/logrotate.d/similar

%post
%systemd_post similar-api.service

%preun
%systemd_preun similar-api.service

%postun
%systemd_postun similar-api.service


%files
%{_bindir}/similar-api
%dir %{_sysconfdir}/similar
%config(noreplace) %{_sysconfdir}/similar/similar.conf
%config %{_sysconfdir}/similar/api-paste.ini
%config(noreplace) %{_sysconfdir}/similar/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/similar
%{_unitdir}/similar-api.service

%dir %attr(0750, root, root) %{_localstatedir}/log/similar
%{python2_sitelib}/similar
%{python2_sitelib}/similar-*.egg-info

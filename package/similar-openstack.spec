Name:       similar-openstack
Version:    %{version}
Release:    1%{?dist}
Epoch:      1
Summary:    Similar OpenStack Service.

License:
URL:        http://github.com/similar-openstack
Source:     similar-openstack-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python
Requires:       python


%description
Similar OpenStack Service.

%prep
%setup -q -n similar-openstack-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

install -d -m 750 %{buildroot}%{_localstatedir}/log/similar-openstack
install -d -m 750 %{buildroot}%{_sysconfdir}/similar-openstack

install -p -D -m 755 package/systemd/similar-openstack-api.service %{buildroot}%{_unitdir}/similar-openstack-api.service

install -p -D -m 640 etc/similar-openstack/similar-openstack.conf  %{buildroot}%{_sysconfdir}/similar-openstack/similar-openstack.conf
install -p -D -m 640 etc/similar-openstack/api-paste.ini  %{buildroot}%{_sysconfdir}/similar-openstack/api-paste.ini
install -p -D -m 640 etc/similar-openstack/policy.json  %{buildroot}%{_sysconfdir}/similar-openstack/policy.json
install -p -D -m 640 etc/logrotate.d/openstack-similar-openstack %{buildroot}%{_sysconfdir}/logrotate.d/similar-openstack

%post
%systemd_post similar-openstack-api.service

%preun
%systemd_preun similar-openstack-api.service

%postun
%systemd_postun similar-openstack-api.service


%files
%{_bindir}/similar-openstack-api
%dir %{_sysconfdir}/similar-openstack
%config(noreplace) %{_sysconfdir}/similar-openstack/similar-openstack.conf
%config %{_sysconfdir}/similar-openstack/api-paste.ini
%config(noreplace) %{_sysconfdir}/similar-openstack/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/similar-openstack
%{_unitdir}/similar-openstack-api.service

%dir %attr(0750, root, root) %{_localstatedir}/log/similar-openstack
%{python2_sitelib}/similar-openstack
%{python2_sitelib}/similar-openstack-*.egg-info

Name:           parsidora-bookmarks
Version:        14
Release:        1
Summary:        Parsidora bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://parsidora.org/
# I had to strip the embedded icons out of the bookmarks file, because they are not 
# distributable under the GFDL. See https://bugzilla.redhat.com/show_bug.cgi?id=433471
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Parsidora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Tue Aug 03 2010 Mostafa Daneshvar info@mostafadaneshvar.com 13-2
- New Parsidora bookmarks
* Mon Mar 22 2010 Christopher Aillon <caillon@redhat.com> 13-1
- Minor updates from marketing

* Fri Jul 24 2009 Parsidora Release Engineering <rel-eng@lists.Parsidoraproject.org> - 11-2
- Rebuilt for https://Parsidoraproject.org/wiki/Parsidora_12_Mass_Rebuild

* Fri May  1 2009 Christopher Aillon <caillon@redhat.com> - 11-1
- Refresh Parsidora Project link set
- Add new Free Content link
- Remove obsolete links

* Tue Feb 24 2009 Parsidora Release Engineering <rel-eng@lists.Parsidoraproject.org> - 10-2
- Rebuilt for https://Parsidoraproject.org/wiki/Parsidora_11_Mass_Rebuild

* Tue Sep  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 10-1
- fix bookmarks.html to not have embedded icons, they aren't usable under the GFDL.
  resolves bz 433471

* Wed Oct 17 2007 Matthias Clasen <mclasen@redhat.com> 8-1
- Update the link to the Parsidora project homepage  (#291851)

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> 7-2
- Remove reference to 'Core' from summary.  (#247362)

* Sun Apr 15 2007 Christopher Aillon <caillon@redhat.com> 7-1
- FC7 bookmarks based on http://Parsidoraproject.org/wiki/Releases/7/Bookmarks

* Tue Mar 20 2007 Christopher Aillon <caillon@redhat.com> 6-2
- Package review updates

* Wed Oct 18 2006 Christopher Aillon <caillon@redhat.com> 6-1
- Initial version


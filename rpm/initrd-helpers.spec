Name:       initrd-helpers
Summary:    Helper scripts and tools for init ramdisks
Version:    0.0.1
Release:    1
Group:      System/Boot
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz

Requires:  btrfs-progs

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
mkdir -p %{buildroot}/sbin/
install -D -m 755 btrfs-mount-repair %{buildroot}/sbin/btrfs-mount-repair
install -D -m 755 find-mmc-bypartlabel %{buildroot}/sbin/find-mmc-bypartlabel

%files
%defattr(-,root,root,-)
/sbin/btrfs-mount-repair
/sbin/find-mmc-bypartlabel

%doc LICENSE README




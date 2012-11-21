Summary:	Digital look-ahead peak limiter
Name:		zita-dpl1
Version:	0.0.2
Release:	2
License:	GPL v2 / Other (see LICENSE)
Group:		X11/Applications
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	6f76ef405396940409f5da89c37a775a
Patch0:		%{name}-make.patch
BuildRequires:	cairo-devel
BuildRequires:	clthreads-devel
BuildRequires:	clxclient-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DPL1 is an look-ahead digital peak limiter, the kind you would use as
the final step to avoid clipping when mastering or mixing. It can
be used as an effect on individual instrument tracks as well.

Latency is 1.2 ms rounded up to the nearest multiple of 8, 16 or 32
samples depending on sampling frequency. This amounts to 56 samples
at 44.1 kHz, 64 samples at 48 kHz, and twice those values for 88.2 or
96 kHz.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} -C source \
	CXX="%{__cxx}"

head -21 source/dplimit1.h > LICENSE

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}


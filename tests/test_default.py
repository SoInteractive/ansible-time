from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(Package):
    present = [
        "tzdata",
        "ntp"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_directories(File):
    present = [
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/ntp.conf"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_services(Service, SystemInfo):
    present = [
        "ntp"
    ]
    for service in present:
        s = Service(service)
        assert s.is_enabled
        assert s.is_running

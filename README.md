<p><img src="https://upload.wikimedia.org/wikipedia/commons/2/25/Hourglass_2.svg" alt="time logo" title="time" align="right" height="60" /></p>

Ansible Role: NTP sync
======================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/time/master)](https://ci.devops.sosoftware.pl/job/SoInteractive/time/master) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18223.svg)](https://galaxy.ansible.com/SoInteractive/time/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Role checks if ntp or chrony is available and configures one to access NTP servers served by comarch, hetzner or europe pool

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.time
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- Standardize variable names
- Move to ntpd (remove chrony support)
- Write tests
- Autodetection of server location

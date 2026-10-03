# Testbed Navigation

## Overview

This package implements a manual Nav2 navigation workflow for the Testbed-T1.0.0 robot.

The navigation system is divided into separate launch files for:

- Map loading
- AMCL localization
- Navigation

The package does not use `nav2_bringup`. Required Nav2 components are launched individually.

## Package Structure

```text
testbed_navigation/
├── config/
│   ├── amcl_params.yaml
│   └── nav2_params.yaml
├── launch/
│   ├── map_loader.launch.py
│   ├── localization.launch.py
│   └── navigation.launch.py
├── CMakeLists.txt
├── package.xml
└── README.md

# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name = 'task_test_base',
  sources = ['task_test_base.py'],
  dependencies = [
    'src/python/pants/goal:context',
    'src/python/pants/ivy',
    'src/python/pants/util:contextutil',
    'src/python/pants/task',
    'tests/python/pants_test:base_test',
  ]
)

target(
  name = 'tasks',
  dependencies = [
    ':builddict',
    ':execution_graph',
    ':group_task',
    ':list_goals',
    ':list_owners',
    ':listtargets',
    ':minimal_cover',
    ':reflect',
    ':sorttargets',
    ':targets_help',
  ],
)

target(
  name = 'integration',
  dependencies = [
    ':bootstrap_jvm_tools_integration',
    ':scalastyle_integration',
  ],
)

python_tests(
  name = 'scalastyle_integration',
  sources = ['test_scalastyle_integration.py'],
  dependencies = [
    'tests/python/pants_test:int-test',
    'src/python/pants/util:contextutil',
  ]
)

python_tests(
  name = 'builddict',
  sources = ['test_builddict.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core:plugin',
    'src/python/pants/backend/core/tasks:builddictionary',
    'src/python/pants/backend/core/tasks:reflect',
    'src/python/pants/backend/jvm:plugin',
    'src/python/pants/backend/python:plugin',
    'src/python/pants/goal',
    'src/python/pants/goal:task_registrar',
    'tests/python/pants_test:base_test',
  ]
)

python_tests(
  name = 'changed_target_integration',
  sources = ['test_changed_target_integration.py'],
  dependencies = [
    'src/python/pants/util:contextutil',
    'tests/python/pants_test:int-test',
  ],
)

python_tests(
  name = 'bootstrap_jvm_tools_integration',
  sources = ['test_bootstrap_jvm_tools_integration.py'],
  dependencies = [
    'src/python/pants/util:contextutil',
    'tests/python/pants_test:int-test',
  ],
)

python_tests(
  name = 'reflect',
  sources = ['test_reflect.py'],
  dependencies = [
    'src/python/pants/backend/core:plugin',
    'src/python/pants/backend/core/tasks:reflect',
    'src/python/pants/backend/jvm:plugin',
    'src/python/pants/backend/python:plugin',
    'tests/python/pants_test:base_test',
  ]
)

python_tests(
  name = 'execution_graph',
  sources = ['test_execution_graph.py'],
  dependencies = [
    'src/python/pants/backend/jvm/tasks/jvm_compile:execution_graph',
    ]
)

python_tests(
  name = 'filemap',
  sources = ['test_filemap.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core/tasks:filemap',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'list_goals',
  sources = ['test_list_goals.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core/tasks:list_goals',
    'src/python/pants/goal',
    'src/python/pants/goal:task_registrar',
    'src/python/pants/task',
  ],
)

python_tests(
  name = 'listtargets',
  sources = ['test_listtargets.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core/tasks:listtargets',
    'src/python/pants/backend/jvm:artifact',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'minimal_cover',
  sources = ['test_minimal_cover.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core/tasks:minimal_cover',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'sorttargets',
  sources = ['test_sorttargets.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/backend/core/tasks:sorttargets',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'targets_help',
  sources = ['test_targets_help.py'],
  dependencies = [
    ':task_test_base',
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/backend/core/tasks:targets_help',
    'src/python/pants/base:build_environment',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'list_owners',
  sources = ['test_list_owners.py'],
  dependencies = [
    'src/python/pants/backend/core/tasks:list_owners',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
  ],
)

python_tests(
  name = 'group_task',
  sources = ['test_group_task.py'],
  dependencies = [
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/backend/core/tasks:group_task',
    'src/python/pants/build_graph',
    'src/python/pants/engine',
    'tests/python/pants_test:base_test',
  ]
)

python_tests(
  name = 'clean_all_integration',
  sources = ['test_clean_all_integration.py'],
  dependencies = [
    'tests/python/pants_test:int-test',
    'src/python/pants/util:contextutil',
  ]
)

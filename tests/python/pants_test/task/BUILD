# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

target(
  name='tasks',
  dependencies=[
    ':mutex_task_mixin',
    ':task',
    ':testrunner_task_mixin',
  ],
)

python_tests(
  name = 'console_task',
  sources = ['test_console_task.py'],
  dependencies = [
    'src/python/pants/task',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)

python_tests(
  name='mutex_task_mixin',
  sources=['test_mutex_task_mixin.py'],
  dependencies=[
    'src/python/pants/build_graph',
    'src/python/pants/task',
    'src/python/pants/util:contextutil',
    'tests/python/pants_test:base_test',
  ]
)

python_tests(
  name='task',
  sources=['test_task.py'],
  dependencies=[
    'src/python/pants/build_graph',
    'src/python/pants/task',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)

python_tests(
  name='testrunner_task_mixin',
  sources=['test_testrunner_task_mixin.py'],
  dependencies=[
    'src/python/pants/task',
    'src/python/pants/util:timeout',
    'tests/python/pants_test/tasks:task_test_base',
    '3rdparty/python:mock',
  ]
)

# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# =======>
# TODO: Remove these after task.py's deprecation cycle is over.
target(
  name = 'common',
  dependencies = [
    'src/python/pants/task',
  ]
)

python_library(
  name = 'task',
  sources = ['task.py'],
  dependencies = [
    'src/python/pants/base:deprecated',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'console_task',
  sources = ['console_task.py'],
  dependencies = [
    'src/python/pants/base:deprecated',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'repl_task_mixin',
  sources = ['repl_task_mixin.py'],
  dependencies = [
    'src/python/pants/base:deprecated',
    'src/python/pants/task'
  ]
)

# <======

target(
  name = 'all',
  dependencies = [
    ':bash_completion',
    ':builddictionary',
    ':cloc',
    ':confluence_publish',
    ':console_task',
    ':deferred_sources_mapper',
    ':dependees',
    ':explain_options',
    ':filemap',
    ':filter',
    ':group_task',
    ':list_goals',
    ':list_owners',
    ':listtargets',
    ':markdown_to_html',
    ':minimal_cover',
    ':pathdeps',
    ':paths',
    ':repl_task_mixin',
    ':scm_publish',
    ':sorttargets',
    ':targets_help',
    ':task',
  ]
)

python_library(
  name = 'bash_completion',
  sources = ['bash_completion.py'],
  resource_targets = [
    ':bash_completion_resources',
  ],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/base:generator',
    'src/python/pants/goal',
    'src/python/pants/help',
    'src/python/pants/option',
    'src/python/pants/task',
  ],
)

resources(
  name = 'bash_completion_resources',
  sources = globs('templates/bash_completion/*.mustache'),
)

python_library(
  name = 'builddictionary',
  sources = ['builddictionary.py'],
  resource_targets = [
    ':builddictionary_resources',
  ],
  dependencies = [
    ':reflect',
    '3rdparty/python:docutils',
    '3rdparty/python:setuptools',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/backend/python:python_requirements',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:build_manual',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:generator',
    'src/python/pants/build_graph',
    'src/python/pants/goal',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
  ],
)

resources(
  name = 'builddictionary_resources',
  sources = globs('templates/builddictionary/*.mustache'),
)

python_library(
  name = 'cloc',
  sources = ['cloc.py'],
  dependencies = [
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/binaries:binary_util',
    'src/python/pants/task',
    'src/python/pants/util:contextutil',
  ],
)

python_library(
  name = 'confluence_publish',
  sources = ['confluence_publish.py'],
  dependencies = [
    '3rdparty/python/twitter/commons:twitter.common.confluence',
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/base:exceptions',
    'src/python/pants/binaries:binary_util',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
  ],
)

python_library(
  name = 'deferred_sources_mapper',
  sources= ['deferred_sources_mapper.py'],
  dependencies = [
    'src/python/pants/base:payload_field',
    'src/python/pants/build_graph',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'dependees',
  sources = ['dependees.py'],
  dependencies = [
    ':target_filter_task_mixin',
    'src/python/pants/base:build_environment',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'explain_options',
  sources = ['explain_options_task.py'],
  dependencies = [
    '3rdparty/python:ansicolors',
    'src/python/pants/option',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'filemap',
  sources = ['filemap.py'],
  dependencies = [
    'src/python/pants/task',
  ],
)

python_library(
  name = 'filter',
  sources = ['filter.py'],
  dependencies = [
    ':target_filter_task_mixin',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:cmd_line_spec_parser',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/task',
    'src/python/pants/util:filtering',
  ],
)

python_library(
  name = 'group_task',
  sources = ['group_task.py'],
  dependencies = [
    '3rdparty/python:six',
    'src/python/pants/base:workunit',
    'src/python/pants/build_graph',
    'src/python/pants/goal',
    'src/python/pants/option',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'list_goals',
  sources = ['list_goals.py'],
  dependencies = [
    'src/python/pants/goal',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'listtargets',
  sources = ['listtargets.py'],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'markdown_to_html',
  sources = ['markdown_to_html.py', 'markdown_to_html_utils.py'],
  resource_targets = [
    ':markdown_to_html_resources',
  ],
  dependencies = [
    '3rdparty/python:Markdown',
    '3rdparty/python:Pygments',
    '3rdparty/python:docutils',
    '3rdparty/python:six',
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:generator',
    'src/python/pants/base:workunit',
    'src/python/pants/binaries:binary_util',
    'src/python/pants/build_graph',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
  ],
)

resources(
  name = 'markdown_to_html_resources',
  sources = globs('templates/markdown/*.mustache'),
)

python_library(
  name = 'minimal_cover',
  sources = ['minimal_cover.py'],
  dependencies = [
    'src/python/pants/task',
  ],
)

python_library(
  name = 'pathdeps',
  sources = ['pathdeps.py'],
  dependencies = [
    'src/python/pants/task',
  ],
)

python_library(
  name = 'paths',
  sources = ['paths.py'],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/task',
    'src/python/pants/util:strutil',
  ],
)

python_library(
  name = 'reflect',
  sources = ['reflect.py'],
  dependencies = [
    ':group_task',
    '3rdparty/python:docutils',
    '3rdparty/python:six',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:build_manual',
    'src/python/pants/base:generator',
    'src/python/pants/build_graph',
    'src/python/pants/goal',
    'src/python/pants/help',
    'src/python/pants/option',
  ],
)

python_library(
  name = 'scm_publish',
  sources = ['scm_publish.py'],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/option',
    'src/python/pants/scm',
  ],
)

python_library(
  name = 'sorttargets',
  sources = ['sorttargets.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'src/python/pants/task',
  ],
)

python_library(
  name = 'target_filter_task_mixin',
  sources = ['target_filter_task_mixin.py'],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/task',
  ]
)

python_library(
  name = 'targets_help',
  sources = ['targets_help.py'],
  resource_targets = [
    ':targets_help_resources',
  ],
  dependencies = [
    ':reflect',
    'src/python/pants/task',
  ],
)

resources(
  name = 'targets_help_resources',
  sources = globs('templates/targets_help/*.mustache'),
)

python_library(
  name = 'list_owners',
  sources = ['list_owners.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'src/python/pants/task',
  ],
)

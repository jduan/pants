# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import os

from pants.backend.core.from_target import FromTarget
from pants.backend.core.targets.dependencies import Dependencies
from pants.backend.core.targets.doc import Page, Wiki, WikiArtifact
from pants.backend.core.targets.prep_command import PrepCommand
from pants.backend.core.targets.resources import Resources
from pants.backend.core.tasks.bash_completion import BashCompletionTask
from pants.backend.core.tasks.builddictionary import BuildBuildDictionary
from pants.backend.core.tasks.cloc import CountLinesOfCode
from pants.backend.core.tasks.confluence_publish import ConfluencePublish
from pants.backend.core.tasks.deferred_sources_mapper import DeferredSourcesMapper
from pants.backend.core.tasks.dependees import ReverseDepmap
from pants.backend.core.tasks.explain_options_task import ExplainOptionsTask
from pants.backend.core.tasks.filemap import Filemap
from pants.backend.core.tasks.filter import Filter
from pants.backend.core.tasks.list_goals import ListGoals
from pants.backend.core.tasks.list_owners import ListOwners
from pants.backend.core.tasks.listtargets import ListTargets
from pants.backend.core.tasks.markdown_to_html import MarkdownToHtml
from pants.backend.core.tasks.minimal_cover import MinimalCover
from pants.backend.core.tasks.pathdeps import PathDeps
from pants.backend.core.tasks.paths import Path, Paths
from pants.backend.core.tasks.sorttargets import SortTargets
from pants.backend.core.tasks.targets_help import TargetsHelp
from pants.backend.core.wrapped_globs import Globs, RGlobs, ZGlobs
from pants.base.build_environment import get_buildroot, pants_version
from pants.base.source_root import SourceRoot
from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.build_graph.target import Target
from pants.goal.task_registrar import TaskRegistrar as task


class BuildFilePath(object):
  """Returns path containing this ``BUILD`` file."""

  def __init__(self, parse_context):
    self.rel_path = parse_context.rel_path

  def __call__(self):
    return os.path.join(get_buildroot(), self.rel_path)


def build_file_aliases():
  return BuildFileAliases(
    targets={
      'dependencies': Dependencies,  # Deprecated, will be removed soon.
      'page': Page,
      'prep_command': PrepCommand,
      'resources': Resources,
      'target': Target,
    },
    objects={
      'ConfluencePublish': ConfluencePublish,
      'get_buildroot': get_buildroot,
      'pants_version': pants_version,
      'wiki_artifact': WikiArtifact,
      'Wiki': Wiki,
    },
    context_aware_object_factories={
      'buildfile_path': BuildFilePath,
      'globs': Globs.factory,
      'from_target': FromTarget,
      'rglobs': RGlobs.factory,
      'source_root': SourceRoot.factory,
      'zglobs': ZGlobs.factory,
    }
  )


def register_goals():
  # TODO: Most of these (and most tasks in other backends) can probably have their
  # with_description() removed, as their docstring will be used instead.

  # Getting help.
  task(name='goals', action=ListGoals).install().with_description('List all documented goals.')

  task(name='targets', action=TargetsHelp).install().with_description(
      'List target types and BUILD file symbols (python_tests, jar, etc).')

  task(name='builddict', action=BuildBuildDictionary).install()

  task(name='markdown', action=MarkdownToHtml).install('markdown').with_description(
      'Generate html from markdown docs.')

  # Linting.
  task(name='pathdeps', action=PathDeps).install('pathdeps').with_description(
      'Print out all paths containing BUILD files the target depends on.')

  task(name='list', action=ListTargets).install('list').with_description(
      'List available BUILD targets.')

  # Build graph information.
  task(name='path', action=Path).install().with_description(
      'Find a dependency path from one target to another.')

  task(name='paths', action=Paths).install().with_description(
      'Find all dependency paths from one target to another.')

  task(name='dependees', action=ReverseDepmap).install().with_description(
      "Print the target's dependees.")

  task(name='filemap', action=Filemap).install().with_description(
      'Outputs a mapping from source file to owning target.')

  task(name='minimize', action=MinimalCover).install().with_description(
      'Print the minimal cover of the given targets.')

  task(name='filter', action=Filter).install()

  task(name='sort', action=SortTargets).install().with_description(
      'Topologically sort the targets.')

  task(name='cloc', action=CountLinesOfCode).install('cloc').with_description(
    "Print counts of lines of code.")

  task(name='list-owners', action=ListOwners).install().with_description(
      'Print targets that own the specified source')

  task(name='deferred-sources', action=DeferredSourcesMapper).install().with_description(
    'Map unpacked sources from archives.')

  task(name='bash-completion', action=BashCompletionTask).install().with_description(
    'Dump bash shell script for autocompletion of pants command lines.')

  task(name='options', action=ExplainOptionsTask).install().with_description(
    'List what options pants has set.')

from alembic.config import Config
from alembic_scripts import command
import click
from pathlib import Path
from typing import Optional
from persistence.migrations import migration_upgrade, migration_downgrade

relative_alembic_path= Path.cwd().parent / 'alembic.ini'
alembic_cfg = Config(relative_alembic_path)


@click.group()
@click.pass_context
def cli(ctx):
    pass

# alembic cmd alembic.command.revision
# @cli.command(context_settings=dict(
#     ignore_unknown_options=True,
# ))
# @click.option('--message', '-m', default=None, help='Revision message')
# @click.pass_context
# def revision(ctx):
#     command.revision(alembic_cfg)

@cli.command()
@click.option('--revision', type=str, default='head')
@click.option('--sql', type=bool, default=False)
@click.option('--tag', type=Optional[str], default=None)
@click.pass_context
def upgrade(ctx, revision, sql, tag):
    migration_upgrade(alembic_cfg, revision, sql, tag)
    # command.upgrade(alembic_cfg, revision, sql, tag)

@cli.command()
@click.option('--revision', type=str)
@click.option('--sql', type=bool, default=False)
@click.option('--tag', type=Optional[str], default=None)
@click.pass_context
def downgrade(ctx, revision, sql, tag):
    migration_downgrade(alembic_cfg)
    # command.downgrade(alembic_cfg, revision, sql, tag)
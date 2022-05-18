# stop development, temporarily
# Not using, currently
from alembic.config import Config
import click
from pathlib import Path
from typing import Optional
from persistence.migrations import migration_upgrade, migration_downgrade
from cmds.cli_option import AVAILABLE_CLI_OPTIONS as AO
from configuration import Configuration
import pprint

relative_alembic_path= Path.cwd().parent / 'alembic.ini'
alembic_cfg = Config(relative_alembic_path)


@click.group()
@click.pass_context
@click.option(*AO['config'].cli, **AO['config'].kwargs)
@click.option(*AO['user_data_dir'].cli, **AO['user_data_dir'].kwargs)
# @click.option(*AO['logfile'].cli, **AO['logfile'].kwargs)
def cli(ctx, config, user_data_dir):
    ctx.ensure_object(dict)
    args = {
        'config': config,
        'user_data_dir': user_data_dir,
    }
    ctx.obj.update(args)


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
@click.option('--tag', type=str, default=None)
@click.pass_context
def upgrade(ctx, revision, sql, tag):
    configured, _ =  Configuration(ctx.obj).get_config()
    ## TODO: fix logfile issue
    pprint(configured) 
    exit()
    migration_upgrade(configured, revision, sql, tag)
    # command.upgrade(alembic_cfg, revision, sql, tag)

@cli.command()
@click.option('--revision', type=str)
@click.option('--sql', type=bool, default=False)
@click.option('--tag', type=str, default=None)
@click.pass_context
def downgrade(ctx, revision, sql, tag):
    migration_downgrade(alembic_cfg, revision, sql, tag)
    # command.downgrade(alembic_cfg, revision, sql, tag)
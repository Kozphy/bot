import click
from cmds.sync_command import start_sync
from loggers import setup_logging_pre
from cmds.cli_option import AVAILABLE_CLI_OPTIONS as AO


@click.group()
@click.pass_context
@click.option(*AO['verbosity'].cli, **AO['verbosity'].kwargs)
@click.option(*AO['logfile'].cli, **AO['logfile'].kwargs)
@click.version_option(*AO['version'].cli, **AO['version'].kwargs)
@click.option(*AO['config'].cli, **AO['config'].kwargs)
@click.option(*AO['user_data_dir'].cli, **AO['user_data_dir'].kwargs)
@click.option(*AO['db_name'].cli, **AO['db_name'].kwargs)
@click.option(*AO['db_path'].cli, **AO['db_path'].kwargs)
@click.option(*AO['db_host'].cli, **AO['db_host'].kwargs)
@click.option(*AO['db_user'].cli, **AO['db_user'].kwargs)
@click.option(*AO['db_port'].cli, **AO['db_port'].kwargs)
def cli(ctx, verbose, logfile, config, user_data_dir,
db_name, db_path, db_host, db_user, db_port):
    setup_logging_pre()
    ctx.ensure_object(dict)
    args = {
        'verbosity': verbose,
        'logfile': logfile,
        'config': config,
        'user_data_dir': user_data_dir,
        'db_name': db_name,
        'db_path': db_path,
        'db_host': db_host,
        'db_user': db_user,
        'db_port': db_port,
    }
    ctx.obj.update(args)


@cli.command()
@click.pass_context
@click.option(*AO['startAt'].cli, **AO['startAt'].kwargs)
@click.option(*AO['endAt'].cli, **AO['endAt'].kwargs)
def sync(ctx,start_at,end_at):
    args = {
        'startAt': start_at,
        'endAt': end_at,
    }
    ctx.obj.update(args)
    start_sync(ctx)

@cli.command()
def trade():
    click.echo('trade')
    pass

@cli.command()
def backtest():
    click.echo('backtest')
    pass
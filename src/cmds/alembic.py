from alembic.config import Config
from alembic import command
import click
from pathlib import Path
relative_alembic_path= Path.cwd().parent / 'alembic.ini'
alembic_cfg = Config(relative_alembic_path)

# alembic cmd alembic.command.revision
@click.command()
@click.option('-c', '--config')


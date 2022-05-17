#TODO: In testing can't work now.
import click
from cmds.cli_option import AVAILABLE_CLI_OPTIONS as AO

# source code from https://github.com/pallets/click/issues/108
# similar option https://stackoverflow.com/questions/40182157/shared-options-and-flags-between-commands

class State():
    def __init__(self):
        self.verbosity = 0
        self.debug = False
    
pass_state = click.make_pass_decorator(State, ensure=True)

def verbosity_option(f, cli_options):
    cli = cli_options.cli
    kw = cli_options.kwargs
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.verbosity = value
        return value
    return click.option(*cli, **kw, callback=callback)(f)

def common_options(f):
    f = verbosity_option(f, AO['verbosity'])
    return f

@click.command()
@common_options
@pass_state
def cmd1(state):
    click.echo(f'Verbosity: {state.verbosity}')




import click

class State():
    def __init__(self):
        self.verbosity = 0
        self.debug = False
    
pass_state = click.make_pass_decorator(State, ensure=True)

def verbosity_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.verbosity = value
        return value
    return click.option()
import click

class State():
    def __init__(self):
        self.verbosity = 0
        self.debug = False
    
pass_state = click.make_pass_decorator(State, ensure=True)

def verbosity_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.verbosity = value
        return value
    return click.option(param)(f)




import aspectlib
import logging
import inspect


FORMAT = '%(asctime)s %(message)s'
log = logging.getLogger(__name__)
logging.basicConfig(filename='method-calls.log', level=logging.DEBUG, format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')


@aspectlib.Aspect(bind=True)
def _log_function(cut_point, *args, **kwargs):
    log.debug("`%s` called with args: %s kwargs: %s" % (cut_point.__qualname__, args, kwargs))

    try:
        yield
        log.debug("`%s` returned successfully..." % (cut_point.__qualname__,))
    except Exception as exc:
        print("Exception raised in `%s` %r for %s/%s" % (cut_point.__qualname__, exc, args, kwargs))
        raise


def weave(module_name):
    components = inspect.getmembers(module_name, lambda x: inspect.isfunction(x) or x == inspect.isclass(x))
    [aspectlib.weave(obj, _log_function) for name, obj in components]

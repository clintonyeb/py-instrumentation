import aspectlib
import logging

logging.basicConfig(filename='method-calls.log', level=logging.DEBUG)
log = logging.getLogger(__name__)


@aspectlib.Aspect(bind=True)
def log_function(cut_point, *args, **kwargs):
    log.debug("`%s` in class `%s` got called with args: %s kwargs: %s" % (cut_point.__name__, cut_point.__qualname__, args, kwargs))

    try:
        yield
        log.debug("`%s` in class `%s` returned successfully..." % (cut_point.__name__, cut_point.__qualname__))
    except Exception as exc:
        print("Exception raised in `%s` from class `%s` %r for %s/%s" % (cut_point.__name__, cut_point.__qualname__, exc, args, kwargs))
        raise

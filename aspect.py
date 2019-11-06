import aspectlib
import logging

FORMAT = '%(asctime)s %(message)s'
log = logging.getLogger(__name__)
logging.basicConfig(filename='method-calls.log', level=logging.DEBUG, format=FORMAT)


@aspectlib.Aspect(bind=True)
def log_function(cut_point, *args, **kwargs):
    log.debug("`%s` called with args: %s kwargs: %s" % (cut_point.__qualname__, args, kwargs))

    try:
        yield
        log.debug("`%s` returned successfully..." % (cut_point.__qualname__,))
    except Exception as exc:
        print("Exception raised in `%s` %r for %s/%s" % (cut_point.__qualname__, exc, args, kwargs))
        raise

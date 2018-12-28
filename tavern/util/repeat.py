# -*- coding: utf-8 -*-
import logging
from functools import wraps

from future.utils import raise_from

from . import exceptions
from .delay import delay

logger = logging.getLogger(__name__)


def repeat(stage):
    """Look for retry and try to repeat the stage `retry` times.

    Args:
        stage (dict): test stage
    """

    times = stage.get('times', 1)

    if times == 1:
        # Just return the plain function
        return lambda fn: fn

    def repeat_wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            for i in range(times):
                logger.info("Stage '%s' repeat for %i time.", stage['name'], i + 1)
                fn(*args, **kwargs)
        return wrapped

    return repeat_wrapper

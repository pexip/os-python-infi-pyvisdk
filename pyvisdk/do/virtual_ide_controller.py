
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualIDEController(vim, *args, **kwargs):
    '''The VirtualIDEController data object type specifies a virtual IDE controller.'''

    obj = vim.client.factory.create('{urn:vim25}VirtualIDEController')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'busNumber', 'key' ]
    optional = [ 'device', 'backing', 'connectable', 'controllerKey', 'deviceInfo',
        'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj

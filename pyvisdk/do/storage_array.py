
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageArray(vim, *args, **kwargs):
    '''This data object represents the storage array.'''

    obj = vim.client.factory.create('{urn:sms}StorageArray')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'modelId', 'name', 'uuid', 'vendorId' ]
    optional = [ 'alternateName', 'firmware', 'supportedBlockInterface',
        'supportedFileSystemInterface', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj

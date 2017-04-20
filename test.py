def foo(bar, baz):
    print ('hello {0}'.format(bar))
    return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

# tuple of args for foo
async_result = pool.apply_async(foo, ('world', 'foo'))

# do some other stuff in the main process

# get the return value from your function.
return_val = async_result.get()

print(return_val)

print(type(return_val))
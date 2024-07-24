from functools import wraps

def decorator(func):
	def __func_wrapper(*args, **kwargs):
		print('Start of __func_wrapper')
		value = func(*args, **kwargs)
		print(f"Result is: {value}")
		print('End of __func_wrapper')
		return value

	return __func_wrapper


def foo(arg1, arg2):
	return arg1 + arg2


new_func = decorator(foo)
result =  new_func(1, 2)

print("----")

@decorator
def foo2(arg1, arg2):
	return arg1 + arg2


new_func = decorator(foo)
result =  new_func(1, 2)
print(f"Result is: {result}")

print("----")

# Note that foo and foo2 have the same behavior - the @ operator
# just calls the decorator and assigns the result to the name foo2.

def decorator_with_argument(key):

	def __new_decorator(func):

		def __func_wrapper(*args, **kwargs):
			print(f'Key is: {key}')
			print('Start of __func_wrapper')
			value = func(*args, **kwargs)
			print('End of __func_wrapper')
			return value

		return __func_wrapper

	return __new_decorator

new_decorator = decorator_with_argument("Drew is awesome")
new_func = new_decorator(foo)
result = new_func(1, 2)
print(f"Result is: {result}")

print("----")

@decorator_with_argument("Drew is awesome")
def foo3(arg1, arg2):
	return arg1 + arg2

result = foo3(1, 2)
print(f"Result is: {result}")
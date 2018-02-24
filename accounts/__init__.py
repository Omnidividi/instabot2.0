__all__ = []

import pkgutil
import inspect

configs = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
	module = loader.find_module(name).load_module(name)

	for name, value in inspect.getmembers(module):
		if name.startswith('__') or name.startswith("os"):
			continue

		configs.append(getattr(module, name))
		__all__.append(name)
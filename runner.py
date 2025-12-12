import argparse
import importlib.util
import pathlib
import sys

from loguru import logger


def configure_logging(verbosity: int, path: str = None):
    # Remove default handler
    logger.remove()

    # Map verbosity → loguru level
    if verbosity == 0:
        level = "INFO"
        logger.add(sys.stderr, level=level, format="{message}")
    elif verbosity == 1:
        level = "DEBUG"
        logger.add(sys.stderr, level=level)
    else:
        level = "TRACE"
        logger.add(sys.stderr, level=level)

    logger.debug(f"Logging initialized at {level=}, {verbosity=}")
    if path:
        logger.add(path, level=level, rotation="10 MB")
        logger.debug(f"Logging to file: {path}")


def list_available_modules(directory: str = "codes"):
    """Return a sorted list of module names (without .py)."""
    base_path = pathlib.Path(directory)
    if not base_path.exists():
        return []

    return sorted(
        p.stem
        for p in base_path.glob("*.py")
        if p.is_file() and not p.name.startswith("_")
    )


def show_available_modules(directory: str = "codes"):
    """Print available modules in the specified directory."""
    possibilities = list_available_modules(directory)
    if possibilities:
        logger.info("Available modules:")
        for mod in possibilities:
            logger.info(f"  - {mod}")
    else:
        logger.warning("No modules found in directory.")


def load_module(module_name: str, directory: str = "codes"):
    """Dynamically load a Python module from a directory."""
    # check if module name has a directory prefix
    if "." in module_name:
        directory, module_name = module_name.rsplit(".", 1)
    package_name = f"{directory}.{module_name}"

    try:
        module = importlib.import_module(package_name)
    except ModuleNotFoundError:
        logger.error(f"Module '{module_name}' not found in '{directory}/'.")
        show_available_modules(directory)
        sys.exit(1)

    logger.debug(f"Module '{module_name}' loaded via importlib.")
    return module


def run_module_functions(module, function_name: str = ""):
    """Run all public callables in the module."""
    functions = {
        name: obj
        for name, obj in module.__dict__.items()
        if callable(obj)
        and not name.startswith("_")  # no private functions
        and getattr(obj, "__module__", None) == module.__name__  # only local functions
    }

    if not functions:
        logger.warning("No public functions found to execute.")
        return

    max_len = max(len(name) for name in functions)
    logger.debug(f"Functions discovered: {list(functions.keys())}")

    for name, func in functions.items():
        if function_name == "" or name == function_name:
            logger.debug(f"Running {module.__name__} {name}()...")
            try:
                result = func()
                logger.info(f"{module.__name__}.{name.ljust(max_len)} : {result}")
            except Exception as e:
                logger.exception(f"Error while executing {name}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Execute public functions of a module in daily_codes/"
    )
    parser.add_argument("module", help="Module name without .py")
    parser.add_argument(
        "function_name", help="Function name prefix to filter", nargs="?", default=""
    )
    parser.add_argument("-l", help="Log file path", default=None)
    parser.add_argument(
        "-v", action="count", default=0, help="Increase verbosity (-v, -vv, -vvv)"
    )
    if len(sys.argv) == 1:
        parser.print_help()
        configure_logging(0)
        show_available_modules()
        sys.exit(0)

    args = parser.parse_args()

    configure_logging(args.v, args.l)
    module = load_module(args.module)
    function_name = args.function_name
    run_module_functions(module, function_name)


if __name__ == "__main__":
    main()

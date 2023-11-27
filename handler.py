import importlib.util
from config.module_mapping import FILE_PATH


def run_module(file_path, method, params):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.run(method, params)
    return result


def handle(method, params):
    file_path = FILE_PATH.get(method)  # todo
    if file_path:
        return run_module(file_path, method, params)
    else:
        return "传入method类型不符，请重新输入"


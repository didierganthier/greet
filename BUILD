py_library(
  name = "app",
  srcs = glob(["app/**/*.py"]),
  deps = ["@python//:template"],
)

py_binary(
  name = "server",
  srcs = ["main.py"],
  deps = [":app"],
)


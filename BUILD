load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

package(default_visibility = ["//litter_box:__subpackages__"])

exports_files(
    [
        "ruff.toml",
    ],
    visibility = ["//tools/format:lint_access_group"],
)

py_binary(
    name = "litter_box",
    srcs = ["litter_box.py"],
    main = "litter_box.py",
    deps = [
        "@pypi//flask",
    ],
)

py_test(
    name = "litter_box_test",
    srcs = ["litter_box_test.py"],
    deps = [
        ":litter_box",
    ],
)

alias(
    name = "format",
    actual = "//tools/format",
)

py_library(
    name = "all_files",
    srcs = glob(["**/*.py"]),
)

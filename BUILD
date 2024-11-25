load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

package(default_visibility = ["//litter_box:__subpackages__"])

py_binary(
    name = "litter_box",
    srcs = ["litter_box.py"],
    main = "litter_box.py",
    deps = [
        "@pypi//flask",
    ]
)

py_test(
    name = "litter_box_test",
    srcs = ["litter_box_test.py"],
    deps = [
        ":litter_box",
    ],
)

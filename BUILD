load("@aspect_bazel_lib//lib:expand_template.bzl", "expand_template")
load("@pypi//:requirements.bzl", "requirement")
load("@rules_oci//oci:defs.bzl", "oci_push")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("//:py_layer.bzl", "py_oci_image")

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

# Build the container image
py_oci_image(
    name = "image",
    base = "@python_base",
    binary = "litter_box",
    entrypoint = ["/litter_box"],
)

#Create a file with the image tag and registry destination
expand_template(
    name = "stamped",
    out = "_stamped.txt",
    stamp_substitutions = {"v0.0.0 repo": "{{BUILD_EMBED_LABEL}}"},
    template = ["v0.0.0 repo"],
)

genrule(
    name = "parse_version",
    srcs = [":stamped"],
    outs = [
        "image_tag.tags.txt",
        "repo.txt",
    ],
    cmd = """
    awk '{print $$1}' $(location :stamped) > $(location image_tag.tags.txt)
    awk '{print $$2}' $(location :stamped) > $(location repo.txt)
    """,
)

# Push the container image to the registry
oci_push(
    name = "push_image",
    image = ":image",
    remote_tags = ":image_tag.tags.txt",
    repository_file = ":repo.txt",
)

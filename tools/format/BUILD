load("@aspect_rules_lint//format:defs.bzl", "format_multirun")

package(default_visibility = ["format_access_group"])

package_group(
    name = "format_access_group",
    packages = [
        "//",
    ],
)

package_group(
    name = "lint_access_group",
    packages = [
        "//tools/format",
    ],
)

format_multirun(
    name = "format",
    python = "@aspect_rules_lint//format:ruff",
    starlark = "@buildifier_prebuilt//:buildifier",
)

import os
import subprocess

bazel_tags_to_autogenerate = [
    "bsoncolumn_bm",
    "mongo_benchmark",
    "mongo_fuzzer_test",
    "mongo_integration_test",
    "mongo_unittest",
    "mongo_unittest_first_group",
    "mongo_unittest_second_group",
    "mongo_unittest_third_group",
    "mongo_unittest_fourth_group",
    "mongo_unittest_fifth_group",
    "mongo_unittest_sixth_group",
    "mongo_unittest_seventh_group",
    "mongo_unittest_eighth_group",
    "query_bm",
    "repl_bm",
    "sharding_bm",
    "sep_bm",
    "storage_bm",
    "first_half_bm",
    "second_half_bm",
]


def autogenerate_targets(args, bazel):
    bazel_autogenerate_flag = "include_autogenerated_targets"
    output_file = os.path.join(
        "src", "mongo", "db", "modules", "enterprise", "autogenerated_targets", "BUILD.bazel"
    )
    if not any(bazel_autogenerate_flag in arg for arg in args):
        if os.path.exists(output_file):
            os.remove(output_file)
        return
    generate_targets(args, bazel, output_file)


def generate_targets(
    args=[],
    bazel="bazel",
    output_file=os.path.join(
        "src", "mongo", "db", "modules", "enterprise", "autogenerated_targets", "BUILD.bazel"
    ),
):
    targets = []
    for tag in bazel_tags_to_autogenerate:
        labels = get_bazel_labels_from_tags(args, bazel, tag)
        filtered_labels = filter_labels(labels)
        targets.append(create_target(tag, filtered_labels))
    write_bazel_file(targets, output_file)


def get_bazel_labels_from_tags(args, bazel, tag):
    # This way we mostly keep the passed config, this parsing isn't perfect
    # for the ways you can call bazel configs but this should mostly just be used in CI
    # where we control how things are called
    extra_args = [arg for arg in args if arg.startswith("--")]
    # The .cquery file is used to get info on which targets are compatible
    # with our current config. Without it dependent targets would just be skipped.
    proc = subprocess.run(
        [bazel, "cquery", "--config=local"]
        + extra_args
        + [
            f"kind(extract_debuginfo_test, attr(tags, '\\b{tag}\\b', //src/...))",
            "--output=starlark",
            "--starlark:file=bazel/wrapper_hook/target_compatable.cquery",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.stdout.splitlines()


# We need to filter out any labels who do not get built in our current configuration
def filter_labels(labels):
    filtered_labels = set()
    for label in labels:
        label_name, can_build = label.split(" ")
        if can_build == "True":
            # Labels get passed with an @ sign
            filtered_labels.add(label_name[1:])
    return filtered_labels


def create_target(tag, labels):
    target = []
    target.append("filegroup(")
    target.append(f'    name="{tag}",')
    target.append("    srcs=[")
    for label in labels:
        target.append(f'        "{label}",')
    target.append("    ],")
    target.append("    testonly=True,")
    target.append('    visibility=["//visibility:public"],')
    target.append(")")
    return "\n".join(target)


# We default write the enterprise directory so we can access both bazel package targets
def write_bazel_file(targets, output_file):
    with open(output_file, "w") as buildfile:
        for target in targets:
            buildfile.write(target + "\n\n")


if __name__ == "__main__":
    generate_targets()

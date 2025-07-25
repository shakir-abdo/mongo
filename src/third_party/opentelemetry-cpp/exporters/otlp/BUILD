# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

load("//bazel:mongo_src_rules.bzl", "mongo_cc_library")
load("//src/third_party/opentelemetry-cpp:otel_rules.bzl", "OTEL_COPTS", "OTEL_TARGET_COMPATIBLE_WITH")

package(default_visibility = ["//visibility:public"])

mongo_cc_library(
    name = "otlp_recordable",
    srcs = [
        "src/otlp_environment.cc",
        "src/otlp_metric_utils.cc",
        "src/otlp_populate_attribute_utils.cc",
        "src/otlp_recordable.cc",
        "src/otlp_recordable_utils.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_metric_utils.h",
        "include/opentelemetry/exporters/otlp/otlp_populate_attribute_utils.h",
        "include/opentelemetry/exporters/otlp/otlp_preferred_temporality.h",
        "include/opentelemetry/exporters/otlp/otlp_recordable.h",
        "include/opentelemetry/exporters/otlp/otlp_recordable_utils.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    includes = [
        # Any target depending on "//src/third_party/opentelemetry-cpp/exporters/otlp" also gets
        # "src/third_party/opentelemetry-cpp/exporters/otlp/include" added to the include path.
        "include",
    ],
    strip_include_prefix = "include",
    tags = ["otlp"],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        "//src/third_party/opentelemetry-cpp/sdk/src/resource",
        "//src/third_party/opentelemetry-cpp/sdk/src/trace",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
        "//src/third_party/opentelemetry-proto:metrics_proto_cc",
        "//src/third_party/opentelemetry-proto:metrics_service_proto_cc",
        "//src/third_party/opentelemetry-proto:resource_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_service_proto_cc",
    ],
)

mongo_cc_library(
    name = "otlp_http_client",
    srcs = [
        "src/otlp_http.cc",
        "src/otlp_http_client.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_http.h",
        "include/opentelemetry/exporters/otlp/otlp_http_client.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = [
        "-DCURL_STATICLIB",
    ] + OTEL_COPTS,
    linkopts = select({
        "@platforms//os:windows": [
            "-DEFAULTLIB:advapi32.lib",
            "-DEFAULTLIB:crypt32.lib",
        ],
        "//conditions:default": [],
    }),
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_http",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        "//src/third_party/abseil-cpp:absl_strings",
        "//src/third_party/nlohmann-json:json",
        "//src/third_party/opentelemetry-cpp/api",
        "//src/third_party/opentelemetry-cpp/ext/src/http/client/curl:http_client_curl",
        "//src/third_party/opentelemetry-cpp/sdk:headers",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:base64",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
    ],
)

# "metric" exporters should probably be in their own library, but I added them to the existing
# library for the sake of simplicity.
mongo_cc_library(
    name = "otlp_http_exporter",
    srcs = [
        "src/otlp_http_exporter.cc",
        "src/otlp_http_exporter_factory.cc",
        "src/otlp_http_exporter_options.cc",
        "src/otlp_http_metric_exporter.cc",
        "src/otlp_http_metric_exporter_factory.cc",
        "src/otlp_http_metric_exporter_options.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_http_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_http_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_http_exporter_options.h",
        "include/opentelemetry/exporters/otlp/otlp_http_metric_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_http_metric_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_http_metric_exporter_options.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_http",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        ":otlp_http_client",
        ":otlp_recordable",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-cpp/sdk/src/trace",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
        "//src/third_party/opentelemetry-proto:resource_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_service_proto_cc",
    ],
)

mongo_cc_library(
    name = "otlp_file_client",
    srcs = [
        "src/otlp_file_client.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_file_client.h",
        "include/opentelemetry/exporters/otlp/otlp_file_client_options.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_file",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        "//src/third_party/abseil-cpp:absl_strings",
        "//src/third_party/nlohmann-json:json",
        "//src/third_party/opentelemetry-cpp/api",
        "//src/third_party/opentelemetry-cpp/sdk:headers",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:base64",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
    ],
)

# "metric" exporters should probably be in their own library, but I added them to the existing
# library for the sake of simplicity.
mongo_cc_library(
    name = "otlp_file_exporter",
    srcs = [
        "src/otlp_file_exporter.cc",
        "src/otlp_file_exporter_factory.cc",
        "src/otlp_file_exporter_options.cc",
        "src/otlp_file_metric_exporter.cc",
        "src/otlp_file_metric_exporter_factory.cc",
        "src/otlp_file_metric_exporter_options.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_file_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_file_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_file_exporter_options.h",
        "include/opentelemetry/exporters/otlp/otlp_file_metric_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_file_metric_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_file_metric_exporter_options.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_file",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        ":otlp_file_client",
        ":otlp_recordable",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-cpp/sdk/src/trace",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
        "//src/third_party/opentelemetry-proto:resource_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_service_proto_cc",
    ],
)

mongo_cc_library(
    name = "otlp_grpc_client",
    srcs = [
        "src/otlp_grpc_client.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_client.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_client_options.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_grpc",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        "//src/third_party/abseil-cpp:absl_strings",
        "//src/third_party/grpc:grpc++",
        "//src/third_party/nlohmann-json:json",
        "//src/third_party/opentelemetry-cpp/api",
        "//src/third_party/opentelemetry-cpp/ext/src/http/client/curl:http_client_curl",
        "//src/third_party/opentelemetry-cpp/sdk:headers",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:base64",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
        "//src/third_party/opentelemetry-proto:logs_service",
        "//src/third_party/opentelemetry-proto:metrics_service",
        "//src/third_party/opentelemetry-proto:trace_service",
    ],
)

mongo_cc_library(
    name = "otlp_grpc_exporter",
    srcs = [
        "src/otlp_grpc_exporter.cc",
        "src/otlp_grpc_exporter_factory.cc",
        "src/otlp_grpc_exporter_options.cc",
        "src/otlp_grpc_metric_exporter.cc",
        "src/otlp_grpc_metric_exporter_factory.cc",
        "src/otlp_grpc_metric_exporter_options.cc",
        "src/otlp_grpc_utils.cc",
    ],
    hdrs = [
        "include/opentelemetry/exporters/otlp/otlp_environment.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_exporter_options.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_metric_exporter.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_metric_exporter_factory.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_metric_exporter_options.h",
        "include/opentelemetry/exporters/otlp/otlp_grpc_utils.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_prefix.h",
        "include/opentelemetry/exporters/otlp/protobuf_include_suffix.h",
    ],
    copts = OTEL_COPTS,
    strip_include_prefix = "include",
    tags = [
        "otlp",
        "otlp_grpc",
    ],
    target_compatible_with = OTEL_TARGET_COMPATIBLE_WITH,
    deps = [
        ":otlp_grpc_client",
        ":otlp_recordable",
        "//src/third_party/opentelemetry-cpp/sdk/src/common:global_log_handler",
        "//src/third_party/opentelemetry-cpp/sdk/src/trace",
        "//src/third_party/opentelemetry-proto:common_proto_cc",
        "//src/third_party/opentelemetry-proto:resource_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_proto_cc",
        "//src/third_party/opentelemetry-proto:trace_service",
    ],
)

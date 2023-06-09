from prefect.infrastructure import KubernetesJob, KubernetesImagePullPolicy

k8s_job = KubernetesJob(
    namespace="prod",
    image="prefecthq/prefect:2-python3.9",
    image_pull_policy=KubernetesImagePullPolicy.IF_NOT_PRESENT,
    env={"EXTRA_PIP_PACKAGES": "s3fs", "PREFECT_LOGGING_LEVEL": "DEBUG"},
)
k8s_job.save("prod", overwrite=True)

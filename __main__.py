import pulumi
import pulumi_kubernetes as kubernetes

# Deploying the itzg/minecraft-server Helm chart on Kubernetes using Pulumi
minecraft_release = kubernetes.helm.v3.Release("minecraft-server",
    chart="minecraft",
    version="3.1.3",
    repository_opts=kubernetes.helm.v3.RepositoryOptsArgs(
        repo="https://itzg.github.io/minecraft-server-charts/"
    ),
    values={
        "minecraftServer": {
            "eula": "TRUE",
            # Additional configuration options can be set here,
            # such as `type`, `difficulty`, `whitelist`, etc.
        }
    }
)

# Export the release name of the Minecraft server
pulumi.export("minecraft_release_name", minecraft_release.name)
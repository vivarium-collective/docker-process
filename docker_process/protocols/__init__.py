from docker_process.protocols.docker_protocol import DockerProtocol


def register_types(core):
    core.register_types({
        'docker': DockerProtocol})

    return core


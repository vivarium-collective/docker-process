import pytest

from bigraph_schema import allocate_core
from process_bigraph import Composite

import docker_process
from docker_process import DockerProtocol


def test_docker_process(core):
    state = {
        'mass': 1.0,
        'julia-process': {
            '_type': 'process',
            'address': {
                'protocol': 'docker',
                'data': {
                    'image': 'julia-process:latest',
                    'port': 11111}},
            'config': {
                'rate': 0.005},
            'inputs': {
                'mass': ['mass']},
            'outputs': {
                'mass_delta': ['mass']},
            'interval': 0.7}}

    composite = Composite({
        'state': state}, core=core)

    composite.run(11.111)

    assert composite.state['mass'] > 1.0


@pytest.fixture
def core():
    return allocate_core()


if __name__ == '__main__':
    core = allocate_core()
    test_docker_process(core)

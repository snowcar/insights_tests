import pytest


@pytest.fixture(scope="class", autouse=True)
def send_request_for_test(request):
    cls = request.node
    if hasattr(cls.obj, "send_request"):
        cls.obj.send_request()

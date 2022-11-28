import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.sentry.tests.mocked_requests import event, issue


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def headers():
    return {
        'sentry-hook-resource': 'issue',
    }


SENTRY_INSTALLATION_UUID = "7a485448-a9e2-4c85-8a3c-4f44175783c9"


@pytest.fixture
def installation():
    return {
        "app": {
            "uuid": "64bf2cf4-37ca-4365-8dd3-6b6e56d741b8",
            "slug": "app",
        },
        "organization": {
            "slug": "example",
        },
        "uuid": SENTRY_INSTALLATION_UUID,
    }


@pytest.fixture
def issue_resolved_webhook(installation):
    return {
        'action': 'resolved',
        'data': {'issue': issue},
        'installation': installation,
    }


@pytest.fixture
def alert_triggered_webhook(installation):
    return {
        "action": "triggered",
        "data": {"event": event},
        "installation": installation,
    }

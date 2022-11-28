import pytest


@pytest.fixture
def mocked_basecamp_send_message(mocker):
    return mocker.patch('src.basecamp.campfire_bot.CampfireBot.send_message')


def test_response_if_issue(client, issue_resolved_webhook, headers, mocked_basecamp_send_message):
    response = client.post('/api/sentry/webhook', json=issue_resolved_webhook, headers=headers)

    assert response.status_code == 200
    mocked_basecamp_send_message.assert_called_once()


def test_response_if_alert(client, alert_triggered_webhook, headers, mocked_basecamp_send_message):
    headers['sentry-hook-resource'] = 'event-alert'
    response = client.post('/api/sentry/webhook', json=alert_triggered_webhook, headers=headers)

    assert response.status_code == 200
    mocked_basecamp_send_message.assert_called_once()


def test_bad_response_if_bad_headers(client, issue_resolved_webhook):
    response = client.post('/api/sentry/webhook', json=issue_resolved_webhook, headers={'missing': 'header'})

    assert response.status_code == 400


def test_bad_response_if_bad_content(client, issue_resolved_webhook, headers):
    response = client.post('/api/sentry/webhook', json={'malformed': True}, headers=headers)

    assert response.status_code == 422

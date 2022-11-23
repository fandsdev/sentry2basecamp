
def test_response_if_issue(client, issue_resolved_webhook, headers):
    response = client.post('/api/sentry/webhook', json=issue_resolved_webhook, headers=headers)

    assert response.status_code == 200


def test_response_if_alert(client, alert_triggered_webhook, headers):
    response = client.post('/api/sentry/webhook', json=alert_triggered_webhook, headers=headers)

    assert response.status_code == 200


def test_bad_response_if_bad_headers(client, issue_resolved_webhook):
    response = client.post('/api/sentry/webhook', json=issue_resolved_webhook, headers={'missing': 'header'})

    assert response.status_code == 400


def test_bad_response_if_bad_content(client, issue_resolved_webhook, headers):
    response = client.post('/api/sentry/webhook', json={'malformed': True}, headers=headers)

    assert response.status_code == 422

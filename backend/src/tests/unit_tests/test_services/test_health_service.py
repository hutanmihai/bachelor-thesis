from src.services.health_srv import HealthSrv


async def test_health_is_healthy(health_service: HealthSrv, sqlalchemy_repository_mock):
    sqlalchemy_repository_mock.ping.return_value = True

    result = await health_service.is_healthy()

    assert result is True
    sqlalchemy_repository_mock.ping.assert_awaited_once_with()


async def test_health_is_not_healthy(health_service: HealthSrv, sqlalchemy_repository_mock):
    sqlalchemy_repository_mock.ping.return_value = False

    result = await health_service.is_healthy()

    assert result is False
    sqlalchemy_repository_mock.ping.assert_awaited_once_with()

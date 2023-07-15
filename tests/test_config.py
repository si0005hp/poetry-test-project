# from poetry_test_project.config import Config
from poetry_test_project import Config


class TestConfig:
    def test(self):
        config = Config("development")

        assert config.id == "dev"

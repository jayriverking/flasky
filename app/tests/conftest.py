import pytest
from app import create_app
from app import db
from app.models.crystal import Crystal
from flask.signals import request_finished


@pytest.fixture
def app():
    # {"TESTING": True} can be used, but also any truthy value would work!
    # i.e., test_config=True
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def make_two_crystals(app):
    crystal1 = Crystal(
        name="Pearl",
        color="White",
        powers="Pretty Powers"
    )
    crystal2 = Crystal(
        name="Garnet",
        color="Red",
        powers="Awesome Powers"
    )
    db.session.add_all([crystal1, crystal2])
    db.session.commit()
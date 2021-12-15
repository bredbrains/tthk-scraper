from typing import Type, List

from sqlmodel import SQLModel, select

from tthk_scraper.database import get_session


class BaseService:
    def __init__(self, model: Type[SQLModel]):
        self.model = model
        self.session = get_session()
        self.table = self.model.__tablename__

    def get_all(self):
        statement = select(self.model)
        return self.session.exec(statement).all()

    def save(self, models):
        for model in models:
            model = self.model.from_orm(model)
            self.session.add(model)
        self.session.commit()

    def clear(self):
        statement = select(self.model)
        changes = self.session.exec(statement)
        for change in changes:
            self.session.delete(change)
        self.session.commit()

    def update(self, models, is_first: bool = False):
        if is_first:
            self.clear()
        self.restore_autoincrement()
        self.save(models)
        self.session.close()

    def restore_autoincrement(self):
        self.session.exec(f"ALTER TABLE {self.table} AUTO_INCREMENT = 1;")
        self.session.commit()

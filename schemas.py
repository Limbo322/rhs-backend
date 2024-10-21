import sqlalchemy

# Создание метаданных для SQLAlchemy
metadata = sqlalchemy.MetaData()

# Определение таблицы "film"
film_table = sqlalchemy.Table(
    "film",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("views", sqlalchemy.Integer),
)
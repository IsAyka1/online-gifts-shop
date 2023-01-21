from enum import Enum, unique

from sqlalchemy import (
    Column, Date, Enum as sqlEnum, ForeignKey, ForeignKeyConstraint, Integer,
    String, Table, MetaData
)

convention = {  # templates for names
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    # indexes
    'ix': 'ix__%(table_name)s__%(all_column_names)s',

    # unique indexes
    'uq': 'uq__%(table_name)s__%(all_column_names)s',

    #  CHECK-constraints
    'ck': 'ck__%(table_name)s__%(constraint_name)s',

    # foreign keys
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',

    # primary keys
    'pk': 'pk__%(table_name)s'
}
metadata = MetaData(naming_convention=convention)


@unique
class Gender(Enum):
    female = 'female'
    male = 'male'


imports_table = Table(
    'imports',
    metadata,
    Column('import_id', Integer, primary_key=True)
)

citizens_table = Table(
    'citizens',
    metadata,
    Column('import_id', Integer, ForeignKey('imports.import_id'), primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('birth_date', Date, nullable=False),
    Column('gender', sqlEnum(Gender, 'gender'), nullable=False),
    Column('town', String, nullable=False),
    Column('street', String, nullable=False),
    Column('building', String, nullable=False),
    Column('apartment', Integer, nullable=False)
)

relatives_table = Table(
    'relatives',
    metadata,
    Column('import_id', Integer,  primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('relative_id', Integer, primary_key=True),
    ForeignKeyConstraint(
        ('import_id', 'citizen_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    ),
    ForeignKeyConstraint(
        ('import_id', 'relative_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    )
)

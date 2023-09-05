from django.core.management import BaseCommand
import psycopg2
import psycopg2.errors
from config.settings import database_name, database_password, database_host, database_port, database_user


class Command(BaseCommand):
    """Command need to create database"""

    def handle(self, *args, **options):
        conn = psycopg2.connect(
            database='postgres',
            user=database_user,
            password=database_password,
            host=database_host,
            port=database_port
        )
        conn.autocommit = True
        cur = conn.cursor()

        try:
            cur.execute(f"CREATE DATABASE {database_name}")
        except psycopg2.errors.DuplicateDatabase:
            print(f'ОШИБКА: база данных {database_name} уже существует')
        conn.close()

# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""
from dataclasses import dataclass
from typing import Optional

from models.teacher import Teacher
from daos.dao import Dao


@dataclass
class TeacherDao(Dao[Teacher]):

    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """

        """
        teacher: Optional[Teacher]
        with Dao.connection.cursor() as cursor:
            sql = """
        SELECT 
            t.id_teacher, 
            t.hiring_date,
            p.first_name,
            p.last_name,
            p.age
        FROM 
            teacher t
        INNER JOIN 
            person p ON t.id_person = p.id_person
        WHERE 
            t.id_teacher = %s
        """
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'], record['last_name'], record['age'], record['hiring_date'])
            teacher.id = record["id_teacher"]
        else:
            teacher = None
        return teacher

    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, teacher: Teacher) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True

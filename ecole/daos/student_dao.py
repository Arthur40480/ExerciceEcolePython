# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""
from dataclasses import dataclass
from typing import Optional

from ecole.daos.dao import Dao
from ecole.models.student import Student


@dataclass
class StudentDao(Dao[Student]):

    def create(self, student: Student) -> int:
        """Crée en BD l'entité Student correspondant au student obj

        :param student: à créer sous forme d'entité Student en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_student: int) -> Optional[Student]:
        """Renvoi l'étudiant correspondant à l'entité dont l'id est id_student
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]
        with Dao.connection.cursor() as cursor:
            sql = """
        SELECT  
            s.student_nbr,
            p.first_name,
            p.last_name,
            p.age
        FROM 
            student s
        INNER JOIN 
            person p ON s.id_person = p.id_person
        WHERE 
            s.student_nbr = %s
        """
            cursor.execute(sql, (id_student, ))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'], record['last_name'], record['age'])
            student.id = record["student_nbr"]
        else:
            student = None
        return student

    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Student correspondant à student, pour y correspondre

        :param student: étudiant déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Student correspondant à student

        :param student: cours dont l'entité Student correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True


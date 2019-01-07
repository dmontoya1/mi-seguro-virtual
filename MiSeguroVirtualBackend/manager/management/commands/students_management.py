# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.core.management.base import BaseCommand
from schools.models import Student


class Command(BaseCommand):

    help = 'Activa o Inactiva estudiantes dependiendo de los atributos del modelo: \
    inactive_start_date e inactive_end_date'

    def handle(self, *args, **options):

        #Contador alumnos inactivos
        inactive_students = 0
        scheduled_students = 0
        non_scheduled_students = 0

        students = Student.objects.all()
        today = datetime.now()
        for student in students:
            try:
                if student.inactive_start_date < today < student.inactive_end_date:
                    print "Esta dentro del rango inactivo"
                    print "Inactivando Usuario..."
                    student.active = False
                    student.save()
                    inactive_students += 1
                elif student.inactive_end_date < today:
                    print "Ya paso el rango de fechas de inactivar el estudiante"
                    print "Activando Estudiante..."
                    student.active = True
                    student.inactive_start_date = None
                    student.inactive_end_date = None
                    student.save()
                elif student.inactive_start_date > today:
                    print "Estudiante próximo a inactivar..."
                    scheduled_students += 1
            except Exception, e:
                if student.active is False:
                    student.active = True
                    student.save()
                print "No tiene inactivaciones pendientes"
                non_scheduled_students += 1

        self.stdout.write(self.style.SUCCESS('Cantidad de Estudiantes inactivados: %s' % inactive_students))
        self.stdout.write(self.style.SUCCESS('Cantidad de Estudiantes próximos a inactivar: %s' % scheduled_students))
        self.stdout.write(self.style.SUCCESS('Cantidad de Estudiantes sin inactivaciones pendientes %s' % non_scheduled_students))

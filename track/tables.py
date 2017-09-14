from math import modf

import django_tables2 as tables

from timer.models import Solve

class SolveTable(tables.Table):
    date = tables.Column()
    scramble = tables.Column()
    time = tables.Column(verbose_name='Time (seconds)', empty_values=())

    def render_time(self, record):
        secs = str(record.centiseconds / 100)
        sec_split = secs.split('.')
        part_one = sec_split[0]

        if len(sec_split) == 1:
            part_two = '00'
        else:
            part_two = sec_split[1]
            if len(part_two) == 1:
                part_two = part_two + '0'
        return part_one + '.' + part_two

    class Meta:
        model = Solve
        sequence = ('date', 'scramble', 'centiseconds')
        exclude = ('comments', 'puzzle', 'user', 'id', 'centiseconds')
        row_attrs = {
            'data-id': lambda record: record.id
        }
        attrs = {'class': 'paleblue'}

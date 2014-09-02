# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.type'
        db.add_column(u'tasks_task', 'type',
                      self.gf('django.db.models.fields.CharField')(default='S', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.type'
        db.delete_column(u'tasks_task', 'type')


    models = {
        u'tasks.graph': {
            'Meta': {'object_name': 'Graph'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'next'", 'to': u"orm['tasks.Task']"}),
            'prev': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prev'", 'to': u"orm['tasks.Task']"})
        },
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'example_solution': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'task_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.TaskSet']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'})
        },
        u'tasks.taskset': {
            'Meta': {'object_name': 'TaskSet'},
            'id': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['tasks']
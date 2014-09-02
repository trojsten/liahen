# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaskSet'
        db.create_table(u'tasks_taskset', (
            ('id', self.gf('django.db.models.fields.SlugField')(max_length=50, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'tasks', ['TaskSet'])

        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            ('id', self.gf('django.db.models.fields.SlugField')(max_length=50, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('example_solution', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('task_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.TaskSet'])),
        ))
        db.send_create_signal(u'tasks', ['Task'])

        # Adding model 'Graph'
        db.create_table(u'tasks_graph', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prev', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prev', to=orm['tasks.Task'])),
            ('next', self.gf('django.db.models.fields.related.ForeignKey')(related_name='next', to=orm['tasks.Task'])),
        ))
        db.send_create_signal(u'tasks', ['Graph'])


    def backwards(self, orm):
        # Deleting model 'TaskSet'
        db.delete_table(u'tasks_taskset')

        # Deleting model 'Task'
        db.delete_table(u'tasks_task')

        # Deleting model 'Graph'
        db.delete_table(u'tasks_graph')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'tasks.taskset': {
            'Meta': {'object_name': 'TaskSet'},
            'id': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['tasks']
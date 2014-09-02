# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Test'
        db.delete_table(u'tasks_test')

        # Deleting model 'Graph'
        db.delete_table(u'tasks_graph')

        # Removing M2M table for field tests on 'Task'
        db.delete_table(db.shorten_name(u'tasks_task_tests'))

        # Adding M2M table for field edges on 'Task'
        m2m_table_name = db.shorten_name(u'tasks_task_edges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_task', models.ForeignKey(orm[u'tasks.task'], null=False)),
            ('to_task', models.ForeignKey(orm[u'tasks.task'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_task_id', 'to_task_id'])


    def backwards(self, orm):
        # Adding model 'Test'
        db.create_table(u'tasks_test', (
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tasks', ['Test'])

        # Adding model 'Graph'
        db.create_table(u'tasks_graph', (
            ('prev', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prev', to=orm['tasks.Task'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('next', self.gf('django.db.models.fields.related.ForeignKey')(related_name='next', to=orm['tasks.Task'])),
        ))
        db.send_create_signal(u'tasks', ['Graph'])

        # Adding M2M table for field tests on 'Task'
        m2m_table_name = db.shorten_name(u'tasks_task_tests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'tasks.task'], null=False)),
            ('test', models.ForeignKey(orm[u'tasks.test'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'test_id'])

        # Removing M2M table for field edges on 'Task'
        db.delete_table(db.shorten_name(u'tasks_task_edges'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tasks.stalker': {
            'Meta': {'object_name': 'Stalker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Task']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'edges': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'next'", 'symmetrical': 'False', 'to': u"orm['tasks.Task']"}),
            'example_solution': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'task_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.TaskSet']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Rozpravka\\n<h4>Zadanie</h4>\\n<h4>Form&aacute;t vstupu</h4>\\n<h4>Form&aacute;t v&yacute;stupu</h4>\\n<h4>Pr&iacute;klad</h4>'"}),
            'timestamps': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'through': u"orm['tasks.Stalker']", 'symmetrical': 'False'}),
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
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Status'
        db.create_table('issues_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('issues', ['Status'])

        # Adding model 'Project'
        db.create_table('issues_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('url_path', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('issues', ['Project'])

        # Adding model 'Issue'
        db.create_table('issues_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Status'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issues.Project'], null=True, blank=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('issues', ['Issue'])


    def backwards(self, orm):
        
        # Deleting model 'Status'
        db.delete_table('issues_status')

        # Deleting model 'Project'
        db.delete_table('issues_project')

        # Deleting model 'Issue'
        db.delete_table('issues_issue')


    models = {
        'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Project']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Status']"}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '800'})
        },
        'issues.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'url_path': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'issues.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['issues']

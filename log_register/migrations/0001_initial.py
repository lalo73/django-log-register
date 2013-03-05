# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lot'
        db.create_table('log_register_lot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('register_start', self.gf('django.db.models.fields.DateField')()),
            ('register_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('log_register', ['Lot'])

        # Adding model 'Log'
        db.create_table('log_register_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(related_name='logs', to=orm['log_register.Lot'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('extra_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.CharField')(default=20, max_length=5)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('log_register', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Lot'
        db.delete_table('log_register_lot')

        # Deleting model 'Log'
        db.delete_table('log_register_log')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'log_register.log': {
            'Meta': {'object_name': 'Log'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'extra_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': '20', 'max_length': '5'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['log_register.Lot']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'log_register.lot': {
            'Meta': {'object_name': 'Lot'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'register_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'register_start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['log_register']
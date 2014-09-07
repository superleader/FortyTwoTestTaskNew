# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.email'
        db.add_column(u'basic_person', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.skype'
        db.add_column(u'basic_person', 'skype',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.jabber'
        db.add_column(u'basic_person', 'jabber',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.photo'
        db.add_column(u'basic_person', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 9, 7, 0, 0), max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.email'
        db.delete_column(u'basic_person', 'email')

        # Deleting field 'Person.skype'
        db.delete_column(u'basic_person', 'skype')

        # Deleting field 'Person.jabber'
        db.delete_column(u'basic_person', 'jabber')

        # Deleting field 'Person.photo'
        db.delete_column(u'basic_person', 'photo')


    models = {
        u'basic.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'basic.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['basic']
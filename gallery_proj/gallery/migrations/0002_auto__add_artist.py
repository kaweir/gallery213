# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'gallery_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('profile_pic', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('picture_1', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture_2', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture_3', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture_4', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture_5', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture_6', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'gallery', ['Artist'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'gallery_artist')


    models = {
        u'gallery.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture_4': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture_5': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture_6': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'profile_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gallery']